CREATE TABLE IF NOT EXISTS department (
employ_id TEXT ,
name TEXT,
department_id TEXT,
manager_id TEXT,
salary REAL
);

INSERT INTO department(
employ_id,
name,
department_id,
manager_id,
salary 
)

VALUES 
('100', 'STEVEN KING', '90', '100', 24000),

('101', 'NEENA KOCCHAR', '90', '100', 17000),

('102', 'LEX DEHAAN', '90', '102', 9000),

('103', 'BRUCE LEE', '60', '103', 4800),

('104', 'DIANA WILLS', '60', '103', 25000),

('105', 'VALLI PATOR', '50', '100', 4200),

('1973', 'LUV HAMI', '60', '102', 5000),

('106', 'DAVID AUSTIN', '90', '100', 6000);

--QUERY TO COUNT NUMBER OF EMPLOYS IN EACH DEPARTMENT

--SELECT department_id AS 'department code', COUNT (*) AS 'number of employees' FROM department GROUP BY department_id;

--QUERY TO SUM UP THE SALARY OF EACH DEPARTMENT

--SELECT department_id, SUM (salary) FROM department GROUP BY department_id;

--query to count the number of employees and sum the salary in each department

--SELECT department_id AS 'department code', SUM(salary) AS 'total salary' FROM department GROUP BY department_id; 

--query to sum the salary of number of employees with a specific manager =103

--SELECT department_id AS ' department code', SUM(salary) AS 'total salary' FROM department WHERE manager_id = '103' GROUP BY department_id;

--query to find departments with more then two employees

SELECT department_id, COUNT (*) AS 'number of employees' FROM department  GROUP BY department_id HAVING COUNT (*)>2 ;
