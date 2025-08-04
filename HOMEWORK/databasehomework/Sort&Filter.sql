CREATE TABLE IF NOT EXISTS hacker_news (
    id INTEGER PRIMARY KEY,
    title TEXT,
    score INTEGER,
    author TEXT
);

INSERT OR IGNORE INTO hacker_news (
    id, 
    title, 
    score, 
    author
) 
VALUES
(1, 'OpenAI launches GPT-5', 520, 'techguy'),
(2, 'Quantum computing breakthrough by Google', 430, 'quantumfan'),
(3, 'Rust tops developer survey again', 390, 'coder123'),
(4, 'Linux 6.5 released with major updates', 275, 'linuxdev'),
(5, 'AI beats humans in code competitions', 610, 'aifan');

SELECT author, title, score AS 'TOP RATED NEWS' FROM hacker_news WHERE score > 300;