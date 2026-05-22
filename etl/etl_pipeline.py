import pandas as pd
import numpy as np
import os

print("Starting ETL Pipeline...")

# -----------------------------
# PATH SETUP
# -----------------------------

BASE_PATH = "../"
RAW_PATH = os.path.join(BASE_PATH, "data_raw")
OUTPUT_PATH = os.path.join(BASE_PATH, "data")

os.makedirs(OUTPUT_PATH, exist_ok=True)

# -----------------------------
# LOAD DATA
# -----------------------------

print("Loading datasets...")

sales = pd.read_csv(os.path.join(RAW_PATH, "sales_daily.csv"))
inventory = pd.read_csv(os.path.join(RAW_PATH, "inventory_daily.csv"))
calendar = pd.read_csv(os.path.join(RAW_PATH, "calendar.csv"))
stores = pd.read_csv(os.path.join(RAW_PATH, "stores.csv"))
purchase_orders = pd.read_csv(os.path.join(RAW_PATH, "purchase_orders.csv"))

print("Datasets loaded successfully.")

# -----------------------------
# STANDARDIZE COLUMN NAMES
# -----------------------------

sales.columns = sales.columns.str.lower()
inventory.columns = inventory.columns.str.lower()
calendar.columns = calendar.columns.str.lower()
stores.columns = stores.columns.str.lower()
purchase_orders.columns = purchase_orders.columns.str.lower()

# -----------------------------
# DATE CONVERSION
# -----------------------------

if 'date' in sales.columns:
    sales['date'] = pd.to_datetime(sales['date'])

if 'date' in inventory.columns:
    inventory['date'] = pd.to_datetime(inventory['date'])

if 'date' in calendar.columns:
    calendar['date'] = pd.to_datetime(calendar['date'])

# -----------------------------
# MERGE CALENDAR
# -----------------------------

print("Merging calendar features...")

sales_master = sales.copy()

if 'date' in calendar.columns:
    sales_master = sales_master.merge(calendar, on="date", how="left")

# -----------------------------
# CREATE DAY OF WEEK FEATURE
# -----------------------------

if 'date' in sales_master.columns:
    sales_master['day_of_week'] = sales_master['date'].dt.dayofweek
else:
    sales_master['day_of_week'] = 0

# -----------------------------
# PROMOTION FLAG
# -----------------------------

if 'promo_flag' not in sales_master.columns:
    sales_master['promo_flag'] = 0

# -----------------------------
# HOLIDAY FLAG
# -----------------------------

holiday_columns = ['holiday_flag','is_holiday','holiday']

holiday_col = None

for col in holiday_columns:
    if col in sales_master.columns:
        holiday_col = col
        break

if holiday_col:
    sales_master['holiday_flag'] = sales_master[holiday_col]
else:
    sales_master['holiday_flag'] = 0

# -----------------------------
# REQUIRED SALES COLUMNS
# -----------------------------

required_cols = ['date','store_id','sku_id','units_sold','revenue']

for col in required_cols:
    if col not in sales_master.columns:
        sales_master[col] = 0

# -----------------------------
# FACT SALES TABLE
# -----------------------------

fact_sales = sales_master[
    [
        'date',
        'store_id',
        'sku_id',
        'units_sold',
        'revenue',
        'promo_flag',
        'holiday_flag',
        'day_of_week'
    ]
]

# -----------------------------
# INVENTORY PROCESSING
# -----------------------------

print("Processing inventory...")

inventory_master = inventory.copy()

if 'on_hand_units' not in inventory_master.columns:
    inventory_master['on_hand_units'] = 0

inventory_master['stockout_flag'] = np.where(
    inventory_master['on_hand_units'] <= 0,
    1,
    0
)

inventory_master['days_of_cover'] = inventory_master['on_hand_units'] / 1

fact_inventory = inventory_master[
    [
        'date',
        'store_id',
        'sku_id',
        'on_hand_units',
        'stockout_flag',
        'days_of_cover'
    ]
]

# -----------------------------
# REPLENISHMENT CALCULATIONS
# -----------------------------

print("Calculating replenishment metrics...")

demand_stats = fact_sales.groupby(
    ['store_id','sku_id']
).agg(
    avg_daily_demand=('units_sold','mean'),
    demand_std_dev=('units_sold','std')
).reset_index()

demand_stats['lead_time_days'] = 7

demand_stats['safety_stock'] = (
    1.65 *
    demand_stats['demand_std_dev'] *
    np.sqrt(demand_stats['lead_time_days'])
)

demand_stats['reorder_point'] = (
    demand_stats['avg_daily_demand'] *
    demand_stats['lead_time_days']
) + demand_stats['safety_stock']

demand_stats['recommended_order_qty'] = (
    demand_stats['avg_daily_demand'] * 14
)

replenishment_inputs = demand_stats

# -----------------------------
# SAVE OUTPUT FILES
# -----------------------------

print("Saving output files...")

fact_sales.to_csv(
    os.path.join(OUTPUT_PATH,"fact_sales_store_sku_daily.csv"),
    index=False
)

fact_inventory.to_csv(
    os.path.join(OUTPUT_PATH,"fact_inventory_store_sku_daily.csv"),
    index=False
)

replenishment_inputs.to_csv(
    os.path.join(OUTPUT_PATH,"replenishment_inputs_store_sku.csv"),
    index=False
)

print("ETL Pipeline Completed Successfully!")