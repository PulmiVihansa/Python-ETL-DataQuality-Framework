USE OlistDW;
GO

INSERT INTO DimProduct
(
    product_id,
    product_category_name,
    product_weight_g
)

SELECT
    product_id,
    product_category_name,
    product_weight_g

FROM DataQualityDB.dbo.Products;