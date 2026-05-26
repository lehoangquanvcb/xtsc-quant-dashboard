from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[1]

def load_macro_monthly():
    return pd.read_csv(BASE / "Data/Macro/vietnam_macro_monthly_2010_2026_model.csv", parse_dates=["date"])

def load_market_daily():
    return pd.read_csv(BASE / "Data/Market/vietnam_market_daily_2018_2026_placeholder.csv", parse_dates=["date"])

def load_yield_curve():
    return pd.read_csv(BASE / "Data/YieldCurve/vietnam_yield_curve_monthly_2010_2026_placeholder.csv", parse_dates=["date"])

def load_sources():
    return pd.read_csv(BASE / "Data/Metadata/source_map.csv")

if __name__ == "__main__":
    print(load_macro_monthly().tail())