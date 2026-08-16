import html
import streamlit as st
from .common import section_heading


SERVICES = [
    ("⌁", "Data Analytics", "Turn raw datasets into useful insights and decisions."),
    ("✦", "AI / ML", "Prototype intelligent workflows and practical ML solutions."),
    ("◈", "BI & Reporting", "Design clear dashboards and reporting experiences."),
    ("◌", "Visualization", "Make complex patterns understandable through visuals."),
    ("⚡", "Automation", "Reduce repetitive work with Python and intelligent workflows."),
]


def render_services():
    st.markdown('<section id="services">', unsafe_allow_html=True)
    section_heading("07 / WHAT I DO", "From question to <span class='accent'>impact</span>.",
                   "Services and strengths that sit at the intersection of data, technology and business.")
    cards = []
    for icon, title, desc in SERVICES:
        cards.append(
            f'<div class="glass-card service-card reveal"><div class="service-icon">{html.escape(icon)}</div><h4>{html.escape(title)}</h4><p>{html.escape(desc)}</p></div>'
        )
    st.markdown(f'<div class="services-grid">{"".join(cards)}</div></section>', unsafe_allow_html=True)
