from pathlib import Path
import streamlit as st
from .common import section_heading


def render_resume():
    st.markdown('<section id="resume">', unsafe_allow_html=True)
    section_heading("10 / RESUME", "One page. <span class='accent'>Full story</span>.",
                   "Your uploaded resume is available directly from the portfolio.")
    docx_path = Path("assets/resume/Shiv_Shankar_Tiwari_Resume.docx")
    pdf_path = Path("assets/resume/resume.pdf")

    st.markdown(
        """
        <div class="glass-card resume-card reveal">
          <div class="icon">▤</div>
          <h3 style="margin-bottom:.4rem">Professional Resume</h3>
          <p style="color:var(--text-2);max-width:620px;margin:0 auto">
            Focused on Computer Science, Data Science & AI, analytics projects and practical development.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)
    with c1:
        if pdf_path.exists():
            st.download_button("Download PDF ↓", pdf_path.read_bytes(), file_name="Shiv_Shankar_Tiwari_Resume.pdf", mime="application/pdf", use_container_width=True)
        else:
            st.info("Add assets/resume/resume.pdf to enable PDF download.")
    with c2:
        if docx_path.exists():
            st.download_button("Download DOCX ↓", docx_path.read_bytes(), file_name="Shiv_Shankar_Tiwari_Resume.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document", use_container_width=True)

    st.markdown("</section>", unsafe_allow_html=True)
