import streamlit as st
from io import load_weather
from charts import chart_dashboard

st.set_page_config(page_title="Explore", layout="wide")
df = load_weather()

st.title("Interactive Exploratory View")
st.write("Use interaction to validate and extend the story—focus on one weather type, then zoom into a time window.")

st.altair_chart(chart_dashboard(df), use_container_width=True)

st.markdown("**Guided prompts:**")
st.write("- Filter to one weather type (e.g., `sun`, `rain`)—does the temperature distribution shift?")
st.write("- Brush a specific year—do extremes cluster in particular periods?")
st.write("- Compare histogram shape across weather types—what changes most: center, spread, or tails?")

st.write("Use interaction to validate and extend the story—focus on one year, then zoom into a time window.")

st.altair_chart(dashboard_precipitation_over_time(df), use_container_width=True)

st.markdown("**Guided prompts:**")
st.write("- Filter to one year—do the precipitation trends by month shift?")
st.write("- Brush a specific collection of months—do extremes cluster in particular periods?")
st.write("- Compare histograms across months—what changes most: modes, spreads, or shapes?")
st.write("- Brush a specific time period in both dashboards-how do precipitation trends compare to temperature trends?")