import pandas as pd
from sqlalchemy import create_engine

# Read CSV
df = pd.read_csv(
    "data/raw/olist_customers_dataset.csv"
)

# SQL Server Connection
server = "HPV\\MSSQLSERVER2"
database = "DataQualityDB"

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)

# Load data
df.to_sql(
    "Customers",
    con=engine,
    schema="dbo",
    if_exists="append",
    index=False
)

print("Customers Loaded Successfully")