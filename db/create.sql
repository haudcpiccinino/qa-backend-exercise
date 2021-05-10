DROP TABLE IF EXISTS users;
CREATE TABLE users (id SERIAL PRIMARY KEY, fullname varchar UNIQUE, occupation varchar);
INSERT INTO users (fullname,occupation) VALUES
('Dorothy Gale','Return to Kansas'),
('Hickory Tin Man','Find a hearth'),
('Hunk Scarecrow','Find a brain'),
('Toto',NULL),
('Zeke Cowardly Lion','Find couraged');



SELECT * FROM users;
DELETE FROM users WHERE id='1';
INSERT INTO users (fullname,occupation) VALUES ('Dorothy Gale','Return to Kansas');