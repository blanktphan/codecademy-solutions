-- Create friends table with ID, name, and birthday columns
CREATE TABLE friends (
   id SERIAL PRIMARY KEY,
   name VARCHAR(255),
   birthday DATE
);

-- Insert first friend record
INSERT INTO friends (name, birthday) 
VALUES ('Ororo Munroe', '1940-05-30');

-- Insert second friend record
INSERT INTO friends (name, birthday)
VALUES ('Pryfon Sangfra', '2002-12-23');

-- Insert third friend record
INSERT INTO friends (name, birthday)
VALUES ('Thitiphan Saragool', '2002-11-13');

-- Update first friend's name to Storm
UPDATE friends
SET name = 'Storm'
WHERE id = 1;

-- Add new email column to existing table
ALTER TABLE friends
ADD COLUMN email VARCHAR(255);

-- Set email for Storm
UPDATE friends
SET email = 'storm@codecademy.com'
WHERE id = 1;

-- Set email for Pryfon
UPDATE friends
SET email = 'pryfon@codecademy.com'
WHERE id = 2;

-- Set email for Thitiphan
UPDATE friends
SET email = 'thitiphan@codecademy.com'
WHERE id = 3;

-- Remove Storm's record from table
DELETE FROM friends
WHERE id = 1;

-- Display all remaining friends data
SELECT * 
FROM friends;