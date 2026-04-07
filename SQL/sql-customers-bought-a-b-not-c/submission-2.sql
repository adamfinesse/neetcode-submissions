SELECT
    customer_id,customer_name
FROM
    customers
WHERE
    customer_id in(
        SELECT customer_id FROM orders WHERE
        customer_id in (SELECT customer_id FROM ORDERS WHERE product_name = 'A') 
            AND 
        customer_id in (SELECT customer_id FROM ORDERS WHERE product_name = 'B')
            AND
        customer_id not in (
            SELECT
                customer_id
            FROM
                orders
            WHERE
                product_name = 'C'
        )
    )
ORDER BY customer_name;