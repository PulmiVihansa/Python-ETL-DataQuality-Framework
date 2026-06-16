CREATE DATABASE OlistDW;
GO

USE OlistDW;
GO

CREATE TABLE DimCustomer
(
    customer_key INT IDENTITY(1,1) PRIMARY KEY,

    customer_id VARCHAR(50),

    customer_city VARCHAR(100),

    customer_state VARCHAR(10),

    customer_zip_code_prefix INT
);

CREATE TABLE DimProduct
(
    product_key INT IDENTITY(1,1) PRIMARY KEY,

    product_id VARCHAR(50),

    product_category_name VARCHAR(100),

    product_weight_g FLOAT
);

CREATE TABLE FactSales
(
    sales_key INT IDENTITY(1,1) PRIMARY KEY,

    customer_key INT,

    product_key INT,

    sales_amount DECIMAL(18,2),

    freight_value DECIMAL(18,2),

    order_date DATETIME
);