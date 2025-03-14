WITH TotalUsers AS (
    SELECT COUNT(user_id) AS total_users FROM Users
)
SELECT 
    r.contest_id, 
    ROUND(COUNT(DISTINCT r.user_id) * 100.0 / tu.total_users, 2) AS percentage
FROM Register r
JOIN TotalUsers tu
GROUP BY r.contest_id, tu.total_users
ORDER BY percentage DESC, contest_id ASC;