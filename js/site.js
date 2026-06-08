/* La Buffet · site interactions */
(() => {
  'use strict';

  /* ---- Year stamp ---- */
  document.querySelectorAll('[data-year]').forEach(el => {
    el.textContent = new Date().getFullYear();
  });

  /* ---- Sticky header on scroll ---- */
  const header = document.querySelector('[data-header]');
  if (header) {
    const onScroll = () => header.classList.toggle('is-scrolled', window.scrollY > 40);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---- Hero video: lazy attach + autoplay when in view ---- */
  const video = document.querySelector('[data-hero-video]');
  if (video && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const start = () => {
      if (video.dataset.loaded) return;
      video.querySelectorAll('source[data-src]').forEach(s => {
        s.src = s.dataset.src;
        s.removeAttribute('data-src');
      });
      video.load();
      const play = () => {
        const p = video.play();
        if (p && p.then) p.then(() => video.classList.add('is-playing')).catch(() => {});
      };
      if (video.readyState >= 2) play();
      else video.addEventListener('loadeddata', play, { once: true });
      video.dataset.loaded = '1';
    };
    if (navigator.connection && navigator.connection.saveData) {
      /* respect data saver: skip the loop */
    } else {
      // Defer until idle + visible
      const kick = () => {
        const io = new IntersectionObserver(entries => {
          entries.forEach(e => { if (e.isIntersecting) { start(); io.disconnect(); } });
        }, { threshold: 0.1 });
        io.observe(video);
      };
      if ('requestIdleCallback' in window) requestIdleCallback(kick, { timeout: 1500 });
      else setTimeout(kick, 800);
    }
  }

  /* ---- Smooth in-page nav (account for fixed header) ---- */
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', (ev) => {
      const id = a.getAttribute('href').slice(1);
      if (!id) return;
      const target = document.getElementById(id);
      if (!target) return;
      ev.preventDefault();
      const top = target.getBoundingClientRect().top + window.scrollY - 70;
      window.scrollTo({ top, behavior: 'smooth' });
      history.pushState(null, '', '#' + id);
    });
  });

  /* ---- Gallery lightbox ---- */
  const gallery = document.querySelector('[data-gallery]');
  const lb = document.querySelector('[data-lightbox]');
  if (gallery && lb) {
    const items = Array.from(gallery.querySelectorAll('.g-item'));
    const lbImg = lb.querySelector('[data-lb-img]');
    const lbCap = lb.querySelector('[data-lb-cap]');
    const btnClose = lb.querySelector('[data-lb-close]');
    const btnPrev = lb.querySelector('[data-lb-prev]');
    const btnNext = lb.querySelector('[data-lb-next]');
    let idx = 0;
    let lastFocus = null;

    const show = (i) => {
      idx = (i + items.length) % items.length;
      const el = items[idx];
      lbImg.src = el.getAttribute('href');
      lbImg.alt = el.querySelector('img')?.alt || '';
      lbCap.textContent = el.dataset.cap || '';
    };

    const open = (i) => {
      lastFocus = document.activeElement;
      lb.hidden = false;
      // next frame for transition
      requestAnimationFrame(() => lb.setAttribute('data-open', ''));
      show(i);
      document.body.style.overflow = 'hidden';
      btnClose.focus();
      document.addEventListener('keydown', onKey);
    };
    const close = () => {
      lb.removeAttribute('data-open');
      document.removeEventListener('keydown', onKey);
      document.body.style.overflow = '';
      setTimeout(() => { lb.hidden = true; lbImg.src = ''; }, 200);
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    };
    const onKey = (e) => {
      if (e.key === 'Escape') close();
      else if (e.key === 'ArrowLeft')  show(document.dir === 'rtl' ? idx + 1 : idx - 1);
      else if (e.key === 'ArrowRight') show(document.dir === 'rtl' ? idx - 1 : idx + 1);
    };

    items.forEach((el, i) => {
      el.addEventListener('click', (ev) => { ev.preventDefault(); open(i); });
    });
    btnClose.addEventListener('click', close);
    btnPrev .addEventListener('click', () => show(document.dir === 'rtl' ? idx + 1 : idx - 1));
    btnNext .addEventListener('click', () => show(document.dir === 'rtl' ? idx - 1 : idx + 1));
    lb.addEventListener('click', (e) => { if (e.target === lb) close(); });
  }
})();
