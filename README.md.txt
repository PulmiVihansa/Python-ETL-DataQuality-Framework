# Python ETL & Data Quality Framework

## Project Overview

This project demonstrates an end-to-end Data Engineering pipeline built using Python, SQL Server, and Power BI. The solution ingests raw e-commerce data, performs data quality validation, loads data into SQL Server, builds a dimensional data warehouse using a Star Schema, and provides business insights through interactive Power BI dashboards.

---

## Architecture

Raw CSV Files
↓
Python ETL Pipeline
↓
Data Quality Validation
↓
SQL Server Staging Database
↓
Star Schema Data Warehouse
↓
Power BI Dashboards

---

## Dataset

The project uses the Olist Brazilian E-Commerce Dataset.

### Source Files

* olist_customers_dataset.csv
* olist_orders_dataset.csv
* olist_order_items_dataset.csv
* olist_products_dataset.csv

---

## Data Quality Checks

The ETL framework performs several validation checks before loading data:

* Null Customer ID Detection
* Null Order ID Detection
* Duplicate Record Detection
* Invalid Delivery Date Detection
* Product Data Validation
* ETL Load Monitoring

---

## Data Warehouse Design

### Dimension Tables

#### DimCustomer

* customer_key
* customer_id
* customer_city
* customer_state
* customer_zip_code_prefix

#### DimProduct

* product_key
* product_id
* product_category_name
* product_weight_g

### Fact Table

#### FactSales

* sales_key
* customer_key
* product_key
* sales_amount
* freight_value
* order_date

---

## ETL Processing Summary

| Table       | Records |
| ----------- | ------: |
| Customers   |  99,441 |
| Orders      |  99,441 |
| Order Items | 112,650 |
| Products    |  32,951 |
| FactSales   | 112,650 |

Total Records Processed: 457,133+

---

## Power BI Dashboards

### Dashboard 1 – Sales Analytics Dashboard

Features:

* Total Revenue Analysis
* Revenue Trend Analysis
* Revenue by State
* Revenue by Product Category
* Customer Distribution Analysis
* Interactive Filtering

### Dashboard 2 – ETL & Data Quality Monitoring Dashboard

Features:

* Total Rows Processed
* Success Rate Monitoring
* Data Quality Validation Results
* Rows Loaded by Table
* ETL Pipeline Visualization
* Technology Stack Overview

---

## Project Structure

```text
Python-ETL-DataQuality-Framework
│
├── data
│   ├── raw
│   ├── processed
│   └── rejected
│
├── dashboard
│   └── Olist_ETL_DataQuality_Framework.pbix
│
├── logs
│   └── etl_log.csv
│
├── screenshots
│
├── scripts
│
├── sql
│
├── README.md
```

---

## Tech Stack

* Python
* Pandas
* SQLAlchemy
* SQL Server
* Power BI
* Data Warehousing
* ETL Development
* Data Quality Validation

---

## Key Outcomes

* Built a complete ETL framework using Python
* Implemented automated data quality validation
* Loaded and transformed 457K+ records
* Designed a Star Schema Data Warehouse
* Developed Power BI business analytics dashboards
* Created ETL monitoring and reporting solutions

---


