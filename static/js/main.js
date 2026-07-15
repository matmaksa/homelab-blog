/* ============================================================
   Homelab Guide – Main JavaScript
   Theme-Toggle, Mobile-Menü, Search-Overlay, Code-Copy, Scroll-to-Top
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

  /* --- Search Overlay (wie raspberry.tips) --- */
  (function searchOverlay() {
    const toggle = document.getElementById('search-toggle');
    const overlay = document.getElementById('search-overlay');
    const backdrop = document.getElementById('search-overlay-backdrop');
    const closeBtn = document.getElementById('search-overlay-close');
    const input = document.getElementById('search-input');

    if (!toggle || !overlay || !backdrop || !closeBtn || !input) return;

    function openSearch() {
      overlay.classList.add('open');
      backdrop.classList.add('open');
      overlay.setAttribute('aria-hidden', 'false');
      backdrop.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      // Focus the input after a brief delay for the transition
      setTimeout(function() { input.focus(); }, 100);
    }

    function closeSearch() {
      overlay.classList.remove('open');
      backdrop.classList.remove('open');
      overlay.setAttribute('aria-hidden', 'true');
      backdrop.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
      toggle.focus();
    }

    toggle.addEventListener('click', openSearch);
    closeBtn.addEventListener('click', closeSearch);
    backdrop.addEventListener('click', closeSearch);

    // Escape key
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && overlay.classList.contains('open')) {
        closeSearch();
      }
    });

    // Close on resize from mobile to desktop
    window.addEventListener('resize', function() {
      if (overlay.classList.contains('open') && window.innerWidth >= 1024) {
        // Keep open on desktop too – user might want search
      }
    });

    // Keyboard shortcut: "/" opens search
    document.addEventListener('keydown', function(e) {
      // Don't trigger if user is typing in an input/textarea
      if (e.key === '/' && !e.ctrlKey && !e.metaKey) {
        const tag = document.activeElement ? document.activeElement.tagName : '';
        if (tag !== 'INPUT' && tag !== 'TEXTAREA' && tag !== 'SELECT') {
          e.preventDefault();
          openSearch();
        }
      }
    });

    // Submit form on Enter
    input.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' && input.value.trim()) {
        // Let the native form submission handle the redirect
        return;
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

  /* --- Mega-Menu: Close on Escape (Desktop) --- */
  (function megaMenuKeyboard() {
    const megaItems = document.querySelectorAll('.has-mega-dropdown');
    megaItems.forEach(function(item) {
      const link = item.querySelector('a');
      const dropdown = item.querySelector('.mega-dropdown');

      if (!link || !dropdown) return;

      item.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
          // Close the dropdown, focus back to the nav link
          // CSS hover handles visibility, so we just need to move focus
          link.focus();
        }
      });

      // Close mega-menu when focus leaves the entire dropdown area
      dropdown.addEventListener('focusout', function(e) {
        // If the newly focused element is outside the mega-dropdown item
        setTimeout(function() {
          if (!item.contains(document.activeElement)) {
            // Do nothing special – CSS handles the hide on non-hover
          }
        }, 0);
      });
    });
  })();

})();
