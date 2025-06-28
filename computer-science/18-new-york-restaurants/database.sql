-- Display all restaurant data
SELECT * FROM nomnom;

-- Show unique neighborhoods (no duplicates)
SELECT DISTINCT neighborhood FROM nomnom;

-- Show unique cuisine types
SELECT DISTINCT cuisine FROM nomnom;

-- Filter restaurants by Chinese cuisine
SELECT * FROM nomnom WHERE cuisine = 'Chinese';

-- Filter restaurants with high ratings (>4)
SELECT * FROM nomnom WHERE review > 4;

-- Filter Italian restaurants with $$$ price range
SELECT * FROM nomnom WHERE cuisine = 'Italian' AND price = "$$$";

-- Search restaurants with 'meatball' in name
SELECT * FROM nomnom WHERE name LIKE '%meatball%';

-- Filter restaurants in multiple neighborhoods
SELECT * FROM nomnom WHERE neighborhood = 'Midtown' OR neighborhood = 'Downtown' OR neighborhood = 'Chinatown'; 

-- Find restaurants with missing health scores
SELECT * FROM nomnom WHERE health IS NULL;

-- Show top 10 highest-rated restaurants
SELECT * FROM nomnom ORDER BY review DESC LIMIT 10;

-- Categorize restaurants by review scores
SELECT name,
 CASE
  WHEN review > 4.5 THEN 'Extraordinary'
  WHEN review > 4 THEN 'Excellent'
  WHEN review > 3 THEN 'Good'
  WHEN review > 2 THEN 'Fair'
  ELSE 'Poor'
 END AS 'Review'
FROM nomnom;
