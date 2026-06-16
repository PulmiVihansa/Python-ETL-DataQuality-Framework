import pandas as pd

df = pd.read_csv(
    "data/raw/olist_customers_dataset.csv"
)

print("========== CUSTOMER DATA ==========")

print("\nRows:", len(df))
print("Columns:", len(df.columns))

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nColumn Names")
print(df.columns.tolist())