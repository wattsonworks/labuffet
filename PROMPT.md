# LA BUFFET — KICKOFF PROMPT (paste this as your first message in a NEW Claude Code session)

> Open a new Claude Code session in `C:\Users\sunnf\Desktop\LABUFFET` (this folder
> already holds the raw photos/videos) and paste everything below. The repo will be
> named **`labuffet`**. Build a stunning, mouth-watering one-page site for **La Buffet
> (לה בופה)** — the morning breakfast experience at **The Way Inn** boutique hotel in
> Safed. Read every file in this folder first, including the media.

---

You are building a **beautiful, appetite-driven breakfast site** for **La Buffet
(לה בופה)** — the **morning open-buffet / breakfast served 08:00–10:30 to the guests of
The Way Inn** suite hotel, in the heart of **Safed's Artists' Quarter (צפת)**, Israel.
The job is to make a hotel guest see the homemade bread and the table of mezze and
immediately want to reserve tomorrow's breakfast.

## GROUND TRUTH (from the owner — treat as fact)
- **What:** *La Buffet (לה בופה)* — the **breakfast** at **The Way Inn**. A generous,
  Mediterranean/Israeli morning spread (see photos): warm **homemade breads**, a big
  table of **salatim & spreads** (chopped Israeli salad, labneh, tahini, beet salad,
  olives, feta & local cheeses, dips), and more.
- **Hours:** **08:00 – 10:30**, daily *(confirm which days — see ASK).*
- **For:** **guests of The Way Inn hotel.**
- **How to order:** through **The Way Inn reception desk**, **at least one day in
  advance** — **or** simply walk in **when the live open buffet is running**. Frame it
  exactly that way: *"Reserve at reception by the day before — or join us whenever the
  live open buffet is on."*
- **Address:** **Simtat Yud Zayin 23 (סמטת י"ז 23), Safed** — inside The Way Inn, down
  a cobblestone alley in the Artists' Quarter.
- **Branding:** La Buffet is **The Way Inn's** breakfast — present it as
  **"La Buffet · breakfast at The Way Inn"** and harmonize with the hotel's identity
  (the blue **Tree-of-Life mandala** logo seen on the napkins and the courtyard wall).

## THE WAY INN — context (pulled from the web; use for tone + cross-linking)
A boutique suite hotel in a **~250-year-old stone house** down a secluded cobblestone
alley in Safed's **Artists' Quarter**, founded by **Chef Rony BarEl** and his wife
**Genine/Gita**. ~**10 studio & family suites** around sheltered courtyards; decor
inspired by the **sephirot / kabbalistic Tree of Life**, with local artisan work,
vintage furniture, **rooftop sunset patios**, a **Turkish hammam & spa**, and event
space ("**The Womb Room**"). Kitchen: **Mediterranean, vegetarian & fish**, seasonal &
local. Positioning words to echo: *"a place to renew,"* *"a sanctuary to nourish body
and spirit,"* *"not just visiting Tzfat, but inhabiting it."*
- Site: **thewayinn.co.il** · Email: **info@thewayinn.co.il**
- Phones (the hotel's published numbers — **confirm which is the reception line for
  breakfast orders**): **+972-73-7750045**, **+972-4-657-9984**, **+972-52-688-1116**.
- Link the finished page to the hotel site, and ideally add a "Book a room at The Way
  Inn" cross-link.

## POSITIONING / VIBE
Cozy, soulful, abundant. The opposite of a sterile hotel buffet — this is a
**boho-Safed, artisan, home-cooked** breakfast in a stone room full of color, light
and Galilee air. Sensory copy: warm bread, fresh za'atar, the blue table, mountain
light through arched windows.

## SITE STRUCTURE (one elegant page; can scroll into sections)
1. **Hero** — a hero shot (the buffet table or the overhead mezze spread), the name
   **La Buffet · לה בופה**, one-line hook, **"08:00–10:30"**, and a primary CTA:
   **"Reserve at The Way Inn reception"** (+ WhatsApp / call).
2. **The breakfast** — short evocative intro + the "how it works": *order via reception
   ≥1 day ahead, or join the live open buffet.* Show the hours clearly.
3. **What's on the table** — a tasteful, photo-led grid of categories (homemade breads,
   salatim & spreads, cheeses & labneh, eggs/hot dish, fruit, coffee/tea). Describe
   **categories**, not invented exact dishes/prices — mark specifics to confirm.
4. **Gallery** — the best photos, lightbox, lazy-loaded. The mezze-from-above and the
   fresh bread tray are money shots.
5. **The setting** — La Buffet inside The Way Inn: the stone dining room, colorful
   tiles, art, courtyard. Tie to the hotel + Artists' Quarter.
6. **How to reserve** — big, simple: reception desk, **at least one day prior**, or the
   live open buffet. WhatsApp/call buttons. Hours + address + map.
7. **Footer** — The Way Inn link, address, phone, hours, social, copyright.

## DESIGN DIRECTION
Match The Way Inn's world: **warm Safed stone, Tree-of-Life blue/teal, terracotta &
patterned-tile accents, natural wood, soft boho textures**, generous whitespace, big
food photography, beautiful Hebrew + English typography. Premium but warm and edible —
never corporate. Consider a subtle Tree-of-Life mandala motif as a divider/accent.

## ASSETS PRESENT (in this folder — curate, fix, optimize)
A mix of phone photos, screenshots and videos. **Handle them, don't dump them:**
- **Dedupe** the `(1)` copies: `IMG_8369(1).PNG`, `IMG_8370(1).PNG`, `IMG_8390(1).PNG`
  are byte-identical to their non-`(1)` versions — keep one each.
- **Phone-captured portraits / screenshots (the large 8–12 MB PNGs):** **crop off any
  phone UI / frame at the bottom** (status bar, home indicator, share tray) — and the
  top bar if present — so only the food/scene remains. This was explicitly requested.
- **Fix EXIF rotation:** some are sideways/upside-down (e.g. `SIDESOLO.jpg` displays
  rotated 90°). Auto-orient every image before use.
- **Convert HEIC → JPG/WebP** (`IMG_7281.HEIC`, `IMG_7600.HEIC`, `SIDEBUFFET2.HEIC`) —
  browsers don't render HEIC.
- **Optimize** the huge PNGs/JPGs down to web sizes; serve WebP/AVIF with fallbacks;
  lazy-load the gallery.
- **Videos** (`IMG_6348.MOV`, `IMG_6603.MOV`, `ScreenRecording_…06-08-2026….mp4`): pick
  the best one as an optional muted autoplay loop in the hero (transcode to mp4+webm,
  compress hard); otherwise leave out. Don't ship a 60–70 MB raw .MOV.
- **Curate & rename** semantically, e.g. `hero-buffet.jpg`, `mezze-overhead.jpg`,
  `homemade-bread.jpg`, `dining-room.jpg`, `salatim-table.jpg`, `courtyard-night.jpg`.
- Named files already meaningful: `HOMMADE BAKE.jpg` (fresh bread tray), `SIDEBUFFET*`
  / `INTERIOR.JPG` (the stone dining room + open buffet), `UP SOLO` / `SIDEQUATRO` /
  `SIDESOLO` (overhead mezze tables, "The Way Inn" napkins visible), `IMG_8400.JPG`
  (the lit courtyard with the Tree-of-Life wall plaque — great for "the setting").
- Move raw originals into a `raw/` (or `_src/`) subfolder; build optimized assets into
  `img/`. Ask the owner for more if useful (golden-hour rooftop, coffee, each dish).

## TECH & RULES
- **Static site** (HTML/CSS/vanilla JS, no build step) — but make it excellent and fast.
- **Hebrew-first (RTL)** primary **+ full English** parity (the hotel hosts many
  international guests). Language switcher; keep CTAs identical.
- **Mobile-first & truly responsive** — most guests are on phones in their room. Test
  **360–390px**, 768px, desktop. Header/nav must never overflow; CTAs thumb-reachable.
- **Ordering CTAs everywhere**, sticky on mobile: "Reserve at reception" + WhatsApp +
  `tel:` to the confirmed hotel number. Pre-fill a friendly bilingual WhatsApp message
  ("Hi, we'd like to reserve La Buffet breakfast for [date], [number of guests]").
- **SEO:** title/description/OpenGraph; Hebrew keywords (ארוחת בוקר בצפת, מלון The Way
  Inn, לה בופה, בופה ארוחת בוקר צפת) + English ("breakfast in Safed", "The Way Inn
  breakfast", "Tzfat boutique hotel breakfast"). Add **`Restaurant`/`FoodEstablishment`
  + `Breakfast` JSON-LD** with `servesCuisine`, `openingHours` (08:00–10:30), address
  Simtat Yud Zayin 23 Safed, and the confirmed phone.
- **Accuracy / integrity:** do **NOT** invent menu items, prices, kashrut, days, or
  capacity. Describe what the photos clearly show; mark anything uncertain "to confirm."
  No fake reviews. Accurate contact only.

## ASK / CONFIRM before publishing (leave clear TODO placeholders meanwhile)
- Exact **days** La Buffet runs; is it **every** morning or specific days?
- **Price** per guest (and whether it's included in some room rates).
- **Kashrut**: is it kosher / dairy-vegetarian-and-fish (no meat)? Certification?
- The **reception phone line** to use for breakfast orders (of the three above).
- Is breakfast **hotel-guests only**, or can outside visitors reserve too?
- The real **menu** (so we can name dishes instead of generic categories).
- WhatsApp number for reservations; any Instagram/Facebook to link
  (The Way Inn: @thewayinn1 on Instagram, facebook.com/WayInnIsrael).

## FIRST STEPS FOR THIS SESSION
1. Inventory + fix the media: dedupe, auto-orient (EXIF), crop phone frames, convert
   HEIC, optimize, pick the hero. Move originals to `raw/`, build into `img/`.
2. Build `index.html` (Hebrew RTL, mobile-first) with the sections above + sticky
   order CTAs, gallery+lightbox, map, JSON-LD, OG tags.
3. Add the English version (`/en/`) at full parity.
4. Verify on mobile (360/390px) and desktop; no overflow; CTAs reachable; images sharp.
5. Commit, then create the GitHub repo and deploy:
   `gh repo create labuffet --public --source=. --remote=origin --push`
   then enable GitHub Pages (it'll live at `https://wattsonworks.github.io/labuffet/`).

Make it the most appetizing breakfast page in the Galilee. Let's go.
