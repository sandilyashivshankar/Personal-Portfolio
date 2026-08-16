import os
import html
import requests
import streamlit as st
from .common import section_heading


def render_contact(profile):
    st.markdown('<section id="contact">', unsafe_allow_html=True)
    section_heading("08 / CONTACT", "Let's build something <span class='accent'>intelligent</span>.",
                   "Have an idea, opportunity or collaboration in mind? Start the conversation.")

    left, right = st.columns([0.85, 1.15], gap="large")

    with left:
        st.markdown(
            f"""
            <div class="glass-card contact-info-card">
              <h3 style="margin-top:0">Connect directly</h3>
              <p class="contact-note">The fastest way to reach me is through email or LinkedIn. I am interested in meaningful data, AI and analytics opportunities.</p>
              <div class="contact-info-row"><div class="contact-info-icon">✉</div><div><div class="label">Email</div><a href="mailto:{html.escape(profile["email"])}">{html.escape(profile["email"])}</a></div></div>
              <div class="contact-info-row"><div class="contact-info-icon">in</div><div><div class="label">LinkedIn</div><a href="{html.escape(profile["linkedin"])}" target="_blank" rel="noreferrer">Open LinkedIn ↗</a></div></div>
              <div class="contact-info-row"><div class="contact-info-icon">GH</div><div><div class="label">GitHub</div><a href="{html.escape(profile["github"])}" target="_blank" rel="noreferrer">Open GitHub ↗</a></div></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown('<div class="glass-card form-shell">', unsafe_allow_html=True)
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Name", placeholder="Your name")
            email = st.text_input("Email", placeholder="you@example.com")
            message = st.text_area("Message", placeholder="Tell me about the opportunity or idea...", height=160)
            submitted = st.form_submit_button("Send Message ↗")

            if submitted:
                if not name.strip() or not email.strip() or not message.strip():
                    st.error("Please complete all fields.")
                elif "@" not in email:
                    st.error("Please enter a valid email address.")
                else:
                    endpoint = os.getenv("CONTACT_FORM_ENDPOINT", "").strip()
                    if endpoint:
                        try:
                            response = requests.post(
                                endpoint,
                                json={"name": name, "email": email, "message": message},
                                timeout=8,
                            )
                            response.raise_for_status()
                            st.success("Message sent successfully.")
                        except requests.RequestException:
                            st.warning("The form endpoint could not be reached. Please use the email or LinkedIn links.")
                    else:
                        st.success("Thanks! Your message is ready. Please connect via email or LinkedIn to complete delivery.")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</section>", unsafe_allow_html=True)
