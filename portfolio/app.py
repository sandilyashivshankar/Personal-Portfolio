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
from components.github import render_github
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

# Streamlit's Markdown parser can interpret deeply-indented multiline HTML as a
# Markdown code block. Normalize component templates before every markdown render.
_original_markdown = st.markdown

def _portfolio_markdown(body="", *args, **kwargs):
    if isinstance(body, str):
        body = textwrap.dedent(body).strip("\n")
    return _original_markdown(body, *args, **kwargs)

st.markdown = _portfolio_markdown

css_path = BASE_DIR / "styles" / "main.css"
st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

render_background()
render_loader()
render_navbar()

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

# Client-side enhancements are optional; the portfolio remains usable without JS.
st.components.v1.html(
    """
    <script>
    (() => {
      const parent = window.parent;
      const doc = parent.document;
      const html = doc.documentElement;
      html.classList.add("portfolio-js-ready");

      const reveal = () => {
        doc.querySelectorAll(".reveal").forEach(el => {
          const r = el.getBoundingClientRect();
          if (r.top < parent.innerHeight * .90) el.classList.add("reveal-visible");
        });
      };

      const onScroll = () => {
        const nav = doc.querySelector(".glass-navbar");
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

# Never display or commit secret values.
if not os.getenv("GITHUB_TOKEN"):
    pass
