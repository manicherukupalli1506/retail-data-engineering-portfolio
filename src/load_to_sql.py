
import pandas as pd
import sqlite3
#
# Load cleaned retail sales data
df = pd.read_csv("data/cleaned_retail_sales.csv")

# Connect to SQLite database
conn = sqlite3.connect("data/retail_sales.db")

# Remove duplicate records within the incoming dataset
original_count = len(df)

df = df.drop_duplicates()

print("Duplicate records removed:", original_count - len(df))
 # Check existing records in SQLite
table_exists = conn.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='retail_sales'"
).fetchone()

if table_exists:
    existing_ids = pd.read_sql_query(
        "SELECT order_id FROM retail_sales", conn
    )["order_id"]

    df = df[~df["order_id"].isin(existing_ids)]

print("New records to insert:", len(df))
# Enforce unique order IDs in SQLite
if table_exists:
    conn.execute(
        "CREATE UNIQUE INDEX IF NOT EXISTS idx_order_id ON retail_sales(order_id)"
    )
# Load data into SQL table
df.to_sql(
    "retail_sales",
    conn,
    if_exists="append",
    index=False
)

print("Data loaded into SQLite successfully!")

# Verify the number of records
query = "SELECT COUNT(*) FROM retail_sales"

result = pd.read_sql_query(query, conn)

print("Total Records:", result.iloc[0, 0])

# Close database connection
conn.close()
