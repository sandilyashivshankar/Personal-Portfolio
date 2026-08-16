# Shiv Shankar Tiwari — Cinematic Portfolio

A premium, animated personal portfolio built with **Python + Streamlit** and a custom cinematic CSS system.

## 1. Project structure

```text
portfolio/
├── .streamlit/
│   └── config.toml
├── assets/
│   ├── images/
│   │   └── profile.jpg        # add your photo here
│   ├── certificates/           # uploaded certificates
│   └── resume/
│       └── resume.pdf         # optional PDF resume
├── components/
│   ├── about.py
│   ├── analytics.py
│   ├── background.py
│   ├── common.py
│   ├── contact.py
│   ├── footer.py
│   ├── github.py
│   ├── hero.py
│   ├── navbar.py
│   ├── projects.py
│   ├── resume.py
│   ├── services.py
│   ├── skills.py
│   └── timeline.py
├── data/
│   ├── experience.py
│   ├── profile.py
│   └── projects.py
├── styles/
│   └── main.css
├── utils/
│   └── github.py
├── .env.example
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

## 2. Run locally

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install:

```bash
pip install -r requirements.txt
```

Create `.env` from `.env.example` if you want optional environment variables.

Start:

```bash
streamlit run app.py
```

## 3. Add your profile photo

Put your image at:

```text
assets/images/profile.jpg
```

The current hero intentionally has an initials fallback so the site still works before the photo is added. To use the actual image, update the `render_hero()` component to point at the local asset.

## 4. Add your resume

Put the PDF at:

```text
assets/resume/resume.pdf
```

The resume download button will become active automatically.

## 5. Edit portfolio content

Most content is intentionally separated from the UI:

- `data/profile.py` → name, role, links, objective
- `data/projects.py` → projects
- `data/experience.py` → experience and timeline
- `components/skills.py` → skill groups
- `components/services.py` → services
- `styles/main.css` → entire visual system

## 6. GitHub

The app reads public GitHub information for:

`https://github.com/sandilyashivshankar`

An optional `GITHUB_TOKEN` can be supplied through `.env` locally or Streamlit Secrets in deployment. The app gracefully falls back if GitHub is unavailable.

## 7. Deployment — Streamlit Community Cloud

1. Push this project to GitHub.
2. Create a new Streamlit Community Cloud app.
3. Set the main file to `app.py`.
4. Deploy.
5. If using secrets, add them in the app's Secrets settings as TOML:

```toml
GITHUB_TOKEN = ""
CONTACT_FORM_ENDPOINT = ""
```

Do not commit `.env` or `secrets.toml`.

## 8. Design

The supplied `styles/main.css` is the core cinematic design system and includes:

- glassmorphism
- gradient glow
- animated background orbs
- animated grid
- noise/vignette
- loading screen
- cinematic hero
- responsive layouts
- hover effects
- reduced-motion support
- Streamlit UI overrides

The project keeps the CSS in `styles/main.css`; the Streamlit entry point remains `app.py` at the project root.


## GitHub catalogue

The portfolio includes a catalogue of the repositories returned from the linked GitHub profile. Public repositories are displayed as clickable cards. Private repositories are named but are never copied or exposed; they remain subject to GitHub access controls.

## Certificates

The uploaded certificates are stored under `assets/certificates/` and exposed through an animated Credentials section with download buttons and verification links where a source document supplied one.
