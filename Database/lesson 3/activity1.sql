CREATE TABLE IF NOT EXISTS nom (
name TEXT,
neighbor TEXT,
cuisine TEXT,
review REAL,
price TEXT,
health TEXT

);

INSERT INTO nom(
name,
neighbor,
cuisine,
review,
price,
health
)
VALUES
('Peter', 'Brooklyn', 'Steak', 4.4, '$$$$', 'A'),

('Jongro', 'Midtown', 'Korean', 3.5, '$$', 'A'),

('Pocha', 'Midtown', 'Pizza', 4.0, '$$$', 'B'),

('Lighthouse', 'Queens', 'Chinese', 3.9, '$', 'A'),

('Minca', 'Downtown', 'American', 4.6, '$$$', ''),

('Marea', 'Chinatown', 'Chinese', 3.0, '$$', ''),

('Dirty Candy', 'Uptown', 'Italian', 4.9, '$$$$', 'B'),

('Di Fara Pizza', 'Brooklyn', 'Pizza', 3.8, '$$$', 'A'),

('Golden Unicorn', 'Uptown', 'Italian', 3.8, '$$$', 'A');

-- SELECT ALL RECORDS FROM nom

--SELECT * FROM nom;

--select distinct neighborhood

--SELECT DISTINCT neighbor FROM nom;

--select all records from the chineese cuisine

--SELECT * FROM nom  WHERE cuisine = 'Chinese';

--select records all with reviews heigher then 4 or same

--SELECT * FROM nom WHERE review > 4;

--select all records with italian cuisines and triple dollar price

--SELECT * FROM nom WHERE cuisine = 'Italian' AND price = '$$$';

--select all records where the name contains candy

--SELECT * FROM nom WHERE name LIKE '%Candy%';

-- select all record where the neihgborhood is midtown down town or china town

--SELECT * FROM nom WHERE  neighbor IN ('Midtown', 'Downtown', 'Chinatown');

--select the top 4 records

--SELECT TOP 4 RECORDS ORDERED BY review ndesc ORDER;
SELECT * FROM nom ORDER BY review DESC LIMIT 4;