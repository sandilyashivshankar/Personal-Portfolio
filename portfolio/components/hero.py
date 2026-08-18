import base64
import html
from pathlib import Path

import streamlit as st

PROFILE_PHOTO_URL = "https://raw.githubusercontent.com/sandilyashivshankar/Personal-Portfolio/main/Shiv_PF.jpeg"


def _portfolio_html(raw_html: str) -> str:
    lines = raw_html.strip("\n").splitlines()
    return "\n".join(line.lstrip() for line in lines)


def _load_profile_photo() -> str:
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
            return f"<img class='hero-photo walking-profile-photo' src='data:{mime};base64,{encoded}' alt='Shiv Shankar Tiwari profile photo'>"
    return f"<img class='hero-photo walking-profile-photo' src='{PROFILE_PHOTO_URL}' alt='Shiv Shankar Tiwari profile photo'>"


def render_hero(profile: dict):
    photo_html = _load_profile_photo()
    markup = f"""
<section id="home" class="hero hero-3d hero-reference-style">
<div class="hero-photo-backdrop" style="background-image:url('{PROFILE_PHOTO_URL}')"></div>
<div class="hero-landscape" aria-hidden="true"><div class="mountain mountain-back"></div><div class="mountain mountain-front"></div><div class="hero-wave wave-pink"></div><div class="hero-wave wave-blue"></div></div>
<div class="hero-depth-grid"></div>
<div class="hero-orb orb-left"></div>
<div class="hero-orb orb-right"></div>
<div class="hero-particle p1"></div><div class="hero-particle p2"></div><div class="hero-particle p3"></div><div class="hero-particle p4"></div>

<div class="hero-floating-card card-a"><span class="card-icon">✦</span><strong>DATA</strong><em>ANALYTICS</em></div>
<div class="hero-floating-card card-b"><span class="card-icon">⌁</span><strong>PYTHON</strong><em>DEVELOPER</em></div>
<div class="hero-floating-card card-c"><span class="card-icon">◈</span><strong>INSIGHTS</strong><em>THAT MATTER</em></div>
<div class="hero-floating-card card-d"><span class="card-icon">✦</span><strong>AI</strong><em>SOLUTIONS</em></div>

<div class="hero-content-layer">
  <div class="hero-photo-wrap walking-profile"><div class="photo-halo"></div>{photo_html}</div>
  <div class="hero-reference-kicker">H I&nbsp; • &nbsp;I ' M</div>
  <h1 class="hero-reference-name">{html.escape(profile["name"])}</h1>
  <div class="hero-reference-role">DATA ANALYST <span>•</span> AI ENTHUSIAST <span>•</span> PROBLEM SOLVER</div>
  <p class="statement hero-reference-statement">{html.escape(profile["objective"])}</p>
  <div class="hero-ctas hero-reference-cta">
    <a class="btn btn-primary" href="#projects">Explore My Work ↗</a>
  </div>
  <div class="hero-connect-label"><span></span> Let's Connect <span></span></div>
  <div class="hero-socials hero-socials-reference">
    <a class="social-pill" href="{html.escape(profile["github"])}" target="_blank" rel="noreferrer" aria-label="GitHub">GH</a>
    <a class="social-pill" href="{html.escape(profile["linkedin"])}" target="_blank" rel="noreferrer" aria-label="LinkedIn">in</a>
    <a class="social-pill" href="mailto:{html.escape(profile["email"])}" aria-label="Email">✉</a>
  </div>
  <a class="hero-scroll-button" href="#about" aria-label="Scroll to explore">SCROLL <span class="scroll-chevron">⌄</span></a>
</div>
</section>
"""
    st.markdown(_portfolio_html(markup), unsafe_allow_html=True)
