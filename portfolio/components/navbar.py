import streamlit as st


def render_navbar():
    st.markdown(
        """
        <nav class="glass-navbar">
          <a class="nav-brand" href="#home">
            <span class="dot"></span> SST<span style="color:var(--text-2)">.</span>
          </a>
          <div class="nav-links">
            <a class="nav-link" href="#about">About</a>
            <a class="nav-link" href="#skills">Skills</a>
            <a class="nav-link" href="#projects">Projects</a>
            <a class="nav-link" href="#experience">Experience</a>
            <a class="nav-link" href="#certificates">Certificates</a>
            <a class="nav-link" href="#analytics">Analytics</a>
            <a class="nav-link" href="#contact">Contact</a>
          </div>
        </nav>
        """,
        unsafe_allow_html=True,
    )
