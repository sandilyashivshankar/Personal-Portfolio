import html
import base64
from pathlib import Path
import streamlit as st


def render_hero(profile: dict):
    initials = "".join(part[0] for part in profile["name"].split()[:2]).upper()
    role = " <span class='sep'>•</span> ".join(profile["roles"])

    # Automatically use assets/images/profile.jpg when the user adds it.
    photo_path = Path("assets/images/profile.jpg")
    if photo_path.exists():
        encoded = base64.b64encode(photo_path.read_bytes()).decode("ascii")
        photo_html = f'<img class="hero-photo" src="data:image/jpeg;base64,{encoded}" alt="{html.escape(profile["name"])}">'
    else:
        photo_html = f'<div class="hero-photo-fallback">{html.escape(initials)}</div>'

    st.markdown(
        f"""
        <section id="home" class="hero">
          <div class="hero-orbit"></div>
          <div class="hero-content-layer">
            <div class="hero-badge"><span class="pulse"></span> Open to data & AI opportunities</div>

            <div class="hero-photo-wrap">
              {photo_html}
            </div>

            <h1>Hi, I'm <span class="highlight">{html.escape(profile["name"])}</span></h1>
            <div class="role">{role}</div>
            <p class="statement">{html.escape(profile["objective"])}</p>

            <div class="hero-ctas">
              <a class="btn btn-primary" href="#projects">Explore My Work ↗</a>
              <a class="btn btn-ghost" href="#contact">Let's Connect</a>
            </div>

            <div class="hero-socials">
              <a class="social-pill" href="{html.escape(profile["github"])}" target="_blank" rel="noreferrer" aria-label="GitHub">GH</a>
              <a class="social-pill" href="{html.escape(profile["linkedin"])}" target="_blank" rel="noreferrer" aria-label="LinkedIn">in</a>
              <a class="social-pill" href="mailto:{html.escape(profile["email"])}" aria-label="Email">✉</a>
            </div>

            <div class="mini-terminal">
              <span class="prompt">shiv@portfolio</span><span class="command">:~$ build --insights --ai --impact</span>
              <span style="color:#34d399"> ✓ ready</span><span class="cursor">▌</span>
            </div>

            <div class="availability">Available for meaningful projects & opportunities</div>
          </div>
          <div class="scroll-cue">Scroll <span class="line"></span></div>
        </section>
        """,
        unsafe_allow_html=True,
    )
