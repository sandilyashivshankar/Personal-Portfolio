import html
import streamlit as st
from .common import section_heading


SKILLS = {
    "Programming": ["Python"],
    "Data Analytics": ["Pandas", "NumPy", "Matplotlib", "Seaborn", "EDA", "Data Cleaning"],
    "AI / Machine Learning": ["Machine Learning", "Scikit-learn", "TensorFlow", "AI"],
    "Generative AI & LLM": ["GenAI", "LLM", "RAG", "AI Agents", "Prompt Engineering"],
    "Databases": ["PostgreSQL", "MySQL"],
    "Visualization": ["Power BI", "Plotly", "Matplotlib"],
    "Tools": ["Git", "GitHub", "Streamlit", "Jupyter Notebook"],
}


def render_skills():
    st.markdown('<section id="skills">', unsafe_allow_html=True)
    section_heading(
        "02 / TOOLKIT",
        "Skills that <span class='accent'>ship</span>.",
        "A practical stack for analytics, intelligent applications, generative AI and data storytelling."
    )
    cards = []
    for category, skills in SKILLS.items():
        pills = "".join(
            f'<span class="skill-pill">{html.escape(skill)}</span>' for skill in skills
        )
        cards.append(
            f'<div class="glass-card skill-category-card reveal"><div class="skill-category-title">✦ {html.escape(category)}</div><div class="skill-pill-list">{pills}</div></div>'
        )
    st.markdown(f'<div class="skills-grid">{"".join(cards)}</div>', unsafe_allow_html=True)
    st.markdown("</section>", unsafe_allow_html=True)
