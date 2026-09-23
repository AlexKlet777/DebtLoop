# DebtLoop — Qatar START Application Working Draft

This document is an internal working draft for preparing a Startup Qatar / Qatar Development Bank START application. It deliberately separates current evidence from assumptions that still need validation.

## 1. Project name

**DebtLoop**

## 2. Category

Primary: **FinTech**  
Adjacent: **B2B SaaS**, **Supply Chain / Working Capital Technology**

## 3. One-line description

**DebtLoop is a B2B platform that detects circular obligations between companies and proposes multilateral netting, helping businesses reduce gross outstanding debt and unlock working capital without adding new borrowing.**

**Live PoC:** https://alexklet777.github.io/DebtLoop/

## 4. Problem

Businesses can be both debtors and creditors at the same time. In a network of companies, obligations may form circular chains. Each company may wait for incoming cash before paying the next company, leaving liquidity trapped even where part of the obligations can theoretically be offset.

Traditional accounting systems record bilateral obligations but generally do not search a wider network for multilateral circular-netting opportunities across independent companies.

## 5. Solution

DebtLoop represents confirmed obligations as a directed graph.

The platform:

1. receives or imports confirmed obligations;
2. detects closed debt cycles;
3. calculates the maximum netting amount that can be applied consistently across each detected cycle;
4. shows every affected participant the before/after position;
5. prepares a proposal for multi-party approval;
6. creates an auditable record of the approved netting event.

The current PoC implements steps 1–4. Approval workflow, legal settlement documentation, integrations, and production security are planned development milestones.

## 6. Current PoC

Implemented today:

- Telegram-based debt registration and confirmation;
- persistent debt storage;
- circular-debt detection algorithm;
- netting calculation engine;
- before/after obligation calculation;
- automated tests;
- reproducible B2B demo.

Reference demo:

- A owes B: $100,000
- B owes C: $80,000
- C owes A: $70,000

Result:

- $70,000 offset per link;
- gross obligations fall from $250,000 to $40,000;
- $210,000 of gross obligations are removed from the cycle.

This is a mathematical PoC. It is not yet a legally executed settlement product.

## 7. Technology

Current stack:

- Python;
- graph-based cycle detection;
- deterministic netting calculation;
- Telegram interface for PoC interaction;
- automated tests via GitHub Actions.

Planned architecture:

- secure B2B web application;
- relational obligation ledger;
- graph-processing service;
- approval / e-signature workflow;
- immutable audit logs;
- REST API;
- ERP and accounting-system integrations;
- role-based access and enterprise security;
- multi-cycle optimization for larger networks.

## 8. Business model hypothesis

To be validated during customer discovery.

Potential revenue models:

- recurring B2B SaaS subscription;
- enterprise/API subscription;
- transaction or success fee based on successfully approved netting volume;
- white-label/API licensing for financial institutions, accounting platforms or B2B marketplaces.

No model should be presented as validated until customer interviews and pilot discussions support it.

## 9. Initial target customers

Potential early adopters:

- SME networks with recurring B2B receivables/payables;
- distributors and supply-chain ecosystems;
- construction and subcontractor networks;
- B2B marketplaces;
- accounting / ERP platforms;
- financial institutions serving SMEs.

The first segment still needs to be selected through interviews and pilot validation.

## 10. Qatar / GCC launch thesis

Proposed approach:

- establish Qatar as the first regulated B2B pilot market;
- partner with local SME ecosystems, financial institutions, accounting providers or B2B platforms;
- validate local legal treatment of bilateral and multilateral set-off;
- run controlled pilots with real but limited participant networks;
- use Qatar as a base for GCC expansion after legal, accounting and commercial validation.

## 11. 18-month milestone draft

### Phase 1 — Product and validation
- production-grade web MVP;
- company accounts and permissions;
- obligation import;
- improved graph/netting engine;
- audit trail;
- first structured customer discovery interviews.

### Phase 2 — Qatar pilot readiness
- local legal and accounting review;
- data protection and security design;
- pilot agreements;
- approval workflow;
- first Qatar pilot participants.

### Phase 3 — Commercial pilots
- execute controlled B2B pilots;
- measure debt reduction, settlement time and working-capital impact;
- convert suitable pilots into paid contracts;
- build API / ERP integrations.

### Phase 4 — GCC scale
- repeatable onboarding;
- enterprise/API sales;
- expansion into selected GCC markets.

## 12. Evidence still required before final submission

The application will be materially stronger after obtaining:

- 5–10 structured interviews with CFOs / finance directors / business owners;
- at least 2 written expressions of interest or pilot LOIs;
- a committed technical lead / CTO or documented development partner;
- a Qatar legal opinion or at minimum a scoped legal review plan;
- a 3-year financial model;
- a clear funding request tied to milestones;
- founder and team CVs;
- a short PoC demo video;
- a defined first customer segment;
- measured assumptions for pricing and sales cycle.

## 13. Funding request structure

Do not frame the request as “we want the maximum available amount.”

Frame it as milestone financing:

**DebtLoop is seeking funding to build a production-grade B2B platform, complete Qatar legal and commercial validation, launch controlled pilots, secure first enterprise customers, and prepare for GCC expansion. Capital would be deployed against agreed product, pilot and commercial milestones.**

The exact requested amount and budget should be finalized only after the 18–24 month operating plan and hiring plan are built.

## 14. Core application message

**DebtLoop does not create new credit. It helps businesses use the structure of existing obligations more efficiently. By detecting circular debt chains and coordinating multilateral netting, the platform can reduce gross outstanding obligations, improve settlement efficiency and potentially release working capital that would otherwise remain trapped inside payment chains.**


## 15. QDB START criteria mapping

This section maps the application directly to the current Startup Qatar START eligibility language.

### Unmet market need
DebtLoop addresses the working-capital friction created when businesses are simultaneously debtors and creditors and payment chains become circular.

### Clear objective and execution plan
The objective is to turn the working PoC into a production-grade B2B platform, validate legal/accounting treatment in Qatar, run controlled pilots, and scale to GCC markets.

### Detailed technology roadmap
The roadmap includes secure company accounts, obligation import, graph-processing services, approval workflows, audit trails, APIs, ERP/accounting integrations and multi-cycle optimization.

### Validated concept
A working public PoC already detects circular obligations and calculates netting outcomes. Commercial validation is still in progress and is explicitly tracked in QATAR_VALIDATION_PACKAGE.md.

### Market readiness supported by research
This remains the most important pre-submission gap. Structured interviews and pilot-interest evidence are required before final submission.

### Robust business model and monetization strategy
Current hypotheses include B2B SaaS, enterprise/API pricing, success-based fees and white-label/API licensing. The final model will be selected after customer validation.

### Committed leadership with relevant experience
Founder profile and technical-delivery structure are being prepared separately. The final application should distinguish current team members from planned hires or external partners.

## 16. Evidence links

- Live PoC: https://alexklet777.github.io/DebtLoop/
- Source repository: https://github.com/AlexKlet777/DebtLoop
- Technical validation: MVP_TEST_PLAN.md
- Market validation plan: QATAR_VALIDATION_PACKAGE.md
