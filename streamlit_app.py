import streamlit as st
import streamlit.components.v1 as components

# Ladataan game.html tiedosto
with open("game.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Näytetään HTML Streamlitissä
components.html(html_code, height=600, scrolling=True)
