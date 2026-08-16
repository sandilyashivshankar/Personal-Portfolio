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
<style>
.about-identity {{
  display:flex; flex-wrap:wrap; align-items:center; gap:.75rem 1rem;
  margin:-.5rem 0 2rem;
}}
.about-role-line {{ display:flex; flex-wrap:wrap; gap:.55rem; }}
.role-chip {{
  display:inline-flex; align-items:center; padding:.5rem .85rem;
  border:1px solid rgba(34,211,238,.22); border-radius:999px;
  background:linear-gradient(135deg,rgba(34,211,238,.08),rgba(139,92,246,.10));
  color:var(--text-1); font-size:.86rem; font-weight:650;
  box-shadow:0 8px 28px rgba(34,211,238,.06);
  transition:transform .25s ease,border-color .25s ease,box-shadow .25s ease;
}}
.role-chip:hover {{ transform:translateY(-2px); border-color:rgba(34,211,238,.5); box-shadow:0 10px 30px rgba(139,92,246,.16); }}
.about-availability {{ margin-left:auto; white-space:nowrap; display:inline-flex; align-items:center; gap:.45rem; }}
.about-availability .pulse {{ width:8px; height:8px; border-radius:50%; background:#34d399; box-shadow:0 0 12px rgba(52,211,153,.65); }}
@media (max-width:760px) {{ .about-availability {{ margin-left:0; }} }}
</style>
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
