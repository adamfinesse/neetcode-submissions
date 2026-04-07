-- Write your query below
SELECT 
    employee_id, 
    CASE 
        WHEN name like 'M%' or employee_id % 2 = 0 THEN 0 
        ELSE salary 
    END as bonus
FROM employees
ORDER BY employee_id;