-- Display all startup data
SELECT *
FROM startups;

-- Count total number of startups
SELECT COUNT(*)
FROM startups;

-- Calculate total valuation of all startups
SELECT SUM(valuation)
FROM startups;

-- Find highest funding raised in Seed stage
SELECT MAX(raised)
FROM startups
WHERE stage = 'Seed';

-- Find earliest founding year
SELECT MIN(founded)
FROM startups;

-- Calculate average valuation across all startups
SELECT AVG(valuation)
FROM startups;

-- Average valuation by category (grouped)
SELECT category, AVG(valuation)
FROM startups
GROUP BY category;

-- Average valuation by category (rounded to 2 decimals)
SELECT category, ROUND(AVG(valuation)::NUMERIC, 2)
FROM startups
GROUP BY category;

-- Count startups in each category
SELECT category, COUNT(*)
FROM startups
GROUP BY category;

-- Categories with more than 3 startups
SELECT category, COUNT(*)
FROM startups
GROUP BY category
HAVING COUNT(*) > 3;

-- Average employees by location
SELECT location, AVG(employees)
FROM startups
GROUP BY location;

-- Locations with average >500 employees
SELECT location, AVG(employees)
FROM startups
GROUP BY location
HAVING AVG(employees) > 500;