import pandas as pd

def validate_data(df):
    print("Starting Data Validation...")

    # Check missing values
    print("Missing Values:")
    print(df.isnull().sum())

    # Check duplicate records
    print("Duplicate Records:")
    print(df.duplicated().sum())

    # Check dataset information
    print("Total Rows:", len(df))
    print("Total Columns:", len(df.columns))

    print("Data Validation Completed!")
# Load retail sales dataset
df = pd.read_csv("data/retail_sales.csv")

# Run data validation
validate_data(df)
