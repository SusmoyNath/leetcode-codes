WITH sales AS (
    SELECT 
        u.product_id, 
        u.units, 
        p.price
    FROM UnitsSold u
    JOIN Prices p 
    ON u.product_id = p.product_id 
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
)
SELECT 
    p.product_id, 
    ROUND(COALESCE(SUM(s.units * s.price) / NULLIF(SUM(s.units), 0), 0), 2) AS average_price
FROM Prices p
LEFT JOIN sales s 
ON p.product_id = s.product_id
GROUP BY p.product_id;
