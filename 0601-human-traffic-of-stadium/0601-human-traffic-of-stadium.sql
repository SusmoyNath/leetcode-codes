WITH consecutive_groups AS (
    SELECT 
        id, 
        visit_date, 
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS group_id
    FROM Stadium
    WHERE people >= 100
)
SELECT id, visit_date, people
FROM (
    SELECT *,
           COUNT(*) OVER (PARTITION BY group_id) AS group_size
    FROM consecutive_groups
) subquery
WHERE group_size >= 3
ORDER BY visit_date;
