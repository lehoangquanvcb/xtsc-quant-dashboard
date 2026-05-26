from forecast_engine import simple_rule_forecast
from regime_classifier import classify_history
from treasury_backtest import duration_pnl_proxy

print("XTSC Historical Quant Package")
print("Forecast:", simple_rule_forecast())
print("Latest regime:")
print(classify_history().tail(3))
print("Treasury P&L proxy:")
print(duration_pnl_proxy().tail(3))