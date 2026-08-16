from pathlib import Path
import os

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
from components.github import render_github
from components.certificates import render_certificates
from components.timeline import render_timeline
from components.analytics import render_analytics
from components.services import render_services
from components.resume import render_resume
from components.contact import render_contact
from components.footer import render_footer

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

st.set_page_config(
    page_title="Shiv Shankar Tiwari | Data Analyst & AI/ML",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Load CSS once per Streamlit run.
css_path = BASE_DIR / "styles" / "main.css"
st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

# Background + chrome
render_background()
render_loader()
render_navbar()

# Main experience
render_hero(PROFILE)
render_about(PROFILE, STATS)
render_skills()
render_projects(PROJECTS)
render_github(PROFILE)
render_timeline(EXPERIENCE)
render_certificates(CERTIFICATES)
render_analytics()
render_services()
render_resume()
render_contact(PROFILE)
render_footer(PROFILE)

# Tiny client-side enhancement for navbar state / reveal effects.
# Kept isolated and non-essential: if the browser blocks it, CSS remains usable.
st.components.v1.html(
    """
    <script>
    (() => {
      const parent = window.parent;
      const doc = parent.document;
      const html = doc.documentElement;
      html.classList.add("portfolio-js-ready");

      const nav = doc.querySelector(".glass-navbar");
      const reveal = () => {
        doc.querySelectorAll(".reveal").forEach(el => {
          const r = el.getBoundingClientRect();
          if (r.top < parent.innerHeight * .90) el.classList.add("reveal-visible");
        });
      };

      const onScroll = () => {
        if (nav) nav.classList.toggle("scrolled", parent.scrollY > 24);
        reveal();
      };

      parent.addEventListener("scroll", onScroll, {passive:true});
      setTimeout(onScroll, 250);

      if ("IntersectionObserver" in parent) {
        const observer = new parent.IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) entry.target.classList.add("reveal-visible");
          });
        }, {threshold:.10});
        doc.querySelectorAll(".reveal").forEach(el => observer.observe(el));
      }
    })();
    </script>
    """,
    height=0,
)

# Optional deployment check: never display secret values.
if not os.getenv("GITHUB_TOKEN"):
    pass
