CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name TEXT,
    city TEXT,
    grade INT
);

INSERT INTO customers (
customer_id, 
name, 
city, 
grade) 


VALUES
(1, 'Alice', 'New York', 95),
(2, 'Bob', 'Los Angeles', 110),
(3, 'Charlie', 'New York', 105),
(4, 'David', 'Chicago', 90),
(5, 'Eve', 'New York', 101),
(6, 'Frank', 'Boston', 120);


SELECT * FROM customers WHERE city = 'New York' OR grade > 100;