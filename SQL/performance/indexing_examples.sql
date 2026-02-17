CREATE INDEX idx_employees_department
ON employees(department_id);

EXPLAIN ANALYZE
SELECT *
FROM employees
WHERE department_id = 1;
