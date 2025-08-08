CREATE TABLE Employees (
    EmpID TEXT,
    Name TEXT,
    Department TEXT,
    Salary TEXT,
    JoinDate TEXT,
    Email TEXT
);

INSERT INTO Employees (
EmpID, 
Name, 
Department, 
Salary, 
JoinDate, 
Email) 

VALUES
('1', 'Amit Sharma', 'IT', '60000', '2021-05-12', 'amit@company.com'),
('2', 'Neha Verma', 'HR', '45000', '2020-11-01', NULL),
('3', 'Ravi Kumar', 'Finance', NULL, '2022-02-20', 'ravi@company.com'),
('4', 'Priya Singh', 'IT', '55000', '2019-08-15', 'priya@company.com'),
('5', 'Vikas Gupta', 'Sales', '30000', '2021-12-10', NULL);

SELECT * FROM Employees WHERE JoinDate BETWEEN '2021-01-01' AND '2022-01-01';