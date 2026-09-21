# Shading simulator: half-cut vs full-cell panels

An interactive demo by DJ Solar Corp. Paint a shadow onto a string of 10 panels and compare how half-cut and full-cell panels respond to the exact same shade. The page shows the string's voltage, current and power, each panel's voltage, and which bypass diodes are on.

## Files

| Path | Purpose |
|---|---|
| `app.py` | Streamlit app that loads the simulator as a component |
| `simulator/index.html` | The simulator: model, drawing and controls in one file. Also opens on its own in any browser |
| `requirements.txt` | Python dependency installed by Streamlit Community Cloud |
| `.streamlit/config.toml` | Page theme matched to the simulator's background |

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository and upload everything in this folder, keeping the structure (including the hidden `.streamlit` folder).
2. In Streamlit Community Cloud, create a new app from that repository, pick the branch, and set the main file path to `app.py`.
3. Deploy. Community Cloud installs `requirements.txt` automatically.

Pushing from the command line instead:

```bash
git init
git add .
git commit -m "Add shading simulator"
git branch -M main
git remote add origin https://github.com/<your-account>/shading-simulator.git
git push -u origin main
```

## How the Streamlit embed works

`app.py` serves the `simulator` folder as a static Streamlit component, so there is no build step. The page sends its own height to Streamlit (no inner scrollbar on phones) and follows the app's light or dark theme. Opened outside Streamlit, that bridge does nothing.

## Model assumptions

- 10 panels in series, mounted upright (portrait).
- Each panel: 50 V open circuit, 15 A short circuit, 600 W (fill factor 0.80 assumed), three bypass diodes.
- Both panel types share the same unshaded ratings, so every difference comes from how the cells are wired.
- The inverter finds the string's highest power point.
- Standard cells at 1000 W/m² and 25 °C. Cell-level shading features, such as the Hi-MO X10's anti-shading design, are not modeled.
- Illustrative model, not a product datasheet.

## Changing the panel ratings

The ratings are constants at the top of the model script in `simulator/index.html` (`PANEL_VOC`, `PANEL_ISC`, `PANEL_PMAX`). If you change them, also update the "How the numbers are made" note on the page and check the chart axes, which are fixed at 550 V and 7 kW.
