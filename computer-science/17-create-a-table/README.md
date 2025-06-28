# 👨‍💻 Project: Create a Table

## 🎯 The Challenge from [Codecademy](http://www.codecademy.com/)

In this project, you will create your own friends table and perform data operations on it!

The instructions provided are a general guideline. Feel free to add more columns, insert more data, and create additional tables.

After completing each task below, click the "Save" button to check your progress. If no results appear in the "Query Results" tab, double-check your syntax for errors.

---

## 🔍 **Code Explanation (Generate by GitHub Copilot)**

The **Create a Table program** uses **SQL (Structured Query Language)** to demonstrate *database operations* including **table creation**, **data manipulation**, and **query execution**. Here's how it works:

### **📋 Complete Code Structure**

```sql
-- Create friends table with columns
CREATE TABLE friends (
   id INTEGER,
   name TEXT,
   birthday DATE
);

-- Insert initial friend records
INSERT INTO friends (id, name, birthday) 
VALUES (1, 'Ororo Munroe', '1940-05-30');

INSERT INTO friends (id, name, birthday)
VALUES (2, 'Pryfon Sangfra', '2002-12-23');

INSERT INTO friends (id, name, birthday)
VALUES (3, 'Thitiphan Saragool', '2002-11-13');

-- Update friend's name
UPDATE friends
SET name = 'Storm'
WHERE id = 1;

-- Add new email column
ALTER TABLE friends
ADD COLUMN email TEXT;

-- Update email addresses for all friends
UPDATE friends
SET email = 'storm@codecademy.com'
WHERE id = 1;

UPDATE friends
SET email = 'pryfon@codecademy.com'
WHERE id = 2;

UPDATE friends
SET email = 'thitiphan@codecademy.com'
WHERE id = 3;

-- Delete a friend record
DELETE FROM friends
WHERE id = 1;

-- Display final table contents
SELECT * 
FROM friends;
```

### **🎯 How It Works**

**1. Table Creation**
```sql
CREATE TABLE friends (
   id INTEGER,
   name TEXT,
   birthday DATE
);
```
- **CREATE TABLE** statement defines *new database* **table structure**
- **Column definitions** specify *data types* for **each field**
- **Schema design** establishes *table organization* and **data constraints**

**2. Data Insertion**
```sql
INSERT INTO friends (id, name, birthday) 
VALUES (1, 'Ororo Munroe', '1940-05-30');
```
- **INSERT INTO** statement adds *new records* to **database table**
- **VALUES clause** provides *specific data* for **each column**
- **Multiple inserts** populate *table* with **initial dataset**

**3. Data Modification**
```sql
UPDATE friends
SET name = 'Storm'
WHERE id = 1;
```
- **UPDATE statement** modifies *existing records* in **database**
- **SET clause** specifies *new values* for **target columns**
- **WHERE clause** filters *which records* to **update**

**4. Schema Modification**
```sql
ALTER TABLE friends
ADD COLUMN email TEXT;
```
- **ALTER TABLE** statement modifies *existing table* **structure**
- **ADD COLUMN** operation extends *schema* with **new fields**
- **Dynamic schema** allows *table evolution* over **time**

**5. Data Deletion**
```sql
DELETE FROM friends
WHERE id = 1;
```
- **DELETE statement** removes *specific records* from **table**
- **WHERE clause** targets *exact records* for **deletion**
- **Selective removal** maintains *data integrity*

**6. Data Retrieval**
```sql
SELECT * 
FROM friends;
```
- **SELECT statement** queries *data* from **database table**
- **Asterisk (*)** retrieves *all columns* from **specified table**
- **Result set** displays *current table* **contents**

### **💡 Key Database Concepts**

- **`SQL (Structured Query Language)`** - *Standard language* for **database operations**
- **`DDL (Data Definition Language)`** - *CREATE*, **ALTER statements**
- **`DML (Data Manipulation Language)`** - *INSERT*, **UPDATE**, **DELETE statements**
- **`DQL (Data Query Language)`** - *SELECT statements* for **data retrieval**
- **`Primary Key`** - *Unique identifier* for **table records**
- **`Data Types`** - *INTEGER*, **TEXT**, **DATE** for **column definitions**
- **`WHERE Clause`** - *Conditional filtering* for **targeted operations**

### **📊 Database Operations Summary**

| Operation | SQL Command | Purpose |
|-----------|-------------|---------|
| Create | `CREATE TABLE` | Define table structure |
| Insert | `INSERT INTO` | Add new records |
| Update | `UPDATE SET` | Modify existing data |
| Delete | `DELETE FROM` | Remove records |
| Query | `SELECT FROM` | Retrieve data |
| Modify | `ALTER TABLE` | Change table structure |

### **🔄 Program Flow**

1. **Table Creation** → Define *friends table* **schema**
2. **Data Population** → Insert *initial friend* **records**
3. **Data Updates** → Modify *existing information*
4. **Schema Evolution** → Add *new email* **column**
5. **Email Updates** → Populate *new field* with **values**
6. **Data Removal** → Delete *specific records*
7. **Final Query** → Display *remaining data*

### **📈 Expected Output**

```sql
id | name              | birthday   | email
---|-------------------|------------|------------------------
2  | Pryfon Sangfra    | 2002-12-23 | pryfon@codecademy.com
3  | Thitiphan Saragool| 2002-11-13 | thitiphan@codecademy.com
```

### **🗃️ Database Applications**

This SQL workflow demonstrates:
- **Database design** and *table creation*
- **CRUD operations** (Create, Read, Update, Delete)
- **Schema evolution** and *table modifications*
- **Data integrity** through *selective operations*
- **Query construction** for *data retrieval*

This project shows how **SQL database operations** work for *data management* and **information storage** in relational database systems.

---

### 🙏 **Thank You, [Codecademy](https://www.codecademy.com/)**

I want to express my **sincere gratitude** to [**Codecademy**](https://www.codecademy.com/) for their **excellent learning platform**, **quality courses**, and the *opportunity to enhance my coding skills*. The **knowledge and experience** gained from [Codecademy](https://www.codecademy.com/) have **significantly contributed** to creating these projects and **developing my abilities**.