SELECT employee_id, IF(employee_id %2 = 1 AND LEFT(name, 1) != 'M', salary, 0) as bonus
FROM Employees
ORDER BY employee_id;