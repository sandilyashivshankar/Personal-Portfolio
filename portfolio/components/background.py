import streamlit as st


def render_background():
    st.markdown(
        """
        <div class="bg-fx">
          <div class="orb orb-1"></div>
          <div class="orb orb-2"></div>
          <div class="orb orb-3"></div>
          <div class="grid-overlay"></div>
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
          <div class="loader-mark">INITIALIZING EXPERIENCE</div>
          <div class="loader-bar"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
