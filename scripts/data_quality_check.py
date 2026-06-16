import pandas as pd
from sqlalchemy import create_engine

# SQL Connection
server = r"HPV\MSSQLSERVER2"
database = "DataQualityDB"

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)

# Load tables
customers = pd.read_sql("SELECT * FROM Customers", engine)
orders = pd.read_sql("SELECT * FROM Orders", engine)
products = pd.read_sql("SELECT * FROM Products", engine)

print("========== DATA QUALITY REPORT ==========\n")

# ----------------------------------
# CUSTOMERS
# ----------------------------------

print("CUSTOMERS")
print("----------")

print(
    "Null Customer IDs:",
    customers["customer_id"].isnull().sum()
)

print(
    "Duplicate Customer IDs:",
    customers["customer_id"].duplicated().sum()
)

print()

# ----------------------------------
# ORDERS
# ----------------------------------

print("ORDERS")
print("------")

print(
    "Null Order IDs:",
    orders["order_id"].isnull().sum()
)

print(
    "Duplicate Order IDs:",
    orders["order_id"].duplicated().sum()
)

invalid_dates = (
    orders["order_delivered_customer_date"]
    < orders["order_purchase_timestamp"]
).sum()

print(
    "Invalid Delivery Dates:",
    invalid_dates
)

print()

# ----------------------------------
# PRODUCTS
# ----------------------------------

print("PRODUCTS")
print("--------")

print(
    "Null Product IDs:",
    products["product_id"].isnull().sum()
)

print(
    "Negative Weight:",
    (products["product_weight_g"] < 0).sum()
)

print(
    "Negative Length:",
    (products["product_length_cm"] < 0).sum()
)