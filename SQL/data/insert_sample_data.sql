INSERT INTO departments (department_name) VALUES
('IT'),
('HR'),
('Finance'),
('Sales');

INSERT INTO employees (name, department_id, salary, hire_date) VALUES
('Alice', 1, 90000, '2021-01-10'),
('Bob', 1, 85000, '2020-03-15'),
('Charlie', 2, 60000, '2019-07-23'),
('David', 3, 95000, '2022-02-11'),
('Eva', 4, 72000, '2021-11-05'),
('Frank', 1, 88000, '2018-09-17');

INSERT INTO orders (customer_id, order_date, amount) VALUES
(101, '2024-01-05', 250),
(102, '2024-01-12', 400),
(101, '2024-02-03', 150),
(103, '2024-02-20', 600),
(104, '2024-03-01', 300);
