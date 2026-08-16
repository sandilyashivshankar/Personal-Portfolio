# Shiv Shankar Tiwari — Cinematic Portfolio

A premium, animated personal portfolio built with **Python + Streamlit**, custom CSS, Plotly analytics, GitHub integration, project discovery, certificates and resume access.

## Project structure

```text
portfolio/
├── .streamlit/
├── assets/
│   ├── images/
│   ├── certificates/
│   └── resume/
├── components/
├── data/
├── styles/
├── utils/
├── .env.example
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

## Run locally

From the `portfolio` directory:

```bash
uv pip install -r requirements.txt
uv run streamlit run app.py
```

Or with standard Python:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

The local site opens at `http://localhost:8501`.

## Personal assets

- Add your professional photo as `assets/images/profile.jpg`.
- Add a PDF resume as `assets/resume/resume.pdf` if you want a PDF download in addition to the supplied DOCX resume.
- Certificates are stored under `assets/certificates/` and are surfaced in the Credentials section.

## Portfolio content

- `data/profile.py` — personal identity, headline, links and objective.
- `data/projects.py` — curated featured projects.
- `data/github_repositories.json` — repository catalogue used for the GitHub showcase.
- `data/experience.py` — timeline.
- `data/certificates.py` — credential metadata.
- `styles/main.css` — cinematic visual system.
- `components/` — modular Streamlit UI sections.

## GitHub

The portfolio links to the GitHub profile `sandilyashivshankar` and presents the repository catalogue with public/private visibility awareness. Public repositories are directly clickable; private repositories are never copied or exposed.

An optional `GITHUB_TOKEN` can be supplied through local `.env` or Streamlit Secrets for richer GitHub API access. Never commit tokens.

## Deployment

For Streamlit Community Cloud, point the app to:

```text
portfolio/app.py
```

The repository includes a portfolio-local `requirements.txt`, so deployment does not depend on the root-level requirements file.

Optional secrets:

```toml
GITHUB_TOKEN = ""
CONTACT_FORM_ENDPOINT = ""
```

## Design system

The portfolio is intentionally designed as a cinematic analytics/AI portfolio with:

- glassmorphism cards
- animated gradient orbs
- grid and vignette layers
- smooth reveal effects
- interactive Plotly analytics
- responsive navigation
- project and GitHub showcases
- credential cards with download/verification actions
- reduced-motion support
- Streamlit UI cleanup

A global Markdown normalization layer prevents indented multiline HTML templates from being rendered as raw source code in Streamlit.
