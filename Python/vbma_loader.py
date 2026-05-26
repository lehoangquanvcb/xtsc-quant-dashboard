import pandas as pd

df = pd.DataFrame(columns=[
    "date",
    "tenor",
    "yield_pct"
])

df.to_csv("../Data/YieldCurve/vbma_curve_real.csv", index=False)

print("VBMA curve template created")