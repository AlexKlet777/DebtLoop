# DebtLoop

**B2B FinTech infrastructure for circular-debt detection and multilateral netting.**

DebtLoop identifies closed chains of obligations between companies and calculates how much debt can be offset without requiring each participant to move the full gross amount of cash.

## Why it matters

SMEs can be simultaneously creditors and debtors. When payment chains become circular, liquidity can remain trapped even though part of the obligations could be offset. DebtLoop models obligations as a directed graph, detects cycles, and proposes a mathematically consistent multilateral netting amount.

## Proof of Concept status

The current PoC includes:

- debt creation and bilateral confirmation in a Telegram prototype;
- persistent debt records;
- circular-debt detection;
- automatic calculation of the maximum equal offset around a detected cycle;
- before/after obligation calculation;
- a built-in B2B demo command;
- automated unit tests for the core netting engine.

**Important:** the current PoC calculates and proposes netting. It does not yet execute legal settlement, move funds, or replace accounting/ERP systems.

## Demo scenario

Input obligations:

- Company A → Company B: **$100,000**
- Company B → Company C: **$80,000**
- Company C → Company A: **$70,000**

DebtLoop detects the cycle and calculates:

- maximum netting per link: **$70,000**
- gross obligations before: **$250,000**
- residual obligations after: **$40,000**
- gross debt eliminated from the cycle: **$210,000**

Residual obligations:

- Company A → Company B: $30,000
- Company B → Company C: $10,000
- Company C → Company A: $0

## Telegram commands

- `/owe @username amount` — create a debt record;
- `/confirm ID` — confirm a debt;
- `/reject ID` — reject a debt;
- `/paid ID` — mark a confirmed debt as paid;
- `/debts` — show debts you owe;
- `/credits` — show debts owed to you;
- `/netting` — detect a circular debt and calculate a netting proposal;
- `/demo` — show the built-in B2B PoC scenario.

## Core files

- `main.py` — Telegram prototype;
- `netting.py` — standalone circular-debt detection and netting engine;
- `test_netting.py` — unit tests;
- `demo_netting.py` — command-line demo;
- `.github/workflows/netting-tests.yml` — automated test workflow;
- `QATAR_START_APPLICATION.md` — working draft for the Startup Qatar / QDB application;
- `MVP_TEST_PLAN.md` — validation checklist for the PoC.

## Run the algorithm demo locally

```bash
python demo_netting.py
```

## Run tests

```bash
python -m unittest -v test_netting.py
```

## Run the Telegram prototype

Install dependencies:

```bash
pip install -r requirements.txt
```

Set the Telegram bot token as environment variable `TOKEN`, then:

```bash
python main.py
```

## Product direction

The intended product is a B2B platform, not merely a Telegram bot. The Telegram interface is currently used as a lightweight PoC. Planned product development includes:

1. B2B web application with company accounts and role-based access;
2. invoice / obligation import;
3. multi-cycle optimization across larger graphs;
4. proposal approval by all affected parties;
5. audit trail and settlement documentation;
6. ERP/accounting integrations and APIs;
7. jurisdiction-specific legal and compliance workflows;
8. analytics showing liquidity unlocked and obligations reduced.

## Qatar / GCC thesis

DebtLoop is being prepared as a B2B FinTech / working-capital infrastructure project for a potential Qatar launch and later GCC expansion. Before commercial deployment, the legal enforceability of multilateral netting, accounting treatment, data requirements, and any regulated activities must be validated with qualified local advisers and partners.

## Founder

Created by **Alexander Kletsov**.  
GitHub: **AlexKlet777**  
Telegram: **@alexanderkletsov**

Original project authorship was recorded in this repository on 2025-04-23.
