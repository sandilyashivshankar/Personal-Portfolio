import html
import streamlit as st
from .common import section_heading, tech_badges


def render_timeline(experience):
    st.markdown('<section id="experience">', unsafe_allow_html=True)
    section_heading("05 / JOURNEY", "Experience & <span class='accent'>education</span>.",
                   "A compact timeline of learning, work and progression.")
    items = []
    for item in experience:
        bullets = "".join(f"<li>{html.escape(x)}</li>" for x in item["points"])
        items.append(
            f"""
            <div class="timeline-item reveal">
              <div class="timeline-node"></div>
              <div class="glass-card timeline-card">
                <div class="duration">{html.escape(item["duration"])}</div>
                <h4>{html.escape(item["role"])}</h4>
                <div class="subtitle">{html.escape(item["company"])}</div>
                <ul>{bullets}</ul>
                <div class="tech-badges">{tech_badges(item["tech"])}</div>
              </div>
            </div>
            """
        )
    st.markdown(f'<div class="timeline">{"".join(items)}</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="timeline" style="margin-top:2rem">
          <div class="timeline-item reveal">
            <div class="timeline-node"></div>
            <div class="glass-card timeline-card">
              <div class="duration">2026</div>
              <h4>B.Tech — Computer Science Engineering</h4>
              <div class="subtitle">Data Science & Artificial Intelligence · SRMU Lucknow</div>
              <ul><li>Focused academic direction toward data, AI/ML and practical software projects.</li></ul>
              <div class="tech-badges"><span class="tech-badge">Data Science</span><span class="tech-badge">AI / ML</span><span class="tech-badge">Python</span></div>
            </div>
          </div>
        </div>
        </section>
        """,
        unsafe_allow_html=True,
    )
