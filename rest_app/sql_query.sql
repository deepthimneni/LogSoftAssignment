SELECT 
	e.id, e.name, m.name as manager_name
FROM
	rest_api_employee e
LEFT OUTER JOIN 
	rest_api_employee m
ON e.manager_id = m.id