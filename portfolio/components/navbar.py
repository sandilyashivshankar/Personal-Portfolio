import streamlit as st


def render_navbar():
    st.markdown(
        """
        <nav class="portfolio-sidebar" aria-label="Portfolio sections">
          <a class="sidebar-brand" href="#home" aria-label="Home"><span class="brand-orbit"></span><span class="brand-core">SST</span></a>
          <div class="sidebar-nav">
            <a class="side-link active" href="#home"><span class="side-icon">⌂</span><span class="side-label">Home</span></a>
            <a class="side-link" href="#about"><span class="side-icon">◎</span><span class="side-label">About</span></a>
            <a class="side-link" href="#skills"><span class="side-icon">✦</span><span class="side-label">Skills</span></a>
            <a class="side-link" href="#projects"><span class="side-icon">◈</span><span class="side-label">Projects</span></a>
            <a class="side-link" href="#experience"><span class="side-icon">↗</span><span class="side-label">Experience</span></a>
            <a class="side-link" href="#certificates"><span class="side-icon">◇</span><span class="side-label">Certificates</span></a>
            <a class="side-link" href="#analytics"><span class="side-icon">▥</span><span class="side-label">Analytics</span></a>
            <a class="side-link" href="#services"><span class="side-icon">✣</span><span class="side-label">Services</span></a>
            <a class="side-link" href="#contact"><span class="side-icon">⌁</span><span class="side-label">Contact</span></a>
          </div>
          <div class="sidebar-status"><span></span><small>AVAILABLE</small></div>
        </nav>
        <div class="mobile-topbar"><a class="mobile-brand" href="#home">SST<span>.</span></a><button class="mobile-menu-btn" type="button" aria-label="Open navigation" onclick="document.body.classList.toggle('mobile-nav-open')">☰</button></div>
        <div class="mobile-nav-backdrop" onclick="document.body.classList.remove('mobile-nav-open')"></div>
        <nav class="mobile-drawer" aria-label="Mobile portfolio sections">
          <div class="mobile-drawer-head"><strong>Explore</strong><button type="button" onclick="document.body.classList.remove('mobile-nav-open')">×</button></div>
          <a href="#home" onclick="document.body.classList.remove('mobile-nav-open')">Home</a><a href="#about" onclick="document.body.classList.remove('mobile-nav-open')">About</a><a href="#skills" onclick="document.body.classList.remove('mobile-nav-open')">Skills</a><a href="#projects" onclick="document.body.classList.remove('mobile-nav-open')">Projects</a><a href="#experience" onclick="document.body.classList.remove('mobile-nav-open')">Experience</a><a href="#certificates" onclick="document.body.classList.remove('mobile-nav-open')">Certificates</a><a href="#analytics" onclick="document.body.classList.remove('mobile-nav-open')">Analytics</a><a href="#services" onclick="document.body.classList.remove('mobile-nav-open')">Services</a><a href="#contact" onclick="document.body.classList.remove('mobile-nav-open')">Contact</a>
        </nav>
        """,
        unsafe_allow_html=True,
    )
