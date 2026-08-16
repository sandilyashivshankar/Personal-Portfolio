# Shiv Shankar Tiwari — Personal Portfolio

A cinematic, animated **Python + Streamlit** portfolio focused on Data Analytics, AI/ML and practical intelligent applications.

## Run locally

```bash
cd portfolio
uv pip install -r requirements.txt
uv run streamlit run app.py
```

Or:

```bash
cd portfolio
pip install -r requirements.txt
streamlit run app.py
```

Open `http://localhost:8501`.

## Main features

- Cinematic animated hero and glassmorphism UI
- Data Analytics / AI / ML personal branding
- Featured project showcase
- GitHub repository catalogue
- Certificates & credential downloads
- Resume access
- Interactive analytics section
- Experience and education timeline
- Responsive navigation and reduced-motion support
- Streamlit Community Cloud ready

The actual Streamlit application lives in `portfolio/app.py` and has its own deployment dependencies in `portfolio/requirements.txt`.

## Security

Never commit `.env`, API keys, GitHub tokens or Streamlit secrets. Use environment variables or Streamlit Secrets for private credentials.
