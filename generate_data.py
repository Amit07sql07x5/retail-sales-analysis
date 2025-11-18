# generate_data.py - Retail Sales Data Generator (10,000 rows)
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime, timedelta
import os

print("Generating 10,000 realistic retail sales records...")

# Settings
np.random.seed(42)  # reproducible results
n = 10000
start_date = datetime(2020, 1, 1)
end_date = datetime(2025, 12, 31)

# Generate random dates
dates = [start_date + timedelta(days=np.random.randint(0, (end_date - start_date).days)) 
         for _ in range(n)]

# Create realistic data
data = {
    'Date': dates,
    'StoreID': np.random.randint(1, 51, n),
    'ProductID': np.random.randint(1001, 1501, n),
    'Category': np.random.choice(['Electronics', 'Clothing', 'Food', 'Books'], n, p=[0.3, 0.3, 0.2, 0.2]),
    'Quantity': np.random.randint(1, 10, n),
    'UnitPrice': np.round(np.random.uniform(5.0, 200.0, n), 2),
    'CustomerSegment': np.random.choice(['VIP', 'Regular', 'New'], n, p=[0.2, 0.6, 0.2])
}

df = pd.DataFrame(data)
df['TotalSales'] = df['Quantity'] * df['UnitPrice']
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')

# Create data folder
os.makedirs("data", exist_ok=True)

# Save as CSV (for Excel & Power BI)
df.to_csv("data/raw_sales.csv", index=False)
print("CSV created: data/raw_sales.csv")

# Save as SQLite DB (for SQL queries)
conn = sqlite3.connect("data/sales_data.db")
df.to_sql("sales", conn, if_exists="replace", index=False)
conn.close()
print("SQLite DB created: data/sales_data.db")

print("\nData generation complete! Ready for SQL, Excel, Python & Power BI")