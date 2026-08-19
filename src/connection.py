# connection.py - Safe Deribit Testnet Connection
import os
from dotenv import load_dotenv
import ccxt
load_dotenv()

def get_exchange():
    """Returns ccxt Deribit exchange in sandbox mode.
    Keys loaded from .env - never hardcoded!
    """
    ex = ccxt.deribit({
        'apiKey': os.getenv('DERIBIT_CLIENT_ID'),
        'secret': os.getenv('DERIBIT_CLIENT_SECRET'),
    })
    ex.set_sandbox_mode(True)  # TESTNET ONLY
    ex.load_markets()
    return ex

if __name__ == '__main__':
    ex = get_exchange()
    print(f"Connected to Deribit testnet. Markets: {len(ex.markets)}")
    bal = ex.fetch_balance()
    print(f"BTC Balance: {bal['BTC']['total']}")
