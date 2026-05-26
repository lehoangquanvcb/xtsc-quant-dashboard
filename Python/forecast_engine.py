from feature_engineering import build_macro_features

def simple_rule_forecast():
    df = build_macro_features()
    latest = df.dropna().iloc[-1]
    forecast_10y = 0.35*latest["cpi_yoy_pct"] + 0.15*latest["usd_vnd"]/10000 + 0.50*latest["on_rate_pct"]
    if forecast_10y > 4.5:
        rec = "Shorten duration"
    elif latest["on_policy_spread_pct"] < -1.0:
        rec = "Extend duration selectively"
    else:
        rec = "Neutral"
    return {
        "date": str(latest["date"].date()),
        "forecast_10y_yield_pct": round(float(forecast_10y), 2),
        "recommendation": rec
    }

if __name__ == "__main__":
    print(simple_rule_forecast())