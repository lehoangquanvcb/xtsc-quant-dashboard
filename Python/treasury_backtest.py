import pandas as pd
from load_data import load_macro_monthly

def duration_pnl_proxy(duration_years=5.0, amount_vnd_bn=1000):
    df = load_macro_monthly().sort_values("date").copy()
    df["yield_change_bp"] = df["vn_10y_yield_pct"].diff() * 100
    # Approximate bond P&L: -Duration * yield change * amount
    df["pnl_vnd_bn"] = -duration_years * (df["yield_change_bp"]/10000) * amount_vnd_bn
    return df[["date","vn_10y_yield_pct","yield_change_bp","pnl_vnd_bn","regime"]]

if __name__ == "__main__":
    print(duration_pnl_proxy().tail())