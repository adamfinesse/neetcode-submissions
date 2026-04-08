SELECT seller_name
FROM seller
WHERE seller_id not in (
    SELECT seller_id from orders WHERE sale_date BETWEEN '2020-01-01' AND '2020-12-31'
)
ORDER BY seller_name asc;