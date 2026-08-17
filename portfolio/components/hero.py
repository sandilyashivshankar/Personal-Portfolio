import base64
import html
from pathlib import Path

import streamlit as st

PROFILE_PHOTO_URL = "https://raw.githubusercontent.com/sandilyashivshankar/Personal-Portfolio/main/Shiv_PF.jpeg"


def _portfolio_html(raw_html: str) -> str:
    lines = raw_html.strip("\n").splitlines()
    return "\n".join(line.lstrip() for line in lines)


def _load_profile_photo() -> str:
    candidates = [Path("assets/images/profile.jpg"), Path("assets/images/profile.jpeg"), Path("assets/images/profile.JPG"), Path("assets/images/profile.JPEG"), Path("assets/images/profile.png"), Path("assets/images/Profile.jpg"), Path("assets/images/Profile.jpeg")]
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
<section id="home" class="hero hero-3d">
<div class="hero-photo-backdrop" style="background-image:url('{PROFILE_PHOTO_URL}')"></div>
<div class="hero-depth-grid"></div>
<div class="hero-floating-card card-a">DATA <b>+</b> AI</div>
<div class="hero-floating-card card-b">PYTHON <b>◈</b></div>
<div class="hero-floating-card card-c">INSIGHTS <b>↗</b></div>
<div class="hero-content-layer">
<div class="hero-photo-wrap"><div class="photo-halo"></div>{photo_html}</div>
<div class="hero-eyebrow"><span></span> DATA × AI × CREATIVITY <span></span></div>
<h1>Hi, I'm <span class="highlight gradient-text">{html.escape(profile["name"])}</span></h1>
<div class="role">{role}</div>
<p class="statement">{html.escape(profile["objective"])}</p>
<div class="hero-ctas">
<a class="btn btn-primary" href="#projects">Explore My Work ↗</a>
<a class="btn btn-ghost" href="#contact">Let's Connect</a>
</div>
<div class="hero-socials">
<a class="social-pill" href="{html.escape(profile["github"])}" target="_blank" rel="noreferrer">GH</a>
<a class="social-pill" href="{html.escape(profile["linkedin"])}" target="_blank" rel="noreferrer">in</a>
<a class="social-pill" href="mailto:{html.escape(profile["email"])}">✉</a>
</div>
</div>
<div class="scroll-cue">SCROLL <span class="line"></span></div>
</section>
"""
    st.markdown(_portfolio_html(markup), unsafe_allow_html=True)
