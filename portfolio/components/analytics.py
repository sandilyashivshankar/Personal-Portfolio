import streamlit as st
import pandas as pd
import plotly.express as px
from .common import section_heading


def render_analytics():
    st.markdown('<section id="analytics">', unsafe_allow_html=True)
    section_heading("06 / DATA STORY", "Let the <span class='accent'>numbers</span> speak.",
                   "An interactive mini dashboard that demonstrates how I communicate patterns visually.")

    kpis = [
        ("Projects", "4+", "Portfolio builds"),
        ("Focus", "AI + Data", "Core direction"),
        ("Stack", "Python", "Primary language"),
        ("Style", "Insight", "Outcome first"),
    ]
    st.markdown(
        '<div class="kpi-row">' +
        ''.join(f'<div class="glass-card kpi-card reveal"><div class="kpi-label">{l}</div><div class="kpi-value">{v}</div><div class="kpi-delta up">{d}</div></div>' for l,v,d in kpis) +
        '</div>',
        unsafe_allow_html=True,
    )

    data = pd.DataFrame({
        "Area": ["Analytics", "AI/ML", "Visualization", "Automation", "BI"],
        "Focus": [92, 86, 82, 74, 78],
    })
    fig = px.bar(data, x="Area", y="Focus", text="Focus", template="plotly_dark")
    fig.update_layout(
        height=360,
        margin=dict(l=10,r=10,t=20,b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#c7ccdd"),
        xaxis_title=None,
        yaxis_title=None,
    )
    fig.update_traces(marker_line_width=0, textposition="outside")
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    st.markdown("</section>", unsafe_allow_html=True)
