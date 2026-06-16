from sqlalchemy import create_engine

server = r"HPV\MSSQLSERVER2"
database = "DataQualityDB"

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

try:
    engine = create_engine(connection_string)

    with engine.connect() as conn:
        print("✅ Connected Successfully")

except Exception as e:
    print("❌ Connection Failed")
    print(e)