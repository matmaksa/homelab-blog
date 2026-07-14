/* ============================================================
   Homelab Guide – Main JavaScript
   Theme-Toggle, Mobile-Menü, Code-Copy, Scroll-to-Top
   ============================================================ */

(function() {
  'use strict';

  /* --- Theme Toggle --- */
  (function themeToggle() {
    const toggle = document.getElementById('theme-toggle');
    const html = document.documentElement;

    if (!toggle) return;

    // Init theme from localStorage
    const stored = localStorage.getItem('pref-theme');
    if (stored) {
      html.dataset.theme = stored;
    }

    toggle.addEventListener('click', function() {
      const isDark = html.dataset.theme === 'dark';
      const newTheme = isDark ? 'light' : 'dark';
      html.dataset.theme = newTheme;
      localStorage.setItem('pref-theme', newTheme);
    });
  })();

  /* --- Mobile Menu --- */
  (function mobileMenu() {
    const openBtn = document.getElementById('hamburger-btn');
    const closeBtn = document.getElementById('mobile-menu-close');
    const overlay = document.getElementById('mobile-overlay');
    const menu = document.getElementById('mobile-menu');

    if (!openBtn || !closeBtn || !overlay || !menu) return;

    function openMenu() {
      menu.classList.add('open');
      overlay.classList.add('open');
      document.body.style.overflow = 'hidden';
      closeBtn.focus();
    }

    function closeMenu() {
      menu.classList.remove('open');
      overlay.classList.remove('open');
      document.body.style.overflow = '';
      openBtn.focus();
    }

    openBtn.addEventListener('click', openMenu);
    closeBtn.addEventListener('click', closeMenu);
    overlay.addEventListener('click', closeMenu);

    // Escape key
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && menu.classList.contains('open')) {
        closeMenu();
      }
    });

    // Close on resize to desktop
    window.addEventListener('resize', function() {
      if (window.innerWidth >= 1024 && menu.classList.contains('open')) {
        closeMenu();
      }
    });
  })();

  /* --- Scroll-to-Top Button --- */
  (function scrollToTop() {
    const link = document.getElementById('top-link');
    if (!link) return;

    window.addEventListener('scroll', function() {
      const threshold = window.innerHeight * 0.5;
      if (document.documentElement.scrollTop > threshold || document.body.scrollTop > threshold) {
        link.classList.add('visible');
      } else {
        link.classList.remove('visible');
      }
    });

    // Smooth scroll
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      window.scrollTo({
        top: 0,
        behavior: prefersReduced ? 'auto' : 'smooth'
      });
    });
  })();

  /* --- Code Copy Buttons --- */
  (function codeCopy() {
    const codeBlocks = document.querySelectorAll('.post-content pre > code');
    if (!codeBlocks.length) return;

    codeBlocks.forEach(function(codeblock) {
      const pre = codeblock.parentElement;
      const container = pre.parentElement;

      const btn = document.createElement('button');
      btn.className = 'copy-code';
      btn.textContent = 'Kopieren';
      btn.setAttribute('aria-label', 'Code in Zwischenablage kopieren');

      function copyDone() {
        btn.textContent = 'Kopiert!';
        setTimeout(function() {
          btn.textContent = 'Kopieren';
        }, 2000);
      }

      btn.addEventListener('click', function() {
        const code = codeblock.textContent || '';
        if (navigator.clipboard) {
          navigator.clipboard.writeText(code).then(copyDone).catch(function() {});
        } else {
          // Fallback for older browsers
          try {
            const range = document.createRange();
            range.selectNodeContents(codeblock);
            const selection = window.getSelection();
            selection.removeAllRanges();
            selection.addRange(range);
            document.execCommand('copy');
            selection.removeRange(range);
            copyDone();
          } catch(e) {}
        }
      });

      // Insert button inside the pre element
      pre.style.position = 'relative';
      pre.appendChild(btn);
    });
  })();

  /* --- Smooth Anchor Scrolling (for TOC) --- */
  (function anchorScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
      anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href === '#') return;

        e.preventDefault();
        const target = document.querySelector('[id="' + decodeURIComponent(href.substring(1)) + '"]');
        if (!target) return;

        const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        target.scrollIntoView({
          behavior: prefersReduced ? 'auto' : 'smooth',
          block: 'start'
        });

        // Update URL without jumping
        history.pushState(null, null, href);
      });
    });
  })();

})();
