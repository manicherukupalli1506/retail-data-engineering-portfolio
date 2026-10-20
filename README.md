# Retail Data Engineering Pipeline

An end-to-end retail data engineering project built using Microsoft Azure.

The project combines customer data from an API with product, store and transaction data from a SQL database. Azure Data Factory is used for data ingestion, Azure Data Lake Storage Gen2 is used for storage, and Azure Databricks with PySpark is used for data transformation.

## Architecture

```text
API + SQL Database
        ↓
Azure Data Factory
        ↓
ADLS Gen2
   Bronze Layer
        ↓
Azure Databricks
     PySpark
        ↓
   Silver Layer
(Cleaned + Joined Data)
        ↓
    Gold Layer
(Aggregated Data)
```

## Technologies

* Azure Data Factory
* Azure Data Lake Storage Gen2
* Azure Databricks
* Apache Spark / PySpark
* Delta Lake
* SQL

## Data Pipeline

### 1. Ingestion

Azure Data Factory ingests data from multiple sources:

* Customer data from an API in JSON format
* Product data from SQL
* Store data from SQL
* Transaction data from SQL

The ingested data is stored in the **Bronze** layer of ADLS Gen2.

### 2. Transformation

Azure Databricks reads the Bronze data using PySpark.

The transformations include:

* Data type conversion
* Selecting required columns
* Removing duplicate customers
* Joining customers, products, stores and transactions
* Creating a `total_amount` column
* Aggregating sales information

### 3. Silver Layer

The cleaned and joined dataset is written to ADLS Gen2 using **Delta Lake**.

The Silver dataset combines transaction information with customer, product and store information.

### 4. Gold Layer

The Silver data is aggregated to create business-level metrics including:

* Total quantity sold
* Total sales amount
* Number of transactions
* Average transaction value

The Gold data is also stored using Delta Lake.

## Project Structure

```text
retail-data-engineering-azure/
│
├── README.md
│
├── architecture/
│   └── retail_architecture.png
│
├── screenshots/
│   ├── adf_pipeline.png
│   ├── adls_bronze_silver_gold.png
│   └── databricks_transformation.png
│
└── databricks/
    └── retail_transformation.py
```

## What I Learned

This project gave me hands-on experience building a multi-source Azure data pipeline.

I learned how to:

* Ingest data from API and SQL sources using Azure Data Factory
* Store data using a Bronze, Silver and Gold architecture
* Process data using Azure Databricks and PySpark
* Clean and transform Spark DataFrames
* Join multiple datasets
* Create calculated columns and aggregations
* Store transformed data using Delta Lake
* Build an end-to-end cloud data engineering workflow

## Future Improvements

* Add data quality checks
* Add incremental data ingestion
* Add pipeline monitoring and error handling
* Use Azure Key Vault or Databricks secret management for credentials
* Add automated testing
* Connect the Gold layer to Power BI

---

**Pipeline:** API + SQL → Azure Data Factory → ADLS Gen2 Bronze → Databricks/PySpark → Delta Silver → Delta Gold
