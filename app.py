import streamlit as st
import pandas as pd

st.set_page_config(page_title="XTSC Quant Dashboard", layout="wide")

st.title("XTSC Historical Quant Dashboard")

macro = pd.read_csv("Data/Macro/vietnam_macro_monthly_2010_2026_model.csv")
st.subheader("Macro Data")
st.dataframe(macro.tail(24), use_container_width=True)

st.line_chart(macro.set_index("date")[["cpi_yoy_pct", "on_rate_pct", "vn_10y_yield_pct"]])