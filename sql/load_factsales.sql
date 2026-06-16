USE OlistDW;
GO

INSERT INTO FactSales
(
    customer_key,
    product_key,
    sales_amount,
    freight_value,
    order_date
)

SELECT

    dc.customer_key,

    dp.product_key,

    oi.price,

    oi.freight_value,

    o.order_purchase_timestamp

FROM DataQualityDB.dbo.OrderItems oi

INNER JOIN DataQualityDB.dbo.Orders o
    ON oi.order_id = o.order_id

INNER JOIN DataQualityDB.dbo.Customers c
    ON o.customer_id = c.customer_id

INNER JOIN DimCustomer dc
    ON c.customer_id = dc.customer_id

INNER JOIN DimProduct dp
    ON oi.product_id = dp.product_id;