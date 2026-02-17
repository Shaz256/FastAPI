-- INNER JOIN
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id;

-- LEFT JOIN
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id;

-- RIGHT JOIN
SELECT e.name, d.department_name
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.department_id;

-- FULL JOIN
SELECT e.name, d.department_name
FROM employees e
FULL OUTER JOIN departments d
ON e.department_id = d.department_id;

-- CROSS JOIN
SELECT e.name, d.department_name
FROM employees e
CROSS JOIN departments d;

-- Aggregations
SELECT department_id, SUM(salary) FROM employees GROUP BY department_id;
SELECT department_id, AVG(salary) FROM employees GROUP BY department_id;
SELECT MIN(salary), MAX(salary) FROM employees;
