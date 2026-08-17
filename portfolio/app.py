from pathlib import Path
import os
import textwrap

import streamlit as st
from dotenv import load_dotenv

from data.profile import PROFILE, STATS
from data.projects import PROJECTS
from data.experience import EXPERIENCE
from data.certificates import CERTIFICATES
from components.background import render_background, render_loader
from components.navbar import render_navbar
from components.hero import render_hero
from components.about import render_about
from components.skills import render_skills
from components.projects import render_projects
from components.certificates import render_certificates
from components.timeline import render_timeline
from components.analytics import render_analytics
from components.services import render_services
from components.resume import render_resume
from components.contact import render_contact
from components.footer import render_footer

BASE_DIR = Path(__file__).resolve().parent
os.chdir(BASE_DIR)
load_dotenv(BASE_DIR / ".env")

st.set_page_config(
    page_title="Shiv Shankar Tiwari | Data Analyst & AI/ML",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

_original_markdown = st.markdown

def _portfolio_markdown(body="", *args, **kwargs):
    if isinstance(body, str):
        body = textwrap.dedent(body).strip("\n")
    return _original_markdown(body, *args, **kwargs)

st.markdown = _portfolio_markdown

for stylesheet in ("styles/main.css", "styles/projects.css", "styles/immersive.css", "styles/sidebar.css", "styles/section-motion.css", "styles/section-backgrounds.css", "styles/skills-cinematic.css", "styles/about-cinematic.css", "styles/certificates-cinematic.css"):
    css_path = BASE_DIR / stylesheet
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

render_background()
render_loader()
render_navbar()
render_hero(PROFILE)
render_about(PROFILE, STATS)
render_skills()
render_projects(PROJECTS)
render_timeline(EXPERIENCE)
render_certificates(CERTIFICATES)
render_analytics()
render_services()
render_resume()
render_contact(PROFILE)
render_footer(PROFILE)

st.components.v1.html(
    """
    <script>
    (() => {
      const parentWindow = window.parent;
      const doc = parentWindow.document;
      const animatedSectionIds = ['about','skills','projects','experience','certificates','analytics','services','contact'];

      const initSectionBackgrounds = () => {
        animatedSectionIds.forEach(id => {
          const section = doc.getElementById(id);
          if (section) section.classList.add('animated-section');
        });
      };

      const initMobileNavigation = () => {
        const menuButton = doc.querySelector('.mobile-menu-btn');
        const drawer = doc.querySelector('.mobile-drawer');
        const backdrop = doc.querySelector('.mobile-nav-backdrop');
        if (!menuButton || !drawer || !backdrop) return false;
        const closeButton = drawer.querySelector('.mobile-drawer-head button');
        const links = drawer.querySelectorAll('a');
        const closeMenu = () => {
          doc.body.classList.remove('mobile-nav-open');
          menuButton.setAttribute('aria-expanded', 'false');
        };
        const toggleMenu = (event) => {
          if (event) event.preventDefault();
          const open = !doc.body.classList.contains('mobile-nav-open');
          doc.body.classList.toggle('mobile-nav-open', open);
          menuButton.setAttribute('aria-expanded', String(open));
        };
        if (menuButton.dataset.mobileNavReady !== 'true') {
          menuButton.addEventListener('click', toggleMenu, {passive:false});
          menuButton.addEventListener('touchend', toggleMenu, {passive:false});
          menuButton.dataset.mobileNavReady = 'true';
        }
        if (backdrop.dataset.mobileNavReady !== 'true') {
          backdrop.addEventListener('click', closeMenu);
          backdrop.addEventListener('touchend', closeMenu, {passive:true});
          backdrop.dataset.mobileNavReady = 'true';
        }
        if (closeButton && closeButton.dataset.mobileNavReady !== 'true') {
          closeButton.addEventListener('click', closeMenu);
          closeButton.addEventListener('touchend', closeMenu, {passive:true});
          closeButton.dataset.mobileNavReady = 'true';
        }
        links.forEach(link => {
          if (link.dataset.mobileNavReady === 'true') return;
          link.addEventListener('click', closeMenu);
          link.addEventListener('touchend', closeMenu, {passive:true});
          link.dataset.mobileNavReady = 'true';
        });
        menuButton.setAttribute('aria-expanded', doc.body.classList.contains('mobile-nav-open') ? 'true' : 'false');
        return true;
      };

      const reveal = () => doc.querySelectorAll('.reveal').forEach(el => {
        const r = el.getBoundingClientRect();
        if (r.top < parentWindow.innerHeight * .90) el.classList.add('reveal-visible');
      });
      const updateActive = () => {
        const ids = ['home','about','skills','projects','experience','certificates','analytics','services','contact'];
        let active = 'home';
        ids.forEach(id => {
          const el = doc.getElementById(id);
          if (el && el.getBoundingClientRect().top <= parentWindow.innerHeight * .35) active = id;
        });
        doc.querySelectorAll('.side-link').forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + active));
      };
      const onScroll = () => { initSectionBackgrounds(); reveal(); updateActive(); };
      parentWindow.addEventListener('scroll', onScroll, {passive:true});
      let attempts = 0;
      const boot = () => {
        initSectionBackgrounds();
        if (initMobileNavigation() || attempts >= 20) return;
        attempts += 1;
        parentWindow.setTimeout(boot, 150);
      };
      boot();
      parentWindow.setTimeout(onScroll, 250);
      if ('IntersectionObserver' in parentWindow) {
        const observer = new parentWindow.IntersectionObserver((entries) => {
          entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('reveal-visible'); });
        }, {threshold:.10});
        doc.querySelectorAll('.reveal').forEach(el => observer.observe(el));
      }
    })();
    </script>
    """,
    height=0,
)

if not os.getenv("GITHUB_TOKEN"):
    pass
