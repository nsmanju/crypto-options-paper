# greeks.py - Fetch live Greeks via raw API
# Key insight: raw['greeks']['delta'] field
from connection import get_exchange

def fetch_greeks(ex, market_id):
    raw = ex.publicGetTicker({'instrument_name': market_id})
    if isinstance(raw, list) and raw: raw = raw[0]
    if isinstance(raw, dict) and 'result' in raw: raw = raw['result']
    g = raw.get('greeks', {}) or {}
    return {
        'mark_price': raw.get('mark_price'),
        'mark_iv': raw.get('mark_iv'),
        'delta': g.get('delta'),
        'gamma': g.get('gamma'),
        'vega': g.get('vega'),
        'theta': g.get('theta'),
    }

ex = get_exchange()
print("Your Top 5 + explanations:\n")

try:
    with open('my_top5.txt') as f:
        top5 = [l.strip() for l in f]
except FileNotFoundError:
    print("Run find_top5.py first!")
    exit()

for sym in top5:
    market_id = ex.markets[sym]['id']
    g = fetch_greeks(ex, market_id)
    d = g['delta'] or 0
    tag = "OTM lottery" if abs(d)<0.2 else "ATM balanced" if abs(d)<0.7 else "Deep ITM"
    direction = "Call" if d>0 else "Put"
    print(f"{market_id}")
    print(f" Price {g['mark_price']} IV {g['mark_iv']}%")
    print(f" Delta {d:.5f} -> {tag} {direction} - {abs(d)*100:.0f}% copy")
    print(f" Gamma {g['gamma']} Theta {g['theta']}/day Vega {g['vega']}\n")
