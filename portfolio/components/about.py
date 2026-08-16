import html
import streamlit as st
from .common import section_heading


def render_about(profile, stats):
    st.markdown('<section id="about">', unsafe_allow_html=True)
    section_heading(
        "",
        "Turning <span class='accent'>data</span> into direction.",
        "A concise look at the person behind the projects."
    )

    roles = "".join(
        f'<span class="role-chip">{html.escape(role)}</span>'
        for role in profile.get("roles", [])
    )

    st.markdown(
        f"""
<div class="about-identity reveal">
  <div class="about-role-line">{roles}</div>
  <div class="availability about-availability"><span class="pulse"></span> Open to data &amp; AI opportunities</div>
</div>
<div class="stats-grid">
  {''.join(f'<div class="glass-card stat-card reveal"><div class="stat-icon">{i}</div><div class="stat-number">{html.escape(v)}</div><div class="stat-label">{html.escape(l)}</div></div>' for i,v,l in stats)}
</div>
<div class="about-grid">
  <div class="about-text reveal">
    <p>{html.escape(profile["about"])}</p>
    <p>My approach is simple: understand the problem, explore the data, communicate the story clearly, and build a solution that people can actually use.</p>
  </div>
  <div class="glass-card building-card reveal reveal-delay-2">
    <h4>Currently building around</h4>
    <div class="building-tags">
      {''.join(f'<span class="tag-chip">{html.escape(x)}</span>' for x in ["Data Analytics","Data Science","AI / ML","Python","Business Intelligence","Automation","Prompt Engineering"])}
    </div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )
    st.markdown("</section>", unsafe_allow_html=True)
