# 📋 Project: New York Restaurants

## 🎯 The Challenge from [Codecademy](http://www.codecademy.com/)

We have a table of restaurants called `nomnom` and need your help to answer some questions. Use SQL commands to find the best dinner spots in the city.

The database schema is available [here](https://www.codecademy.com/journeys/computer-science/paths/cscj-22-databases/tracks/cscj-22-working-with-databases/modules/wdcp-22-what-can-i-do-with-a-database-77f195cc-06a4-457a-9db4-6f697f303f0e/projects/learn_sql_query_table-1).

---

## 🔍 Code Explanation (Generated by AI)

The New York Restaurants program uses SQL queries to analyze restaurant data and extract meaningful insights from the nomnom database. Here's how it works:

### 📋 Complete Code Structure

```sql
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
```

### 🎯 How It Works

1. Basic Data Retrieval
```sql
SELECT * FROM nomnom;
```
- SELECT statement retrieves all columns from nomnom table
- Asterisk (*) wildcard represents all available fields
- FROM clause specifies source table for data query

2. Unique Value Analysis
```sql
SELECT DISTINCT neighborhood FROM nomnom;
SELECT DISTINCT cuisine FROM nomnom;
```
- DISTINCT keyword eliminates duplicate values from result set
- Data exploration shows available options for filtering
- Categorical analysis reveals variety in dataset

3. Conditional Filtering
```sql
SELECT * FROM nomnom WHERE cuisine = 'Chinese';
SELECT * FROM nomnom WHERE review > 4;
```
- WHERE clause filters records based on specific conditions
- Comparison operators (=, >, <) test field values
- Conditional logic narrows results to relevant data

4. Complex Filtering
```sql
SELECT * FROM nomnom WHERE cuisine = 'Italian' AND price = "$$$";
```
- AND operator combines multiple conditions for precise filtering
- Logical operators create complex queries with multiple criteria
- Boolean logic refines search results

5. Pattern Matching
```sql
SELECT * FROM nomnom WHERE name LIKE '%meatball%';
```
- LIKE operator performs pattern matching on text fields
- Wildcard characters (%) match any sequence of characters
- Text search finds partial matches in string data

6. Multiple Conditions
```sql
SELECT * FROM nomnom WHERE neighborhood = 'Midtown' OR neighborhood = 'Downtown' OR neighborhood = 'Chinatown';
```
- OR operator matches any of multiple conditions
- Alternative filtering expands search criteria
- Location-based queries for geographic analysis

7. NULL Value Handling
```sql
SELECT * FROM nomnom WHERE health IS NULL;
```
- IS NULL condition finds missing values in database fields
- Data quality assessment for incomplete records
- Null checking identifies data gaps

8. Sorting and Limiting
```sql
SELECT * FROM nomnom ORDER BY review DESC LIMIT 10;
```
- ORDER BY clause sorts results by specified column
- DESC keyword arranges data in descending order
- LIMIT clause restricts number of returned records

9. Conditional Logic
```sql
SELECT name,
 CASE
  WHEN review > 4.5 THEN 'Extraordinary'
  WHEN review > 4 THEN 'Excellent'
  WHEN review > 3 THEN 'Good'
  WHEN review > 2 THEN 'Fair'
  ELSE 'Poor'
 END AS 'Review'
FROM nomnom;
```
- CASE statement implements conditional logic in queries
- WHEN clauses define condition-value pairs
- ELSE clause provides default value for unmatched conditions

### 💡 Key SQL Concepts

- `SELECT Statements` - Data retrieval from database tables
- `WHERE Clauses` - Conditional filtering of records
- `DISTINCT Keyword` - Unique value extraction
- `Logical Operators` - AND, OR for complex conditions
- `Comparison Operators` - =, >, < for value testing
- `Pattern Matching` - LIKE operator with wildcards
- `NULL Handling` - IS NULL for missing data
- `Sorting and Limiting` - ORDER BY and LIMIT clauses
- `Conditional Logic` - CASE statements for data categorization

### 🍽️ Restaurant Analysis Workflow

1. Data Exploration
- View all data to understand structure
- Identify unique neighborhoods and cuisines
- Assess data quality and completeness

2. Filtering and Search
- Filter by cuisine type for specific preferences
- Search by ratings to find quality restaurants
- Combine criteria for precise recommendations

3. Pattern Analysis
- Search restaurant names for specific dishes
- Analyze location distribution across neighborhoods
- Identify data gaps and missing information

4. Ranking and Categorization
- Sort restaurants by rating for top recommendations
- Categorize quality levels using review scores
- Limit results for manageable lists

### 📊 Expected Query Results

| Query Type | Purpose | Example Result |
|------------|---------|----------------|
| Basic SELECT | View all data | Complete restaurant listings |
| DISTINCT | Unique values | Available neighborhoods/cuisines |
| WHERE | Filtered data | High-rated Chinese restaurants |
| LIKE | Pattern match | Restaurants with "meatball" |
| ORDER BY | Sorted data | Top 10 rated establishments |
| CASE | Categorized data | Quality ratings by score ranges |

### 🗽 NYC Restaurant Applications

This SQL analysis enables:
- Restaurant discovery by cuisine preferences
- Quality assessment through rating analysis
- Location-based recommendations by neighborhood
- Data quality monitoring for incomplete records
- Business intelligence for restaurant trends

This project demonstrates how SQL queries can extract actionable insights from restaurant databases for dining recommendations and business analysis.

---

### 🙏 Thank You [Codecademy](https://www.codecademy.com/)

I want to express my sincere gratitude to [Codecademy](https://www.codecademy.com/) for their excellent learning platform, quality courses, and the opportunity to enhance my coding skills. The knowledge and experience gained from [Codecademy](https://www.codecademy.com/) have significantly contributed to creating these projects and developing my abilities.

