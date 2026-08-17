import html

import streamlit as st

from .common import section_heading, tech_badges


def _safe_url(value: str) -> str:
    return html.escape(value or "", quote=True)


def _project_visual(project: dict) -> str:
    image = project.get("image", "")
    if image:
        return (
            f'<div class="project-card-media project-visual" style="background-image:'
            f'linear-gradient(135deg, rgba(5,6,10,.16), rgba(5,6,10,.78)), url(\'{_safe_url(image)}\')">'
            f'<div class="project-visual-overlay"><span class="project-live-dot"></span>'
            f'<span>{html.escape(project.get("type", "Project"))}</span></div>'
            f'</div>'
        )
    return '<div class="project-card-media project-visual project-visual-fallback"><span>✦</span></div>'


def project_card(project):
    features = "".join(f"<li>{html.escape(x)}</li>" for x in project["features"])
    demo = project.get("demo", "")
    links_html = (
        f'<a class="link-btn" href="{_safe_url(demo)}" target="_blank" rel="noreferrer">Live Demo ↗</a>'
        if demo else ""
    )
    category = html.escape(project.get("category", "All"))
    return f"""
<div class="glass-card project-card reveal" data-category="{category}">
  {_project_visual(project)}
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
    section_heading(
        "",
        "Projects with <span class='accent'>purpose</span>.",
        "Seven highlighted builds across Generative AI, RAG, agentic systems, machine learning and business intelligence."
    )

    categories = ["All", "AI/ML", "Data Analytics"]
    pills = "".join(
        f'<button class="filter-pill {"active" if i == 0 else ""}" onclick="window.__filterProjects(\'{html.escape(c)}\', this)">{html.escape(c)}</button>'
        for i, c in enumerate(categories)
    )
    st.markdown(f'<div class="project-filter">{pills}</div>', unsafe_allow_html=True)

    # Every project uses the same card structure and visual hierarchy.
    cards = "".join(project_card(project) for project in projects)
    st.markdown(f'<div class="project-grid">{cards}</div>', unsafe_allow_html=True)

    st.components.v1.html(
        """
<script>
(() => {
  const doc = window.parent.document;
  window.parent.__filterProjects = (category, button) => {
    doc.querySelectorAll('.project-filter .filter-pill').forEach(b => b.classList.remove('active'));
    if (button) button.classList.add('active');
    doc.querySelectorAll('.project-card').forEach(card => {
      const match = category === 'All' || card.dataset.category === category;
      card.style.display = match ? '' : 'none';
    });
  };
})();
</script>
""",
        height=0,
    )
    st.markdown("</section>", unsafe_allow_html=True)
