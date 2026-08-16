import html
import streamlit as st
from .common import section_heading


def render_about(profile, stats):
    st.markdown('<section id="about">', unsafe_allow_html=True)
    section_heading(
        "",
        "Turning <span class='accent'>data</span> into direction.",
        "I combine analytical thinking, data storytelling and practical AI to turn complex information into clear decisions and useful digital solutions."
    )

    roles = "".join(
        f'<span class="role-chip">{html.escape(role)}</span>'
        for role in profile.get("roles", [])
    )

    st.markdown(
        f"""
<style>
.about-identity {{ display:flex; flex-wrap:wrap; align-items:center; gap:.75rem 1rem; margin:-.5rem 0 2rem; }}
.about-role-line {{ display:flex; flex-wrap:wrap; gap:.55rem; }}
.role-chip {{ display:inline-flex; align-items:center; padding:.5rem .85rem; border:1px solid rgba(34,211,238,.22); border-radius:999px; background:linear-gradient(135deg,rgba(34,211,238,.08),rgba(139,92,246,.10)); color:var(--text-1); font-size:.86rem; font-weight:650; box-shadow:0 8px 28px rgba(34,211,238,.06); transition:transform .25s ease,border-color .25s ease,box-shadow .25s ease; }}
.role-chip:hover {{ transform:translateY(-2px); border-color:rgba(34,211,238,.5); box-shadow:0 10px 30px rgba(139,92,246,.16); }}
.about-lead {{ max-width:900px; margin:0 0 1rem; color:var(--text-1); font-size:1.08rem; line-height:1.8; }}
.about-lead.secondary {{ color:var(--text-2); font-size:1rem; }}
.about-lead strong {{ color:var(--text-0); }}
.about-intro {{ margin-bottom:2.4rem; }}
</style>
<div class="about-intro reveal">
  <div class="about-identity">
    <div class="about-role-line">{roles}</div>
  </div>
  <p class="about-lead"><strong>I turn data into insights, insights into decisions, and ideas into practical AI solutions.</strong> I enjoy working where technology, analytics and real-world business problems meet.</p>
  <p class="about-lead secondary">My work spans <strong>Data Analytics, Data Science, Artificial Intelligence, Machine Learning and Business Intelligence</strong>. I build dashboards, predictive models, intelligent assistants, RAG systems and automation workflows with a focus on clarity, usefulness and measurable impact.</p>
</div>
<div class="stats-grid">
  {''.join(f'<div class="glass-card stat-card reveal"><div class="stat-icon">{i}</div><div class="stat-number">{html.escape(v)}</div><div class="stat-label">{html.escape(l)}</div></div>' for i,v,l in stats)}
</div>
<div class="about-grid">
  <div class="about-text reveal">
    <h3>How I approach problems</h3>
    <p>{html.escape(profile["about"])}</p>
    <p>Understand the problem first. Explore the data deeply. Find the signal. Communicate the story clearly. Then build a solution that people can actually use.</p>
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
