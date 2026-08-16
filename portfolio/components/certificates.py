import html
from pathlib import Path

import streamlit as st

from .common import section_heading


def render_certificates(certificates):
    st.markdown('<section id="certificates">', unsafe_allow_html=True)
    section_heading(
        "06 / CREDENTIALS",
        "Proof of <span class='accent'>learning</span>.",
        "Verified learning experiences across AI, data analytics, predictive modelling and deep learning."
    )

    cols = st.columns(2, gap="large")
    for idx, cert in enumerate(certificates):
        with cols[idx % 2]:
            st.markdown(
                f"""
                <div class="glass-card achieve-card reveal" style="margin-bottom:1.2rem">
                  <div class="achieve-icon">✦</div>
                  <div style="flex:1">
                    <h4>{html.escape(cert["title"])}</h4>
                    <div class="issuer">{html.escape(cert["issuer"])}</div>
                    <div class="date">{html.escape(cert["date"])}</div>
                    <p class="gh-repo-desc" style="min-height:0;margin-bottom:.7rem">{html.escape(cert["summary"])}</p>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            path = Path(cert["file"])
            if path.exists():
                left, right = st.columns([1, 1])
                with left:
                    st.download_button(
                        "Certificate ↓",
                        data=path.read_bytes(),
                        file_name=path.name,
                        mime="application/pdf",
                        key=f"cert_dl_{idx}",
                        use_container_width=True,
                    )
                with right:
                    if cert.get("credential"):
                        st.markdown(
                            f'<a class="link-btn" href="{html.escape(cert["credential"])}" target="_blank" rel="noreferrer" style="display:block">Verify ↗</a>',
                            unsafe_allow_html=True,
                        )
    st.markdown("</section>", unsafe_allow_html=True)
