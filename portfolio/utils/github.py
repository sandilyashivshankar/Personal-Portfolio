from __future__ import annotations

import os
from typing import Any

import requests
import streamlit as st


@st.cache_data(ttl=900, show_spinner=False)
def get_github_profile(username: str) -> dict[str, Any] | None:
    token = os.getenv("GITHUB_TOKEN", "")
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        response = requests.get(
            f"https://api.github.com/users/{username}",
            headers=headers,
            timeout=8,
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None


@st.cache_data(ttl=900, show_spinner=False)
def get_github_repositories(username: str) -> list[dict[str, Any]]:
    token = os.getenv("GITHUB_TOKEN", "")
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        response = requests.get(
            f"https://api.github.com/users/{username}/repos",
            params={"sort": "updated", "per_page": 9},
            headers=headers,
            timeout=8,
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return []
