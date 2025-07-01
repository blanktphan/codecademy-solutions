-- Display top 5 highest-scored stories
SELECT title, score
FROM hacker_news
ORDER BY score DESC
LIMIT 5;

-- Calculate total score across all stories
SELECT SUM(score)
FROM hacker_news;

-- Find users with high total scores (>200)
SELECT "user", SUM(score)
FROM hacker_news
GROUP BY "user"
HAVING SUM(score) > 200
ORDER BY 2 DESC;

-- Calculate percentage of top users' contribution
SELECT (517 + 309 + 304 + 282) / 6366.0;

-- Find users who posted specific YouTube link
SELECT "user",
    COUNT(*)
FROM hacker_news
WHERE url LIKE '%watch?v=dQw4w9WgXcQ%'
GROUP BY "user"
ORDER BY COUNT(*) DESC;

-- Categorize stories by source domain
SELECT CASE
    WHEN url LIKE '%github.com%' THEN 'GitHub'
    WHEN url LIKE '%medium.com%' THEN 'Medium'
    WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
    ELSE 'Other'
  END AS "Source"
FROM hacker_news;

-- Count stories by categorized source
SELECT CASE
    WHEN url LIKE '%github.com%' THEN 'GitHub'
    WHEN url LIKE '%medium.com%' THEN 'Medium'
    WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
    ELSE 'Other'
  END AS "Source",
  COUNT(*)
FROM hacker_news
GROUP BY 1;

-- Examine timestamp format
SELECT "timestamp"
FROM hacker_news
LIMIT 10;

-- Extract hour from timestamp
SELECT "timestamp",
    EXTRACT(HOUR FROM "timestamp"::timestamp)
FROM hacker_news
GROUP BY 1
LIMIT 20;

-- Analyze average scores by hour
SELECT EXTRACT(HOUR FROM "timestamp"::timestamp), 
    AVG(score),
    COUNT(*)
FROM hacker_news
GROUP BY 1
ORDER BY 2 DESC;

-- Final hourly analysis with formatted results
SELECT EXTRACT(HOUR FROM "timestamp"::timestamp) AS "Hour", 
    ROUND(AVG(score), 1) AS "Average Score", 
    COUNT(*) AS "Number of Stories"
FROM hacker_news
WHERE "timestamp" IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC;
