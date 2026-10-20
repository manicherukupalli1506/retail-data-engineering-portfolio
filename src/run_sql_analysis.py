
import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("data/retail_sales.db")

# Read SQL queries from file
with open("sql/sales_analysis.sql", "r") as file:
    sql_script = file.read()

# Separate SQL queries
queries = sql_script.split(";")

# Execute each query
for query in queries:
    if query.strip():
        result = pd.read_sql_query(query, conn)
        print("\nSQL Query Result:")
        print(result.to_string(index=False))

# Close database connection
conn.close()

print("\nSQL Analysis Completed!")
