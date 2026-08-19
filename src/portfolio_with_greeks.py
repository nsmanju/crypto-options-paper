# portfolio_with_greeks.py - PnL + Delta dashboard
from connection import get_exchange

ex = get_exchange()
bal = ex.fetch_balance()
print(f"Balance: {bal['BTC']['total']} BTC\n")

positions = ex.fetch_positions()
for p in positions:
    if float(p['contracts'] or 0)==0: continue
    print(f"{p['symbol']} Size {p['contracts']} PnL {p['unrealizedPnl']}")

print("\nRun greeks.py for Delta explanations")
