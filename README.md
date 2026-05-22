# Retail Demand Forecasting & Replenishment Engine

Inventory decision intelligence system for retail demand forecasting, stock risk detection, and replenishment planning.

## Why this exists

Retail inventory teams frequently operate with delayed demand visibility, fragmented inventory signals, and reactive replenishment decisions.

The operational consequences are predictable:

- stockouts → lost sales + poor customer experience
- overstock → tied-up working capital + holding cost inefficiency
- weak forecasting → unreliable planning decisions

This project explores how structured analytics workflows can improve inventory decision quality through demand forecasting, risk intelligence, and automated replenishment recommendations.

The objective is not reporting.

The objective is operational decision support.

---

## Product Scope

The system provides workflow support across four operational decision layers:

1. Demand forecasting
2. Inventory risk detection
3. Replenishment planning
4. Business impact estimation

---

## Core Capabilities

### Demand Forecasting

Forecasts near-term SKU-store demand using structured forecasting workflows.

Includes:

- trend analysis
- seasonality analysis
- promo / holiday demand impact
- baseline forecasting models
- comparative model evaluation
- forecast accuracy measurement (MAPE / WAPE)

Supports forward inventory planning decisions.

---

### Inventory Risk Intelligence

Detects operational inventory risk before execution failure.

Risk classifications include:

- stockout risk
- overstock risk
- healthy inventory zone

Supporting intelligence:

- days of inventory coverage
- lost sales exposure proxy
- inventory health visibility
- top risk SKU prioritization

---

### Replenishment Decision Engine

Implements inventory planning logic using standard replenishment policy design.

Includes:

- safety stock computation
- reorder point calculation
- lead-time-aware planning
- recommended reorder quantity generation
- service-level-based decision logic
- replenishment constraint awareness

Built to simulate practical operational inventory workflows.

---

### Data Engineering Pipeline

Reproducible ETL workflows for operational retail data preparation.

Pipeline responsibilities:

- multi-source ingestion
- data cleaning
- missing value handling
- duplicate resolution
- outlier detection
- schema normalization
- curated analytics dataset generation

Generated outputs:

- fact_sales_store_sku_daily
- fact_inventory_store_sku_daily
- replenishment_inputs_store_sku

---

### Executive Decision Support

Business-facing outputs include:

- inventory risk prioritization
- replenishment recommendations
- KPI visibility
- impact estimation scenarios
- decision-ready summaries

---

## System Architecture

```text
retail-demand-forecasting-replenishment-engine/
├── etl/
│   └── etl_pipeline.py
├── analysis/
│   └── analysis.ipynb
├── dashboard/
├── final_story/
├── data/
└── README.md
