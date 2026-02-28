import streamlit as st
from PIL import Image

st.set_page_config(page_title="Narrative Visualization - Jamie", layout="wide")

st.title("Weather Patterns in Seattle")
st.write(Image.open('images/seattle-weather.jpg'))
st.write("This project is meant to explore weather patterns and trends in Seattle.\n")
st.write(
    "To explore this visual data story, please navigate it through the pages in the sidebar:\n"
    "- **Central Narrative**: We begin by taking into account daily weather patterns over time.\n"
    "- **Exploration**: For a closer reader-driven exploration of the data, we provide a few interactive designs.\n"
    "- **Methodology**: We lay down some key details about our data and limitations to our analysis.\n"
)
st.info("Dataset: `vega_datasets.data.seattle_weather()`")
