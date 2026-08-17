import streamlit as st


def render_background():
    st.markdown(
        """
        <div class="bg-fx" aria-hidden="true">
          <div class="orb orb-1"></div>
          <div class="orb orb-2"></div>
          <div class="orb orb-3"></div>
          <div class="grid-overlay"></div>
          <div class="aurora aurora-1"></div>
          <div class="aurora aurora-2"></div>
          <div class="particle-field">
            <span></span><span></span><span></span><span></span><span></span>
            <span></span><span></span><span></span><span></span><span></span>
            <span></span><span></span><span></span><span></span><span></span>
          </div>
        </div>
        <div class="noise-fx"></div>
        <div class="vignette"></div>
        """,
        unsafe_allow_html=True,
    )


def render_loader():
    st.markdown(
        """
        <div class="loader-screen">
          <div class="loader-mark">ENTERING SHIV'S DIGITAL UNIVERSE</div>
          <div class="loader-ring"></div>
          <div class="loader-bar"><span></span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
