import html
import json
from pathlib import Path

import streamlit as st

from .common import section_heading
from utils.github import get_github_profile


def _load_repositories():
    path = Path("data/github_repositories.json")
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def render_github(profile):
    st.markdown('<section id="github">', unsafe_allow_html=True)
    section_heading(
        "04 / OPEN SOURCE",
        "My GitHub, <span class='accent'>my lab</span>.",
        "A complete catalogue of the repositories associated with my GitHub profile, "
        "with direct links and visibility-aware presentation."
    )

    username = profile["github"].rstrip("/").split("/")[-1]
    gh = get_github_profile(username)
    repos = _load_repositories()

    public_repos = [r for r in repos if not r.get("private")]
    private_repos = [r for r in repos if r.get("private")]

    stats = [
        ("Total tracked", str(len(repos))),
        ("Public", str(len(public_repos))),
        ("Private", str(len(private_repos))),
        ("Profile", username),
    ]

    st.markdown(
        '<div class="github-grid">' +
        ''.join(
            f'<div class="glass-card gh-stat reveal"><div class="num">{html.escape(v)}</div>'
            f'<div class="lab">{html.escape(l)}</div></div>'
            for l, v in stats
        ) +
        '</div>',
        unsafe_allow_html=True,
    )

    if gh:
        st.markdown(
            f"""
            <div class="glass-card reveal" style="padding:1.4rem;margin-bottom:1.6rem">
              <div style="display:flex;justify-content:space-between;gap:1rem;align-items:center;flex-wrap:wrap">
                <div>
                  <div style="color:var(--text-2);font-size:.78rem;text-transform:uppercase;letter-spacing:.12em">Live GitHub profile</div>
                  <div style="font-size:1.2rem;font-weight:800;margin-top:.25rem">{html.escape(gh.get("name") or username)}</div>
                  <div style="color:var(--text-2);font-size:.85rem;margin-top:.2rem">Updated from GitHub API when available</div>
                </div>
                <a class="btn btn-ghost" href="{html.escape(profile["github"])}" target="_blank" rel="noreferrer">Open GitHub ↗</a>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="skills-filter" style="margin-bottom:1.2rem">
          <span class="filter-pill active">All</span>
          <span class="filter-pill">Public</span>
          <span class="filter-pill">Private</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cards = []
    for repo in public_repos:
        lang = repo.get("language") or "Repository"
        cards.append(
            f"""
            <div class="glass-card gh-repo-card reveal">
              <div style="display:flex;justify-content:space-between;gap:.8rem;align-items:flex-start">
                <a href="{html.escape(repo["url"])}" target="_blank" rel="noreferrer">{html.escape(repo["name"])} ↗</a>
                <span class="tech-badge">PUBLIC</span>
              </div>
              <p class="gh-repo-desc">GitHub repository from the portfolio project catalogue.</p>
              <div class="gh-repo-meta"><span>{html.escape(lang)}</span></div>
            </div>
            """
        )

    st.markdown(
        '<div class="gh-repo-list">' + "".join(cards) + "</div>",
        unsafe_allow_html=True,
    )

    if private_repos:
        st.markdown(
            '<div class="section-wrap tight"><span class="section-eyebrow">PRIVATE WORK</span>'
            '<p class="section-subtitle" style="margin-bottom:1rem">Private repositories are listed below but never exposed or copied into the website. '
            'They require GitHub access for visitors to open.</p></div>',
            unsafe_allow_html=True,
        )
        private_cards = []
        for repo in private_repos:
            private_cards.append(
                f"""
                <div class="glass-card gh-repo-card reveal">
                  <div style="display:flex;justify-content:space-between;gap:.8rem;align-items:flex-start">
                    <span style="font-weight:700;color:var(--text-0)">{html.escape(repo["name"])}</span>
                    <span class="tech-badge">PRIVATE</span>
                  </div>
                  <p class="gh-repo-desc">Repository exists in the GitHub account but is private.</p>
                </div>
                """
            )
        st.markdown('<div class="gh-repo-list">' + "".join(private_cards) + "</div>", unsafe_allow_html=True)

    st.markdown("</section>", unsafe_allow_html=True)
