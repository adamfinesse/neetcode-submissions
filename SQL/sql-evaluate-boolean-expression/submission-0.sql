SELECT 
 expressions.left_operand,
 expressions.operator,
 expressions.right_operand,
 CASE 
    WHEN expressions.operator = '>' THEN v1.value > v2.value 
    WHEN expressions.operator = '<' THEN v1.value < v2.value
    ELSE v1.value = v2.value 
 END as value
FROM expressions
JOIN variables v1
ON v1.name = expressions.left_operand
JOIN variables v2
ON v2.name = expressions.right_operand;

