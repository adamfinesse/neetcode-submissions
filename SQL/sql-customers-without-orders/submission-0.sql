-- Write your query below
SELECT name
FROM customers c
LEFT JOIN orders o on c.id = o.customer_id
where o.id is null;

