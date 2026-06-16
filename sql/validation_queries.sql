SELECT COUNT(*) AS Customers
FROM DataQualityDB.dbo.Customers;

SELECT COUNT(*) AS Orders
FROM DataQualityDB.dbo.Orders;

SELECT COUNT(*) AS OrderItems
FROM DataQualityDB.dbo.OrderItems;

SELECT COUNT(*) AS Products
FROM DataQualityDB.dbo.Products;


SELECT COUNT(*) AS DimCustomer
FROM OlistDW.dbo.DimCustomer;

SELECT COUNT(*) AS DimProduct
FROM OlistDW.dbo.DimProduct;

SELECT COUNT(*) AS FactSales
FROM OlistDW.dbo.FactSales;


SELECT * FROM DataQualityDB.dbo.ETL_Log;