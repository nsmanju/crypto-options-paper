# Delta Rules - Options Strategy Cheat-Sheet
*Your Top 5 live mapping from 19-Aug-2026*

## Core Concept in Simple Words

- **Delta POSITIVE (+0.05 to +1.0) = CALL** -> You win when BTC goes UP
- **Delta NEGATIVE (-1.0 to -0.05) = PUT** -> You win when BTC goes DOWN
- **Bigger Delta = Short-term, balanced, scalp**
- **Smaller Delta = Long-term, lottery, HODL**

> You already used Rule #2 yesterday: BTC-28AUG26-64000-C Delta 0.56 -> +33% profit overnight!

---

## Rules Table

| Rule | Delta Range | Type | Simple Strategy | When to Use |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **+0.70 to +1.0** | **Deep ITM Call** | **SAFE CALL** - Like owning BTC. Moves 70-100% with BTC. Expensive, low risk, low reward. | Very bullish, want BTC exposure with leverage protection. |
| **2** | **+0.40 to +0.70** | **ATM Call** | **WINNER ZONE - Balanced Scalp!** BTC up $100 -> option up $40-$70. Good leverage, manageable Theta. | **Your sweet spot.** 1-3 day trade if you think BTC up. This was your +33% winner. |
| **3** | **+0.05 to +0.20** | **OTM Call Lottery** | **LOTTERY CALL** - Cheap, needs big BTC move. 5-20% copy. Low Theta (-6/day), High Vega. | Long-term bet BTC to $100k by Dec. Buy and HODL 3-4 months. |
| **4** | **-0.20 to -0.50** | **OTM Put** | **PUT OPPORTUNITY** - Bear bet! Moves OPPOSITE. BTC up $100 -> Put down $20-$50. | Think BTC will DROP. Good for hedge or bear scalp. |
| **5** | **-0.05 to -0.20** | **Far OTM Put** | **CRASH INSURANCE** - Black swan protection. Cheap, barely moves now. | Fear crash below $50k, want insurance. |

---

## Today's Top 5 Mapped (Live 19-Aug-2026, BTC ~64,262)

| Instrument | Price | Delta | IV | Theta/day | Maps To | Strategy Note |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **BTC-28AUG26-64000-C** | 0.0197 | **+0.55** | 27% | -59.8 | **Rule 2 WINNER** | ATM Call, 9 days left, 56% copy. Repeat of yesterday's +33% scalp. Best for learning. |
| **BTC-28AUG26-63000-P** | 0.0089 | **-0.31** | 27% | -54.4 | **Rule 4 PUT OPP** | Slight OTM Put. Profit if BTC <63k. Good to learn opposite PnL. |
| **BTC-25SEP26-54000-P** | 0.006 | **-0.088** | 43% | -19.3 | **Rule 5 INSURANCE** | Far OTM Put Sep, 37 days. Cheap crash lottery, barely moves. Skip for now. |
| **BTC-25DEC26-100000-C** | 0.0046 | **+0.05** | 40% | -6.3 | **Rule 3 LOTTERY CALL** | $100k Call Dec, 128 days. 5% copy, needs $35k rally. Long HODL. |
| **BTC-25DEC26-50000-P** | 0.0214 | **-0.13** | 46% | -15.2 | **Rule 5 INSURANCE** | $50k Put Dec, 128 days. Bear insurance, expensive due to fear premium. |

---

## Quick Decision Flowchart

```
Is Delta POSITIVE?
  YES -> CALL (BTC UP wins)
    Delta >0.5? -> Rule 1 or 2 -> SHORT-TERM SCALP (1-3 days)
    Delta <0.2? -> Rule 3 -> LONG-TERM LOTTERY (months)
  NO -> PUT (BTC DOWN wins)
    Delta -0.2 to -0.5? -> Rule 4 -> BEAR SCALP / HEDGE
    Delta -0.05 to -0.2? -> Rule 5 -> CRASH INSURANCE
```

## Key Greek Reminders

- **Theta:** Daily decay. Aug 28 options = -59/day (FAST!). Dec options = -6/day (SLOW). Don't hold Aug past 26th.
- **IV:** Implied Vol. 27% (Aug) vs 40-46% (Dec). Higher IV = market expects bigger move.
- **Vega:** IV sensitivity. Dec options have high Vega - jump on news even if BTC flat.

## Your Trade History

- **Trade #1:** 18-Aug: Bought BTC-28AUG26-64000-C @0.015 Delta 0.55 -> Sold @0.02 Delta 0.55 = +0.0005 BTC (+33.3%)
- **Reason:** BTC 62957->64352 (+1395) x Delta 0.55 = option up 0.005

---
*Generated from live Deribit testnet API: raw['greeks']['delta'] field*
