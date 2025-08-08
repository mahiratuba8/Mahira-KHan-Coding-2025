CREATE TABLE IF NOT EXISTS Customer_details (
    CustomerID TEXT,
    CustomerName TEXT,
    Product TEXT,
    Country TEXT
);

INSERT INTO Customer_details (
CustomerID, 
CustomerName, 
Product, 
Country) 

VALUES
('03349', 'Aaron Ford', 'Laptops', 'USA'),
('07862', 'Arnold Corp', 'Mobiles', 'Canada'),
('02553', 'Adrian Moris', 'Furniture', 'Australia');

SELECT * FROM Customer_details WHERE CustomerName LIKE 'A%' AND CustomerName LIKE '%or%';