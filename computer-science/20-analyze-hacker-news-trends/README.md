# 👨‍💻 Project: Analyze Hacker News Trends

## 🎯 The Challenge from [Codecademy](http://www.codecademy.com/)

![The Challage of Codecademy](./image/image.png)

## 📊 Project Overview

Hacker News is a popular website run by Y Combinator, widely recognized in the tech industry as a community platform for sharing news, showcasing projects, and asking questions.

In this project, you'll analyze data from the `hacker_news` table, which contains stories from Hacker News since its launch in 2007.

### 🗃️ Dataset Structure

The dataset includes the following columns:

- **title**: The title of the story
- **user**: The user who submitted the story  
- **score**: The score of the story
- **timestamp**: The time when the story was posted
- **url**: The link to the story

*This data is publicly available under the MIT license.*

---

## 🔍 **Code Explanation (Generate by GitHub Copilot)**

The **Analyze Hacker News Trends program** uses **advanced SQL techniques** to analyze *community engagement patterns* and extract **meaningful insights** from Hacker News data. Here's how it works:

### **📋 Complete Code Structure**

```sql
-- Display top 5 highest-scored stories
SELECT title, score
FROM hacker_news
ORDER BY score DESC
LIMIT 5;

-- Calculate total score across all stories
SELECT SUM(score)
FROM hacker_news;

-- Find users with high total scores (>200)
SELECT user, SUM(score)
FROM hacker_news
GROUP BY user
HAVING SUM(score) > 200
ORDER BY 2 DESC;

-- Calculate percentage of top users' contribution
SELECT (517 + 309 + 304 + 282) / 6366.0;

-- Find users who posted specific YouTube link
SELECT user,
   COUNT(*)
FROM hacker_news
WHERE url LIKE '%watch?v=dQw4w9WgXcQ%'
GROUP BY user
ORDER BY COUNT(*) DESC;

-- Categorize stories by source domain
SELECT CASE
   WHEN url LIKE '%github.com%' THEN 'GitHub'
   WHEN url LIKE '%medium.com%' THEN 'Medium'
   WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
   ELSE 'Other'
  END AS 'Source'
FROM hacker_news;

-- Count stories by categorized source
SELECT CASE
   WHEN url LIKE '%github.com%' THEN 'GitHub'
   WHEN url LIKE '%medium.com%' THEN 'Medium'
   WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
   ELSE 'Other'
  END AS 'Source',
  COUNT(*)
FROM hacker_news
GROUP BY 1;

-- Examine timestamp format
SELECT timestamp
FROM hacker_news
LIMIT 10;

-- Extract hour from timestamp
SELECT timestamp,
   strftime('%H', timestamp)
FROM hacker_news
GROUP BY 1
LIMIT 20;

-- Analyze average scores by hour
SELECT strftime('%H', timestamp) AS 'Hour', 
   ROUND(AVG(score), 1) AS 'Average Score', 
   COUNT(*) AS 'Number of Stories'
FROM hacker_news
WHERE timestamp IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC;
```

### **🎯 How It Works**

**1. Top Content Analysis**
```sql
SELECT title, score
FROM hacker_news
ORDER BY score DESC
LIMIT 5;
```
- **ORDER BY DESC** sorts *stories* by **highest scores**
- **LIMIT clause** restricts *results* to **top performers**
- **Content ranking** identifies *most popular* **stories**

**2. Community Metrics**
```sql
SELECT SUM(score)
FROM hacker_news;
```
- **SUM function** calculates *total engagement* **score**
- **Community activity** *measurement* across **platform**
- **Aggregate metrics** for *overall* **health**

**3. User Contribution Analysis**
```sql
SELECT user, SUM(score)
FROM hacker_news
GROUP BY user
HAVING SUM(score) > 200
ORDER BY 2 DESC;
```
- **GROUP BY user** organizes *data* by **contributor**
- **HAVING clause** filters *high-impact* **users**
- **User ranking** identifies *top* **contributors**

**4. Influence Percentage**
```sql
SELECT (517 + 309 + 304 + 282) / 6366.0;
```
- **Mathematical calculation** determines *top users'* **impact**
- **Percentage analysis** shows *community* **concentration**
- **Influence metrics** for *platform* **dynamics**

**5. Content Pattern Detection**
```sql
SELECT user, COUNT(*)
FROM hacker_news
WHERE url LIKE '%watch?v=dQw4w9WgXcQ%'
GROUP BY user
ORDER BY COUNT(*) DESC;
```
- **LIKE operator** detects *specific* **URL patterns**
- **Pattern matching** identifies *duplicate* **content**
- **Spam detection** and *content* **analysis**

**6. Source Categorization**
```sql
SELECT CASE
   WHEN url LIKE '%github.com%' THEN 'GitHub'
   WHEN url LIKE '%medium.com%' THEN 'Medium'
   WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
   ELSE 'Other'
  END AS 'Source'
FROM hacker_news;
```
- **CASE statements** implement *conditional* **logic**
- **Domain classification** organizes *content* **sources**
- **URL parsing** for *source* **identification**

**7. Source Distribution**
```sql
SELECT CASE ... END AS 'Source',
  COUNT(*)
FROM hacker_news
GROUP BY 1;
```
- **Grouped categorization** shows *source* **distribution**
- **Content analysis** by *platform* **origin**
- **SOURCE popularity** *metrics*

**8. Temporal Analysis**
```sql
SELECT strftime('%H', timestamp) AS 'Hour', 
   ROUND(AVG(score), 1) AS 'Average Score', 
   COUNT(*) AS 'Number of Stories'
FROM hacker_news
WHERE timestamp IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC;
```
- **strftime function** extracts *hour* from **timestamps**
- **Temporal grouping** analyzes *posting* **patterns**
- **Time-based insights** for *optimal* **posting**

### **💡 Key SQL Concepts**

- **`Advanced Aggregation`** - *SUM*, **AVG**, **COUNT** with **complex conditions**
- **`CASE Statements`** - *Conditional logic* for **data categorization**
- **`Date/Time Functions`** - *strftime* for **temporal analysis**
- **`Pattern Matching`** - *LIKE operator* with **wildcards**
- **`Mathematical Operations`** - *Calculations* within **SQL queries**
- **`Complex Grouping`** - *Multi-level* **data organization**
- **`Result Ranking`** - *ORDER BY* with **multiple criteria**

### **📈 Hacker News Analysis Workflow**

**1. Content Performance**
- **Top stories** by *engagement* **score**
- **Community favorites** *identification*
- **Content quality** *assessment*

**2. User Behavior**
- **Power users** *identification*
- **Contribution patterns** *analysis*
- **Community influence** *metrics*

**3. Source Analysis**
- **Domain distribution** *across* **stories**
- **Platform preferences** in *community*
- **Content source** *diversity*

**4. Temporal Patterns**
- **Optimal posting** *times*
- **Engagement patterns** by *hour*
- **Community activity** *cycles*

### **📊 Expected Analysis Results**

| Analysis Type | Insight | Business Value |
|---------------|---------|----------------|
| Top Stories | Content performance | Editorial strategy |
| User Ranking | Community leaders | Influencer identification |
| Source Distribution | Platform preferences | Content sourcing |
| Hourly Patterns | Optimal timing | Posting strategy |

### **🔍 Community Intelligence Applications**

This SQL analysis enables:
- **Content strategy** *optimization* for **engagement**
- **Community management** through *user* **insights**
- **Posting optimization** based on *temporal* **patterns**
- **Source diversity** *analysis* for **content curation**
- **Platform health** *monitoring* through **metrics**

This project demonstrates how **advanced SQL analysis** can extract *actionable insights* from **social platform data** for community management and content strategy.

---

### 🙏 **Thank You, [Codecademy](https://www.codecademy.com/)**

I want to express my **sincere gratitude** to [**Codecademy**](https://www.codecademy.com/) for their **excellent learning platform**, **quality courses**, and the *opportunity to enhance my coding skills*. The **knowledge and experience** gained from [Codecademy](https://www.codecademy.com/) have **significantly contributed** to creating these projects and **developing my abilities**.