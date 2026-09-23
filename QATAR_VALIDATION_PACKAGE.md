# DebtLoop — Qatar START Validation Package

## Purpose

This document tracks the evidence required to turn the current working PoC into a credible START-stage application.

The current product already has a working circular-debt detection and multilateral-netting PoC. The next gap is **market validation**, not more speculative features.

## Current readiness

### Working evidence already available

- [x] Public interactive PoC
- [x] Reproducible 3-company circular-debt example
- [x] Circular-debt detection engine
- [x] Before/after netting calculation
- [x] Automated tests
- [x] Technology direction / roadmap draft
- [x] Initial business-model hypotheses
- [x] Initial Qatar / GCC expansion thesis

### Evidence still needed before submission

- [ ] 5–10 structured customer interviews
- [ ] Clear choice of first customer segment
- [ ] At least 2 written pilot-interest statements / LOIs
- [ ] Founder CV in English
- [ ] Technical lead / CTO or documented technical delivery partner
- [ ] 18–24 month hiring and operating plan
- [ ] 3-year financial model
- [ ] Funding request linked to milestones
- [ ] Qatar legal/accounting validation plan
- [ ] 60–120 second demo video

## First validation target

Do not interview “everyone.”

Start with one segment where circular receivables/payables are plausible:

1. distributors / wholesalers;
2. construction / subcontractor ecosystems;
3. B2B marketplaces;
4. accounting / ERP providers;
5. SME-focused financial institutions.

The objective of interviews is not to sell the product. It is to test whether the problem is frequent, costly, measurable, and important enough to pay for.

## Interview script

Use the same questions in every interview so results can be compared.

1. Does your company regularly have both accounts receivable and accounts payable at the same time?
2. Roughly how large are those balances in a typical month?
3. How often do late incoming payments delay your own outgoing payments?
4. Do you currently use bilateral set-off / netting with counterparties?
5. Have you ever tried to identify multi-company chains where several obligations could be offset together?
6. What is the biggest obstacle: legal approval, counterparty coordination, accounting, data availability, trust, or something else?
7. If software automatically identified a valid circular-netting opportunity, who inside your company would approve it?
8. What evidence or documentation would you require before approving a netting proposal?
9. Would you test this in a controlled pilot using a limited set of counterparties?
10. If a pilot reduced gross outstanding obligations or shortened settlement time, what pricing model would be easier to accept: subscription, success fee, enterprise/API fee, or another model?

## Interview evidence log

For each interview record:

- date;
- company / sector;
- respondent role;
- approximate company size;
- answers to all 10 questions;
- strongest pain point;
- objections;
- whether they agreed to a pilot discussion;
- whether they agreed to provide a written statement of interest.

Do not publish confidential interview details in the public repository. Keep identifying information in a private working document; only aggregate findings should be published.

## Minimum validation threshold before QDB submission

Recommended internal threshold:

- 5 completed interviews minimum;
- at least 3 respondents confirm that delayed receivables materially affect outgoing payments or working capital;
- at least 2 respondents agree the concept is worth piloting;
- at least 2 written expressions of interest / LOIs;
- one clearly selected initial customer segment;
- one pricing hypothesis supported by interview feedback.

These thresholds are DebtLoop's own application-readiness targets, not official QDB rules.

## Pilot-interest / LOI template

**Subject: Non-binding expression of interest in a DebtLoop pilot**

[Company name] confirms its interest in exploring a controlled pilot of DebtLoop, a B2B technology platform designed to identify circular obligations and calculate multilateral netting opportunities.

The proposed pilot would be limited in scope and would focus on evaluating:

- the ability to identify relevant circular obligations;
- the potential reduction in gross outstanding obligations;
- workflow requirements for finance/accounting approval;
- legal, accounting and data requirements for a production implementation.

This expression of interest is non-binding and does not create any payment, investment, exclusivity, or deployment obligation.

Company:  
Name / title:  
Date:  
Signature / email confirmation:

## Demo video outline

Target length: 60–120 seconds.

1. Problem: three companies are waiting for cash from each other.
2. Open the live DebtLoop demo.
3. Show A → B $100k, B → C $80k, C → A $70k.
4. Click **Detect & Calculate**.
5. Show gross obligations $250k → $40k.
6. Explain that the PoC finds the cycle and calculates a proposal; it does not move money.
7. End with the Qatar plan: controlled B2B pilots, legal/accounting validation, then GCC expansion.

## Founder / team evidence

Prepare:

- 1-page English founder CV;
- previous entrepreneurship / B2B / sales experience;
- product ownership role;
- technical delivery structure;
- future CTO / engineering hiring plan.

The application should not imply that a full engineering team already exists if it does not.

## Funding model to build next

The final ask must be tied to milestones rather than merely requesting the program maximum.

Budget lines to model:

- engineering;
- product / UX;
- security;
- legal and accounting review;
- Qatar company setup and operations;
- pilot implementation;
- sales / partnerships;
- cloud / infrastructure;
- contingency.

## Next milestone

**Customer validation sprint:** complete the first 5 structured interviews and obtain at least 2 pilot-interest statements.
