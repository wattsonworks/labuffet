"""La Buffet media pipeline: dedupe, auto-orient, crop phone UI, HEIC->JPG,
resize to web sizes, emit WebP + JPG to img/. Run once."""
from __future__ import annotations
import hashlib, json, shutil, sys
from pathlib import Path
from PIL import Image, ImageOps
from pillow_heif import register_heif_opener
register_heif_opener()

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT
RAW = ROOT / "raw"
OUT = ROOT / "img"
RAW.mkdir(exist_ok=True)
OUT.mkdir(exist_ok=True)

# (source filename, output basename, crop_top%, crop_bottom%, note)
ITEMS = [
    ("UP SOLO.jpg",                                       "mezze-overhead",        0,    0, "HERO: 16-bowl mezze overhead w/ Way Inn napkins"),
    ("HOMMADE BAKE.jpg",                                  "homemade-bread",        0,    0, "Fresh bread rolls on parchment"),
    ("SIDEDUO.JPG",                                       "bread-salad-juice",     0,    0, "Bread + salad + OJ close-up"),
    ("SIDEQUATRO.jpg",                                    "table-for-four",        0,    0, "Full table set w/ shakshuka + mezze"),
    ("a28161ef-14a5-4fee-8c4a-938b233c0f5f.jpg",          "mezze-window",          0,    0, "Mezze table by blue gates"),
    ("1FC9B1F0-DE31-4762-9318-D193AB070DFC.jpg",          "bread-cut",             0,    0, "Cut homemade bread close-up"),
    ("9DD20605-7515-4376-8C7B-C1BB971695C1.jpg",          "dough-spirals",         0,    0, "Dough spirals prep"),
    ("CBEBAC93-62BB-4F34-A06A-EFFDE5839B09.jpg",          "nut-loaf",              0,    0, "Walnut/chocolate loaf"),
    ("IMG_6029.PNG",                                      "specialty-loaf",        0,    0, "Marbled walnut loaf in tin"),
    ("IMG_7281.HEIC",                                     "eggplant-tahini",       0,    0, "Smoked eggplant + tahini close-up"),
    ("IMG_8369.PNG",                                      "mezze-side",            0,    3, "Side view of mezze table"),
    ("IMG_8370.PNG",                                      "buffet-spread",         0,    3, "Sideboard buffet w/ cheeses & jams"),
    ("IMG_8372.PNG",                                      "dining-archway",       15,   28, "Dining room through stone archway"),
    ("IMG_8373.PNG",                                      "dining-wide",          15,   28, "Wide dining room view"),
    ("IMG_8377.PNG",                                      "mezze-marble",          0,    3, "Marble-top mezze table"),
    ("IMG_8378.PNG",                                      "dining-windows",        0,    3, "Stone dining room w/ arched windows"),
    ("IMG_8380.PNG",                                      "mezze-yogurt",          0,    3, "Mezze side with yogurt + olives"),
    ("IMG_8390.PNG",                                      "salatim-closeup",       0,    3, "Salatim close-up: beet, labneh, olives"),
    ("IMG_8400.JPG",                                      "courtyard-treeoflife",  0,    0, "Lit courtyard w/ Way Inn Tree-of-Life plaque"),
    ("IMG_8402.JPG",                                      "rooftop-banner",        0,    0, "Rooftop chairs + lanterns banner"),
    ("IMG_8403.JPG",                                      "courtyard-flowers",     0,    0, "Blue gates, flowers, courtyard table"),
    ("INTERIOR.JPG",                                      "dining-chairs",         0,    0, "Colorful chairs + patterned tiles"),
    ("SIDEBUFFET.JPG",                                    "dining-buffet-wide",    0,    0, "Wide dining room w/ mezze + open buffet"),
    ("SIDEBUFFET2.HEIC",                                  "dining-buffet-tall",    0,    0, "Open buffet by stone wall + Tree-of-Life art"),
]

# Output widths (px). Will only generate variants smaller than source width.
WIDTHS = [1920, 1280, 800]

# Files that are byte-identical dupes (will be moved to raw/ only)
DUPES = ["IMG_8369(1).PNG", "IMG_8370(1).PNG", "IMG_8390(1).PNG"]
# Files excluded entirely (still moved to raw/)
SKIP = ["IMG_7600.HEIC", "SIDESOLO.jpg"]
# Preview helper files to delete
TMP_PREVIEWS = ["IMG_7281_preview.jpg", "IMG_7600_preview.jpg", "SIDEBUFFET2_preview.jpg"]


def open_oriented(path: Path) -> Image.Image:
    im = Image.open(path)
    im = ImageOps.exif_transpose(im)
    return im.convert("RGB")


def process_one(src: Path, base: str, top_pct: int, bot_pct: int):
    im = open_oriented(src)
    w, h = im.size
    # crop phone chrome
    if top_pct or bot_pct:
        top = int(h * top_pct / 100)
        bot = int(h * (100 - bot_pct) / 100)
        im = im.crop((0, top, w, bot))
        w, h = im.size
    out_widths = sorted({tw for tw in WIDTHS if tw <= w} | {min(WIDTHS[-1], w)}, reverse=True)
    if not out_widths:
        out_widths = [w]
    saved = []
    for tw in out_widths:
        if tw == w:
            v = im
        else:
            th = round(h * tw / w)
            v = im.resize((tw, th), Image.LANCZOS)
        jpg = OUT / f"{base}-{tw}.jpg"
        wp  = OUT / f"{base}-{tw}.webp"
        v.save(jpg, "JPEG", quality=84, optimize=True, progressive=True)
        v.save(wp,  "WEBP", quality=80, method=6)
        saved.append((tw, jpg.stat().st_size, wp.stat().st_size))
    # also save the largest as canonical fallback for OG image
    if out_widths:
        big = max(out_widths)
        shutil.copyfile(OUT / f"{base}-{big}.jpg", OUT / f"{base}.jpg")
    return saved


def main():
    # 1. Move dupes and skips to raw/ (no processing)
    for f in DUPES + SKIP:
        p = SRC / f
        if p.exists():
            shutil.move(str(p), str(RAW / f))
    # 2. Clean temp previews
    for f in TMP_PREVIEWS:
        p = SRC / f
        if p.exists(): p.unlink()
    # 3. Process curated items
    manifest = []
    for fname, base, t, b, note in ITEMS:
        src = SRC / fname
        if not src.exists():
            # maybe already moved to raw?
            alt = RAW / fname
            if alt.exists():
                src = alt
            else:
                print(f"MISSING: {fname}", file=sys.stderr)
                continue
        try:
            saved = process_one(src, base, t, b)
            mf = {
                "src": fname, "base": base, "note": note,
                "crop_top_pct": t, "crop_bot_pct": b,
                "variants": [{"w": w, "jpg_kb": jk//1024, "webp_kb": wk//1024} for (w, jk, wk) in saved],
            }
            manifest.append(mf)
            print(f"OK  {fname:50s} -> {base:24s}  {saved}")
        except Exception as e:
            print(f"FAIL {fname}: {e}", file=sys.stderr)
        # move src into raw/ after processing (only if it was at SRC root)
        if src.parent == SRC:
            shutil.move(str(src), str(RAW / fname))
    # 4. Write manifest
    (ROOT / "scripts" / "manifest.json").write_text(json.dumps(manifest, indent=2))
    # 5. Move PROMPT.md out of repo root? Keep it — it's documentation.
    print(f"\nDone. {len(manifest)} curated images. raw/ has originals.")


if __name__ == "__main__":
    main()
