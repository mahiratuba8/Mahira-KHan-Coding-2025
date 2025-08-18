CREATE TABLE company_details (
    id INT,
    name TEXT,
    department TEXT,
    salary INT
);
INSERT INTO company_details 
(id, 
name, 
department, 
salary) 

VALUES
(1, 'Alice', 'HR', 4000),
(2, 'Bob', 'IT', 5000),
(3, 'Charlie', 'Finance', 6000),
(4, 'Diana', 'IT', 5500),
(5, 'Eve', 'HR', 4500);

--SELECT SUM(salary) FROM  company_details;

--SELECT MIN(salary) FROM  company_details;

SELECT MAX(salary) FROM  company_details;

--SELECT COUNT(DISTINCT department) FROM  company_details;