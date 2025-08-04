CREATE TABLE IF NOT EXISTS Salesmen(
    salesmen_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    comission TEXT
);

INSERT INTO Salesmen(
    salesmen_id,
    name,
    city,
    comission
)
VALUES 
    ("5001","James Hoog","New York","0.15"),
    ("5002","Nail Knite","Paris","0.13"),
    ("5005","Pit Alex","London","0.11"),
    ("5006","Mc Lyon","Paris","0.14"),
    ("5007","Paul Adam","Rome","0.13"),
    ("5003","Lauson Hen","San Jose","0.12");

CREATE TABLE IF NOT EXISTS customer(
    customer_id TEXT,
    cust_name TEXT PRIMARY KEY,
    city TEXT,
    grade TEXT,
    salesmen_id TEXT
);

INSERT INTO customer(
    customer_id,
    cust_name,
    city,
    grade,
    salesmen_id
)
VALUES 
    ("3002","nick rimando","new york","100","5001"),
    ("3007","brad davis","new york","200","5001"),
    ("3005","graham zusi","california","200","5002"),
    ("3008","julian green","london","300","5002"),
    ("3004","fabian johnson","paris","300","5006"),
    ("3009","geoff cameron","berlin","100","5003"),
    ("3003","jozy altidor","moscow","200","5007"),
    ("3001","brad guzan","london","","5005");

CREATE TABLE IF NOT EXISTS orders(
    order_no TEXT PRIMARY KEY,
    p_amt TEXT,
    order_date TEXT,
    customer_id TEXT,
    salesmen_id TEXT
);

INSERT INTO orders(
    order_no,
    p_amt,
    order_date,
    customer_id,
    salesmen_id
)
VALUES 
    ("70001","150.5","2012-10-05","3005","5002"),
    ("70009","270.65","2012-09-10","3001","5001"),
    ("70002","65.26","2012-10-05","3002","5003"),
    ("70004","110.5","2012-08-17","3009","5007"),
    ("70007","948.5","2012-09-10","3005","5005"),
    ("70005","2400.6","2012-07-27","3007","5006");

SELECT 
    customer.cust_name,
    Salesmen.name,
    Salesmen.city
FROM customer
JOIN Salesmen ON LOWER(customer.city) = LOWER(Salesmen.city);