import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(
    "data/raw/olist_products_dataset.csv"
)

print("========== PRODUCTS DATA ==========\n")

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

# Rename columns to match SQL table

df.rename(
    columns={
        "product_name_lenght": "product_name_length",
        "product_description_lenght": "product_description_length"
    },
    inplace=True
)


# SQL Connection
server = r"HPV\MSSQLSERVER2"
database = "DataQualityDB"

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)
engine = create_engine(connection_string)

df.to_sql(
    "Products",
    engine,
    if_exists="append",
    index=False
)

print(f"\n✅ {len(df)} Products Loaded Successfully")