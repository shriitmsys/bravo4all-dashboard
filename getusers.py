import requests
import streamlit as st

def get_users():
    url = f"{st.secrets['baseUrl']}/users"
    headers = {
        "unifocus-api-secret": st.secrets["apiKey"]
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("_embedded", {}).get("collection", [])
    else:
        st.error(f"Failed to fetch users: {response.status_code}")
        return []