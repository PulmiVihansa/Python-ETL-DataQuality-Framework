USE OlistDW;
GO

INSERT INTO DimCustomer
(
    customer_id,
    customer_city,
    customer_state,
    customer_zip_code_prefix
)

SELECT
    customer_id,
    customer_city,
    customer_state,
    customer_zip_code_prefix

FROM DataQualityDB.dbo.Customers;