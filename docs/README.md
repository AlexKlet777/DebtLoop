# DebtLoop public demo

This folder contains a static browser-based demo of the DebtLoop circular-debt detection and multilateral netting concept.

It requires no backend and no Telegram bot server. The demo can be published with GitHub Pages and used in investor or accelerator applications as a live proof of concept.

The current implementation:

- accepts a set of B2B obligations;
- detects a circular chain;
- calculates the maximum equal netting amount;
- displays gross obligations before and after netting;
- does not modify real balances or execute settlement.
