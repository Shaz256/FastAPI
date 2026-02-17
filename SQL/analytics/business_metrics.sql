-- Monthly revenue

SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(amount) AS monthly_revenue
FROM orders
GROUP BY month
ORDER BY month;

-- Top customers

SELECT
    customer_id,
    SUM(amount) AS total_spent
FROM orders
GROUP BY customer_id
ORDER BY total_spent DESC;
