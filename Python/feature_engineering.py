import pandas as pd
from load_data import load_macro_monthly

def build_macro_features():
    df = load_macro_monthly().sort_values("date").copy()
    df["usd_vnd_mom_pct"] = df["usd_vnd"].pct_change() * 100
    df["on_policy_spread_pct"] = df["on_rate_pct"] - df["policy_rate_pct"]
    df["curve_proxy_10y_policy_spread_pct"] = df["vn_10y_yield_pct"] - df["policy_rate_pct"]
    df["liquidity_stress_score"] = (
        (df["on_policy_spread_pct"] > 0.5).astype(int)
        + (df["usd_vnd_mom_pct"] > 1.0).astype(int)
        + (df["cpi_yoy_pct"] > 5.0).astype(int)
        + (df["vn_10y_yield_pct"] > 5.0).astype(int)
    )
    return df

if __name__ == "__main__":
    print(build_macro_features().tail())