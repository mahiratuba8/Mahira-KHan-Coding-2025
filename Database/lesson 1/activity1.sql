CREATE TABLE supplier(
serialno TEXT PRIMARY KEY,
serialname TEXT,
age INTEGER,
city TEXT
);

INSERT INTO supplier (
serialno,
serialname,
age,
city
)
VALUES 
('s1','Smith',20,'Paris'),
('s2','Adam',25,'New York'),
('s3','Mary',34,'Gothenburg'),
('s4','Bleke',23,'Rio de janero'),
('s5','Nia',30,'London');

SELECT * FROM supplier;

