# Retail Demand Forecasting & Replenishment Engine

A Python-based inventory decision intelligence system designed to forecast retail demand, detect stockout and overstock risk, and generate data-backed replenishment recommendations for operational planning.

## Product Thesis

Retail inventory decisions often fail because organizations operate with fragmented demand visibility, delayed replenishment responses, and limited operational forecasting confidence.

This project explores how structured analytics and workflow automation can improve inventory decision-making through demand forecasting, inventory risk intelligence, replenishment policy automation, and impact simulation.

Rather than functioning as a one-off analytics exercise, the system is intentionally designed as an operational decision-support product simulating how internal retail planning teams could use data-driven workflow tooling to improve service levels while controlling inventory costs.

---

## Core Product Capabilities

### Demand Forecasting Intelligence

Forecasts retail demand at SKU-store level using structured forecasting workflows.

Capabilities include:

- demand trend analysis
- seasonality detection
- promo / holiday demand impact analysis
- baseline forecasting models
- comparative forecast performance evaluation
- forecast accuracy measurement (MAPE / WAPE)

Designed to improve planning confidence for near-term inventory decisions.

---

### Inventory Risk Intelligence

Identifies operational inventory risk zones including:

- projected stockout risk
- overstock risk
- inventory health classification
- days of inventory coverage analysis
- stockout exposure visibility
- lost sales proxy estimation

Supports proactive intervention rather than reactive inventory firefighting.

---

### Replenishment Decision Engine

Implements replenishment planning logic using inventory policy principles.

Includes:

- safety stock calculation
- reorder point computation
- lead-time-aware replenishment logic
- recommended reorder quantity generation
- service-level-aware inventory planning
- constraint-aware replenishment decisioning

Simulates operational planning workflows used by retail inventory teams.

---

### ETL & Data Engineering Layer

Built reproducible Python ETL workflows for structured operational data preparation.

Capabilities:

- multi-source data ingestion
- missing data handling
- duplicate resolution
- outlier detection
- schema normalization
- curated dataset generation

Generated outputs include:

- fact_sales_store_sku_daily
- fact_inventory_store_sku_daily
- replenishment_inputs_store_sku

---

### Executive Decision Support

Produces business-facing outputs for inventory planning and leadership visibility including:

- inventory risk prioritization
- replenishment planning recommendations
- operational KPI tracking
- impact estimation scenarios
- decision-ready business summaries

---

## Product Architecture

Designed as a modular analytics decision-support system.

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
