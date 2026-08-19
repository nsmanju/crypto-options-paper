# find_top5.py - Find Top 5 liquid BTC options
from connection import get_exchange

ex = get_exchange()

liquid = []
for m in ex.markets.values():
    if 'BTC' not in m['id'] or m['type'] != 'option':
        continue
    try:
        t = ex.fetch_ticker(m['symbol'])
        # Liquidity filter
        if t['baseVolume'] and t['baseVolume'] > 5:
            liquid.append((m['symbol'], t['baseVolume'], m['id']))
    except:
        continue

liquid.sort(key=lambda x: x[1], reverse=True)
top5 = liquid[:5]

print("Top 5 Liquid Options:")
for sym, vol, mid in top5:
    print(f" {mid} Vol:{vol:.1f}")

# Save for other scripts
with open('my_top5.txt','w') as f:
    for sym,_,_ in top5:
        f.write(sym+"\n")
