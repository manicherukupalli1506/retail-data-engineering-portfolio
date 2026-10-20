
import pandas as pd

# Load retail sales data
df = pd.read_csv("data/retail_sales.csv")

print("Starting Data Cleaning...")

# Remove duplicate records
df = df.drop_duplicates()

# Remove records with missing quantities
df = df.dropna(subset=["quantity"])

# Calculate total sales for each record
df["total_sales"] = df["quantity"] * df["price"]

# Save cleaned dataset
df.to_csv("data/cleaned_retail_sales.csv", index=False)

print("Data Cleaning Completed!")
print("Total Cleaned Records:", len(df))
