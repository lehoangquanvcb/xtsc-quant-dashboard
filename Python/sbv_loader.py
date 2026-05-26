import pandas as pd

df = pd.DataFrame(columns=[
    "date",
    "on_rate_pct",
    "omo_outstanding_bn",
    "refinancing_bn"
])

df.to_csv("../Data/Macro/sbv_liquidity_real.csv", index=False)

print("SBV liquidity template created")