"""Shading simulator: half-cut vs full-cell panels in a 10-panel string.

Streamlit wrapper for the self-contained simulator in ./simulator/index.html.
The simulator reports its own height to Streamlit and follows the app theme,
so the page sizes itself with no inner scrollbar.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Shading simulator | DJ Solar Corp",
    page_icon="⛅",
    layout="wide",
)

# Trim Streamlit's default top padding so the simulator's own header leads the page.
st.markdown(
    """
    <style>
      .block-container, [data-testid="stMainBlockContainer"] {
        padding-top: 2rem;
        padding-bottom: 1rem;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

shading_simulator = components.declare_component(
    "shading_simulator",
    path=str(Path(__file__).parent / "simulator"),
)

shading_simulator(key="simulator")
