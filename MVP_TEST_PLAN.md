# DebtLoop PoC — MVP Test Plan

## Goal

Prove that the production bot code can detect and calculate a real circular-debt scenario, not only a hard-coded demo.

## Automated checks

These are already included in the repository:

- three-company cycle;
- no-cycle case;
- cycle embedded inside a longer path.

GitHub Actions runs the tests on pushes to `main`.

## Human check A — instant demo

After the Telegram bot is running with the latest code:

1. Open the DebtLoop bot.
2. Send `/start`.
3. Send `/demo`.
4. Confirm that the bot shows:
   - $250,000 gross obligations before;
   - $70,000 maximum netting per link;
   - $40,000 gross obligations after;
   - $210,000 debt eliminated.

This check uses the same netting engine as the live `/netting` command.

## Human check B — live three-account scenario

This requires three Telegram accounts with usernames.

1. Account A creates: `/owe @AccountB 100000`
2. Account B confirms the returned debt ID.
3. Account B creates: `/owe @AccountC 80000`
4. Account C confirms the returned debt ID.
5. Account C creates: `/owe @AccountA 70000`
6. Account A confirms the returned debt ID.
7. Any account sends `/netting`.

Expected result:

- the cycle A → B → C → A is detected;
- netting amount = 70,000;
- residual obligations = 30,000 / 10,000 / 0;
- gross obligations fall from 250,000 to 40,000.

## What this proves

This demonstrates:

- actual user-created obligations;
- participant confirmation;
- graph cycle detection;
- deterministic multilateral netting calculation.

## What this does not yet prove

It does not prove:

- legal enforceability;
- accounting treatment;
- willingness of businesses to adopt;
- secure production deployment;
- automated settlement;
- scalability across large enterprise graphs.

Those become the next validation stages.
