from pathlib import Path
import streamlit as st
from .common import section_heading


def render_resume():
    st.markdown('<section id="resume">', unsafe_allow_html=True)
    section_heading(
        "10 / RESUME",
        "One page. <span class='accent'>Full story</span>.",
        "Your latest CV is available directly from the portfolio."
    )

    resume_path = Path("SST_PF_CV.pdf")

    st.markdown(
        """
        <div class="glass-card resume-card reveal">
          <div class="icon">▤</div>
          <h3 style="margin-bottom:.4rem">Professional CV</h3>
          <p style="color:var(--text-2);max-width:620px;margin:0 auto">
            Data Analyst profile focused on Python, data analytics, business intelligence,
            AI/ML, generative AI and practical analytics projects.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if resume_path.exists():
        st.download_button(
            "Download CV ↓",
            resume_path.read_bytes(),
            file_name="Shiv_Shankar_Tiwari_CV.pdf",
            mime="application/pdf",
            use_container_width=True,
        )
    else:
        st.error("The CV file could not be found in the portfolio repository.")

    st.markdown("</section>", unsafe_allow_html=True)
