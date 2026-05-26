from feature_engineering import build_macro_features

def classify_regime(row):
    if row["usd_vnd_mom_pct"] > 1.5:
        return "FX_STRESS"
    if row["cpi_yoy_pct"] > 5.0 and row["on_policy_spread_pct"] > 0:
        return "INFLATION_TIGHTENING"
    if row["on_policy_spread_pct"] < -1.0:
        return "LIQUIDITY_EASING"
    if row["liquidity_stress_score"] >= 2:
        return "MULTI_FACTOR_STRESS"
    return "NORMAL"

def classify_history():
    df = build_macro_features()
    df["model_regime"] = df.apply(classify_regime, axis=1)
    return df[["date","regime","model_regime","liquidity_stress_score"]]

if __name__ == "__main__":
    print(classify_history().tail(12))