# Crypto Options Paper Trading Lab
### Why Paper Trade in 2026? BTC Enters the Monetary System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![LinkedIn Carousel](https://img.shields.io/badge/Carousel-World%20Bank%20Style-0057B8)](#-linkedin-carousel)

> **TL;DR:** Japan reclassified crypto as financial assets (July 2026). Hong Kong's HKMA runs Project e-HKD+ with 21 banks. Governments hold 460,000 BTC (2.3% supply). Paper trading = safe simulation for this new monetary regime.

---

## Macro Context 2026 - Quantified

| Jurisdiction | 2026 Status | Source |
|---|---|---|
| **Japan** | Crypto = Financial Assets under FIEA | Nikkei, FSA |
| **Hong Kong** | Project e-HKD+ Phase 2: 21 banks, 11 use cases | HKMA.gov |
| **Hong Kong** | First spot BTC/ETH ETFs Apr 2024, 11 VATP licensed | SFC/HKMA |
| **USA** | Strategic Bitcoin Reserve 198k BTC | White House |
| **Global** | 32 countries → 45 est, 460k BTC gov-held | EORMC |

---

## What This Repo Does

Paper trading lab: Delta 0.70+ = high prob, Top5 liquidity filter, +33% paper P&L testnet

Modules: find_top5.py, greeks.py, rules_table.py, macro_analysis.py

## LinkedIn Carousel
World Bank style - see docs/carousel/ - 6 slides

Post template: BTC financial asset, Japan law, HKMA 21 banks, 460k BTC, github.com/nsmanju/crypto-options-paper #HKMA #eHKD

## Quick Start
pip install -r requirements.txt
python src/paper_trading.py --delta 0.7 --top5
python src/macro_analysis.py

## Python Quantified
USA 198k, UK 61k, Bhutan 13k, El Salvador 6.3k, HK 21 banks
Global: 460k BTC = 2.3% supply

See docs/MACRO_CONTEXT.md for full research
