from sqlalchemy import create_engine, text

server = r"HPV\MSSQLSERVER2"
database = "DataQualityDB"

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)

def log_etl(
    file_name,
    rows_read,
    rows_loaded,
    rows_rejected,
    status
):
    with engine.begin() as conn:

        conn.execute(
            text(
                """
                INSERT INTO ETL_Log
                (
                    file_name,
                    rows_read,
                    rows_loaded,
                    rows_rejected,
                    status,
                    load_start_time,
                    load_end_time
                )
                VALUES
                (
                    :file_name,
                    :rows_read,
                    :rows_loaded,
                    :rows_rejected,
                    :status,
                    GETDATE(),
                    GETDATE()
                )
                """
            ),
            {
                "file_name": file_name,
                "rows_read": rows_read,
                "rows_loaded": rows_loaded,
                "rows_rejected": rows_rejected,
                "status": status
            }
        )

    print("ETL Log Saved")