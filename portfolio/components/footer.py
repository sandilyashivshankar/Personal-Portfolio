import html
import streamlit as st


def render_footer(profile):
    st.markdown(
        f"""
        <footer class="site-footer">
          <div class="footer-socials">
            <a class="social-pill" href="{html.escape(profile["github"])}" target="_blank" rel="noreferrer">GH</a>
            <a class="social-pill" href="{html.escape(profile["linkedin"])}" target="_blank" rel="noreferrer">in</a>
            <a class="social-pill" href="mailto:{html.escape(profile["email"])}">✉</a>
          </div>
          <div>© 2026 {html.escape(profile["name"])} · Built with Python + Streamlit.</div>
        </footer>
        """,
        unsafe_allow_html=True,
    )
