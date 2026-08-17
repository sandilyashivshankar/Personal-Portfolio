import requests
import streamlit as st
from .common import section_heading


CV_URL = "https://raw.githubusercontent.com/sandilyashivshankar/Personal-Portfolio/main/SST_PF_CV.pdf"


def render_resume():
    st.markdown('<section id="resume">', unsafe_allow_html=True)
    section_heading(
        "10 / RESUME",
        "One page. <span class='accent'>Full story</span>.",
        "Your latest CV uploaded to the portfolio repository is available directly here."
    )

    st.markdown(
        """
        <div class="glass-card resume-card reveal">
          <div class="icon">▤</div>
          <h3 style="margin-bottom:.4rem">Professional CV</h3>
          <p style="color:var(--text-2);max-width:620px;margin:0 auto">
            Data Analyst profile focused on data analytics, Python, business intelligence,
            AI/ML, generative AI and practical analytics projects.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    try:
        response = requests.get(CV_URL, timeout=15)
        response.raise_for_status()
        st.download_button(
            "Download CV ↓",
            response.content,
            file_name="Shiv_Shankar_Tiwari_CV.pdf",
            mime="application/pdf",
            use_container_width=True,
        )
    except requests.RequestException:
        st.link_button("Open CV ↗", CV_URL, use_container_width=True)

    st.markdown("</section>", unsafe_allow_html=True)
