from vnstock import *
import pandas as pd
from pathlib import Path

OUT = Path("../Data/Market")
OUT.mkdir(parents=True, exist_ok=True)

def download_vnindex():
    try:
        df = stock_historical_data(
            symbol='VNINDEX',
            start_date='2018-01-01',
            end_date='2026-12-31',
            resolution='1D',
            type='index'
        )
        df.to_csv(OUT / "vnindex_daily_real.csv", index=False)
        print("VNINDEX downloaded")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    download_vnindex()