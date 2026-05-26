import pandas as pd

df = pd.DataFrame(columns=["date","foreign_flow_bn_vnd"])
df.to_csv("../Data/Market/foreign_flow_real.csv", index=False)

print("Foreign flow template created")