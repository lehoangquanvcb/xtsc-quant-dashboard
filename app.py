import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="XTSC Quant Dashboard", layout="wide")

BASE = Path(__file__).parent

def load_csv(path):
    p = BASE / path
    if p.exists():
        return pd.read_csv(p)
    return pd.DataFrame()

st.title("XTSC Historical Quant Dashboard")

macro = load_csv("Data/Macro/vietnam_macro_monthly_2010_2026_model.csv")
market = load_csv("Data/Market/vietnam_market_daily_2018_2026_placeholder.csv")
curve = load_csv("Data/YieldCurve/vietnam_yield_curve_monthly_2010_2026_placeholder.csv")
treasury = load_csv("Data/Treasury/xtsc_treasury_book_template.csv")
risk = load_csv("Data/Risk/risk_limits_template.csv")

tabs = st.tabs([
    "1. CEO Overview",
    "2. Macro Regime",
    "3. VNINDEX & FX",
    "4. Yield Curve",
    "5. Treasury Backtest",
    "6. Risk Limits",
    "7. Strategic Signals"
])

with tabs[0]:
    st.subheader("CEO Overview")
    c1, c2, c3, c4 = st.columns(4)
    if not macro.empty:
        latest = macro.iloc[-1]
        c1.metric("CPI YoY", f"{latest['cpi_yoy_pct']:.2f}%")
        c2.metric("ON Rate", f"{latest['on_rate_pct']:.2f}%")
        c3.metric("10Y Yield", f"{latest['vn_10y_yield_pct']:.2f}%")
        c4.metric("USD/VND", f"{latest['usd_vnd']:,.0f}")
    st.info("Dashboard này là bản CSO/CRO prototype. Các chuỗi placeholder cần thay bằng dữ liệu thật từ vnstock/SBV/VBMA.")

with tabs[1]:
    st.subheader("Macro Regime")
    st.dataframe(macro.tail(36), use_container_width=True)
    if not macro.empty:
        st.line_chart(macro.set_index("date")[["cpi_yoy_pct", "on_rate_pct", "vn_10y_yield_pct"]])

with tabs[2]:
    st.subheader("VNINDEX & FX")
    if not market.empty:
        st.dataframe(market.tail(30), use_container_width=True)
        cols = [c for c in ["vnindex_close", "usd_vnd_close", "foreign_flow_bn_vnd"] if c in market.columns]
        st.line_chart(market.set_index("date")[cols])
    else:
        st.warning("Chưa có market data. Hãy chạy vnstock connector hoặc upload CSV.")

with tabs[3]:
    st.subheader("Yield Curve")
    if not curve.empty:
        st.dataframe(curve.tail(50), use_container_width=True)
        latest_date = curve["date"].max()
        latest_curve = curve[curve["date"] == latest_date]
        st.bar_chart(latest_curve.set_index("tenor")["yield_pct"])
    else:
        st.warning("Chưa có yield curve data.")

with tabs[4]:
    st.subheader("Treasury Backtest")
    if not treasury.empty:
        st.dataframe(treasury, use_container_width=True)
        treasury["stress_loss_100bp_vnd_bn"] = treasury["amount_vnd_bn"] * treasury["duration_years"] * 0.01
        st.bar_chart(treasury.set_index("instrument")["stress_loss_100bp_vnd_bn"])
    else:
        st.warning("Chưa có treasury book.")

with tabs[5]:
    st.subheader("Risk Limits")
    st.dataframe(risk, use_container_width=True)

with tabs[6]:
    st.subheader("Strategic Signals")
    if not macro.empty:
        latest = macro.iloc[-1]
        signals = []
        if latest["cpi_yoy_pct"] > 5:
            signals.append("CPI cao: shorten duration, ưu tiên floating-rate assets.")
        if latest["on_rate_pct"] < latest["policy_rate_pct"] - 1:
            signals.append("Thanh khoản dễ: có thể tăng duration TPCP chọn lọc.")
        if latest["usd_vnd"] > 25500:
            signals.append("FX stress: giảm leverage và kiểm soát liquidity.")
        if not signals:
            signals.append("Tín hiệu hiện tại: Neutral / monitor.")
        for s in signals:
            st.write("•", s)
