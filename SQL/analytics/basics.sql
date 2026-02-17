-- Basic filtering and grouping

SELECT * FROM employees;

SELECT name, salary
FROM employees
WHERE salary > 80000;

SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id;

SELECT *
FROM employees
WHERE hire_date >= '2020-01-01';
