import pandas as pd
from sqlalchemy import create_engine

# Read CSV
df = pd.read_csv(
    "data/raw/olist_orders_dataset.csv"
)

print("========== ORDERS DATA ==========")

print("\nRows:", len(df))
print("Columns:", len(df.columns))

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

# SQL Connection
server = r"HPV\MSSQLSERVER2"
database = "DataQualityDB"

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)

# Load Data
df.to_sql(
    "Orders",
    con=engine,
    schema="dbo",
    if_exists="append",
    index=False
)

print(f"\n✅ {len(df)} Orders Loaded Successfully")