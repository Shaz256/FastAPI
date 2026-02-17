-- Top 3 highest paid employees per department

SELECT *
FROM (
    SELECT
        e.employee_id,
        e.name,
        d.department_name,
        e.salary,
        ROW_NUMBER() OVER (
            PARTITION BY e.department_id
            ORDER BY e.salary DESC
        ) AS rn
    FROM employees e
    JOIN departments d
        ON e.department_id = d.department_id
) t
WHERE rn <= 3;
