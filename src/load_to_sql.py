
import pandas as pd
import sqlite3

# Load cleaned retail sales data
df = pd.read_csv("data/cleaned_retail_sales.csv")

# Connect to SQLite database
conn = sqlite3.connect("data/retail_sales.db")

# Load data into SQL table
df.to_sql(
    "retail_sales",
    conn,
    if_exists="replace",
    index=False
)

print("Data loaded into SQLite successfully!")

# Verify the number of records
query = "SELECT COUNT(*) FROM retail_sales"

result = pd.read_sql_query(query, conn)

print("Total Records:", result.iloc[0, 0])

# Close database connection
conn.close()
