WITH RideSums AS (
    SELECT 
        user_id, 
        COALESCE(SUM(distance), 0) AS travelled_distance
    FROM Rides
    GROUP BY user_id
)
SELECT 
    u.name, 
    COALESCE(rs.travelled_distance, 0) AS travelled_distance
FROM Users u
LEFT JOIN RideSums rs ON u.id = rs.user_id
ORDER BY travelled_distance DESC, name ASC;
