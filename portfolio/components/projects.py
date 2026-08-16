import html
import streamlit as st
from .common import section_heading, tech_badges


def project_card(project):
    features = "".join(f"<li>{html.escape(x)}</li>" for x in project["features"])
    links = []
    if project.get("github"):
        links.append(f'<a class="link-btn primary" href="{html.escape(project["github"])}" target="_blank" rel="noreferrer">GitHub ↗</a>')
    if project.get("demo"):
        links.append(f'<a class="link-btn" href="{html.escape(project["demo"])}" target="_blank" rel="noreferrer">Live Demo ↗</a>')
    links_html = "".join(links) or '<span class="link-btn" style="opacity:.55">Demo coming soon</span>'
    return f"""
    <div class="glass-card project-card reveal">
      <div class="project-card-media"><span>✦</span></div>
      <div class="project-card-body">
        <span class="project-type">{html.escape(project["type"])}</span>
        <h4>{html.escape(project["title"])}</h4>
        <p>{html.escape(project["description"])}</p>
        <ul class="feature-list">{features}</ul>
        <div class="tech-badges">{tech_badges(project["tech"])}</div>
        <div class="project-card-links">{links_html}</div>
      </div>
    </div>
    """


def render_projects(projects):
    st.markdown('<section id="projects">', unsafe_allow_html=True)
    section_heading("03 / SELECTED WORK", "Projects with <span class='accent'>purpose</span>.",
                   "A few builds that demonstrate analytical thinking, AI experimentation and product-minded execution.")

    featured = next((p for p in projects if p.get("featured")), projects[0])
    feature_list = "".join(f"<li>{html.escape(x)}</li>" for x in featured["features"])
    st.markdown(
        f"""
        <div class="featured-project reveal">
          <span class="featured-badge">★ Featured project</span>
          <h3>{html.escape(featured["title"])}</h3>
          <p class="desc">{html.escape(featured["description"])}</p>
          <div class="featured-grid">
            <div>
              <div class="tech-badges">{tech_badges(featured["tech"])}</div>
              <div class="hero-ctas" style="justify-content:flex-start;margin:1.2rem 0 0;">
                <a class="btn btn-primary" href="{html.escape(featured["github"])}" target="_blank" rel="noreferrer">View Repository ↗</a>
              </div>
            </div>
            <ul class="feature-list">{feature_list}</ul>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="project-grid">', unsafe_allow_html=True)
    for project in projects:
        if project is not featured:
            st.markdown(project_card(project), unsafe_allow_html=True)
    st.markdown("</div></section>", unsafe_allow_html=True)
