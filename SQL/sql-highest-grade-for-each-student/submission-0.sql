SELECT student_id, MIN(exam_id) as exam_id, score
FROM exam_results
WHERE (student_id, score) in (
    SELECT student_id, MAX(score) as score
    FROM exam_results
    GROUP BY student_id
    ORDER BY student_id ASC
)
GROUP BY student_id,score
ORDER BY student_id ASC;