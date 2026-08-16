import html
import streamlit as st


def section_heading(eyebrow: str, title: str, subtitle: str = ""):
    """Render a clean section heading without numbered eyebrow labels."""
    subtitle_html = f'<p class="section-subtitle">{html.escape(subtitle)}</p>' if subtitle else ""
    st.markdown(
        f"""
<div class="section-wrap reveal">
  <h2 class="section-title">{title}</h2>
  {subtitle_html}
</div>
""",
        unsafe_allow_html=True,
    )


def card(content: str, classes: str = "glass-card"):
    st.markdown(f'<div class="{classes}">{content}</div>', unsafe_allow_html=True)


def tech_badges(items: list[str]) -> str:
    return "".join(f'<span class="tech-badge">{html.escape(x)}</span>' for x in items)
