# Crypto Options Paper Trading - Deribit Testnet

Learn BTC options Greeks (Delta, Gamma, Theta, Vega) with safe paper trading. No real money.

From zero to +33% profitable trade in 2 days.

## Folder Structure
```
crypto-options-paper/
├── src/
│   ├── connection.py            # Safe testnet connection (keys from .env)
│   ├── find_top5.py             # Liquidity filter -> Top 5 options
│   ├── greeks.py                # Live Greeks via raw['greeks']['delta']
│   ├── portfolio_with_greeks.py # PnL + Delta dashboard
│   └── rules_table.py           # Delta rules table in terminal
├── docs/
│   ├── DELTA_RULES.md           # Markdown cheat-sheet
│   └── DELTA_RULES.html         # Beautiful HTML version
├── examples/
│   └── .env.example             # Template - copy to .env
├── requirements.txt
├── .gitignore                   # Blocks .env from GitHub
└── README.md
```

## Quick Start (Safe)

1. **Clone & Setup**
```bash
git clone <your-repo>
cd crypto-options-paper
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. **Add Testnet Keys (never commit!)**
```bash
cp examples/.env.example .env
# Edit .env with your testnet keys from https://test.deribit.com/account/API
```

3. **Run Dashboard**
```bash
python3 src/find_top5.py
python3 src/greeks.py
python3 src/portfolio_with_greeks.py
```

## Work Accomplished

### 1. Deribit Connection
- Sandbox mode, ccxt library, raw API for Greeks
- Key learning: `publicGetTicker({'instrument_name': id})['result']['greeks']['delta']`

### 2. Trading Logic
- Liquidity filter (volume>5)
- 5 Delta Rules: Rule 2 (0.40-0.70) Winner Zone = balanced scalp

### 3. Execution
- Trade #1: BTC-28AUG26-64000-C 0.015 -> 0.02 = +33.3% overnight
- BTC move $62,957 -> $64,352 x Delta 0.55

### 4. Safeguards
- Testnet only, 0.1 contract sizing, Theta warnings, flat check

### 5. Dashboard
- PnL + Delta together, HTML cheat-sheet

## Safeguards

- `.gitignore` blocks `.env` - credentials never pushed
- `set_sandbox_mode(True)` - testnet only
- No real money, paper trading only

## Example Output

```
BTC-28AUG26-64000-C
 Price 0.0197 IV 27% Delta 0.55 -> ATM Call - 56% copy
```

## License
MIT License with educational disclaimer - see LICENSE file.
