import pandas as pd
df = pd.DataFrame([
    {'Country':'El Salvador','BTC':6313},
    {'Country':'USA','BTC':198000},
    {'Country':'UK','BTC':61000},
    {'Country':'Bhutan','BTC':13000},
])
print(f"Total: {df['BTC'].sum():,} BTC")
print("Global 2025: 460k BTC = 2.3% supply")
df.to_csv('docs/crypto_reserves.csv', index=False)
