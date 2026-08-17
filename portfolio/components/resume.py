import requests
import streamlit as st
from .common import section_heading


CV_URL = "https://raw.githubusercontent.com/sandilyashivshankar/Personal-Portfolio/main/SST_PF_CV.pdf"


def render_resume():
    st.markdown('<section id="resume">', unsafe_allow_html=True)
    section_heading(
        "10 / RESUME",
        "One page. <span class='accent'>Full story</span>.",
        "A concise view of my professional journey, technical strengths, and the kind of data-driven solutions I enjoy building."
    )

    st.markdown(
        """
        <div class="glass-card resume-card reveal">
          <div class="icon">▤</div>
          <h3 style="margin-bottom:.65rem">Professional CV</h3>
          <div style="max-width:820px;margin:0 auto;text-align:left">
            <p style="color:var(--text-1);font-size:1.04rem;line-height:1.8;margin:0 0 1rem">
              I am a <strong style="color:var(--text-0)">Data Analyst and Data + AI professional</strong>
              with a strong foundation in Python, data analytics, machine learning, business intelligence,
              and practical AI application development. I enjoy transforming raw and complex information
              into meaningful insights, clear visual stories, and solutions that can support better decisions.
            </p>
            <p style="color:var(--text-2);line-height:1.8;margin:0 0 1rem">
              My project experience spans <strong>exploratory data analysis, interactive dashboards,
              predictive modeling, deep learning, Generative AI, RAG systems, AI assistants,
              and multi-agent workflows</strong>. I focus on understanding the problem first,
              exploring the data carefully, selecting practical techniques, and communicating results
              in a way that is useful to real people and businesses.
            </p>
            <p style="color:var(--text-2);line-height:1.8;margin:0">
              I am particularly interested in opportunities where <strong>analytics, AI, and business
              problem-solving</strong> come together, allowing me to continuously learn, build practical
              solutions, and create measurable value through data.
            </p>
          </div>
          <div class="resume-highlights" style="display:flex;flex-wrap:wrap;justify-content:center;gap:.65rem;margin-top:1.5rem">
            <span class="tag-chip">Data Analytics</span>
            <span class="tag-chip">Python</span>
            <span class="tag-chip">Power BI</span>
            <span class="tag-chip">Machine Learning</span>
            <span class="tag-chip">Generative AI</span>
            <span class="tag-chip">RAG</span>
            <span class="tag-chip">Prompt Engineering</span>
          </div>
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
