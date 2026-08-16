import base64
import html
from pathlib import Path

import streamlit as st


PROFILE_PHOTO_URL = "https://raw.githubusercontent.com/sandilyashivshankar/Personal-Portfolio/main/Shiv_PF.jpeg"


def _portfolio_html(raw_html: str) -> str:
    """Normalize generated HTML so Streamlit does not treat it as a code block."""
    lines = raw_html.strip("\n").splitlines()
    return "\n".join(line.lstrip() for line in lines)


def _load_profile_photo() -> str:
    """Use the supplied GitHub profile photo, with local-file fallback support."""
    candidates = [
        Path("assets/images/profile.jpg"),
        Path("assets/images/profile.jpeg"),
        Path("assets/images/profile.JPG"),
        Path("assets/images/profile.JPEG"),
        Path("assets/images/profile.png"),
        Path("assets/images/Profile.jpg"),
        Path("assets/images/Profile.jpeg"),
    ]

    for photo_path in candidates:
        if photo_path.exists() and photo_path.is_file():
            suffix = photo_path.suffix.lower()
            mime = "image/png" if suffix == ".png" else "image/jpeg"
            encoded = base64.b64encode(photo_path.read_bytes()).decode("ascii")
            return f"<img class='hero-photo' src='data:{mime};base64,{encoded}' alt='Shiv Shankar Tiwari profile photo'>"

    return f"<img class='hero-photo' src='{PROFILE_PHOTO_URL}' alt='Shiv Shankar Tiwari profile photo'>"


def render_hero(profile: dict):
    role = " <span class='sep'>•</span> ".join(profile["roles"])
    photo_html = _load_profile_photo()

    markup = f"""
<section id="home" class="hero">
<div class="hero-orbit"></div>
<div class="hero-content-layer">
<div class="hero-photo-wrap">{photo_html}</div>
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
<div class="availability">Available for meaningful projects & opportunities</div>
</div>
<div class="scroll-cue">Scroll <span class="line"></span></div>
</section>
"""
    st.markdown(_portfolio_html(markup), unsafe_allow_html=True)
