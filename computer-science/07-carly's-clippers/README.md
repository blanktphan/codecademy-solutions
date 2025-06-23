# 👨‍💻 Project: Carly's Clippers

## 🎯 The Challenge from [Codecademy](http://www.codecademy.com/)

You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. Your job is to go through the lists of data that have been collected in the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.

You have been provided with three lists:

- hairstyles: the names of the cuts offered at Carly’s Clippers.
- prices: the price of each hairstyle in the hairstyles list.
- last_week: the number of purchases for each hairstyle type in the last week.

Each index in hairstyles corresponds to an associated index in prices and last_week.

For example, The hairstyle "bouffant" has an associated price of 30 from the prices list, and was purchased 2 times in the last week as shown in the last_week list. Each of these elements are in the first index of their respective lists.

Let’s get started!

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

---

## 🔍 **Code Explanation (Generate by GitHub Copilot)**

The **Carly's Clippers program** uses **Python loops** and **list iteration** to analyze *hair salon data* and calculate **business metrics**. Here's how it works:

### **📋 Complete Code Structure**

```python
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]  # Hair salon services

prices = [30, 25, 40, 20, 20, 35, 50, 35]  # Prices for each hairstyle

last_week = [2, 3, 5, 8, 4, 4, 6, 2]  # Number of each service sold last week

total_price = 0  # Initialize accumulator

# Sum all prices using for loop
for price in prices:
  total_price += price

# Calculate average price
average_price = total_price / len(prices)

print("Average Haircut Price: " + str(average_price))

# Create discounted price list ($5 off each)
new_prices = []
for price in prices:
  new_prices.append(price - 5)

print(new_prices)

total_revenue = 0  # Initialize revenue accumulator

# Calculate total revenue (price × quantity sold)
for i in range(0, len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print('Total Revenue: '+ str(total_revenue))

# Calculate daily average from weekly total
average_daily_revenue = total_revenue / 7

# Find hairstyles under $30 after discount
cuts_under_30 = []
for i in range(0, len(new_prices)):
  if new_prices[i] < 30:
    cuts_under_30.append(hairstyles[i])

print('Under 30$ :'+ str(cuts_under_30))
```

### **🎯 How It Works**

**1. Data Structure Setup**
```python
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
```
- **Three parallel lists** store *related salon data*
- **Same index** corresponds to *same hairstyle* across **all lists**
- **Index 0:** "bouffant" costs *$30*, sold **2 times**

**2. Price Analysis with For Loop**
```python
total_price = 0
for price in prices:
  total_price += price
```
- **For loop** iterates through *each price* in **prices list**
- **Accumulator pattern** adds *each price* to **running total**
- **Variable `price`** holds *current list element* in **each iteration**

**3. Statistical Calculation**
```python
average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))
```
- **Division** calculates *mean price* using **total ÷ count**
- **`len()` function** gets *number of items* in **list**

**4. Price Modification with Loops**
```python
new_prices = []
for price in prices:
  new_prices.append(price - 5)
```
- **Empty list** created to *store modified prices*
- **For loop** processes *each original price*
- **Mathematical operation** subtracts *$5 from each price*
- **`append()` method** adds *modified price* to **new list**

**5. Revenue Calculation with Index Access**
```python
total_revenue = 0
for i in range(0, len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
```
- **`range()` function** generates *index numbers* from **0 to list length**
- **Index access** `[i]` gets *corresponding elements* from **multiple lists**
- **Multiplication** calculates *price × quantity* for **revenue**

**6. Filtering with Conditional Logic**
```python
cuts_under_30 = []
for i in range(0, len(new_prices)):
  if new_prices[i] < 30:
    cuts_under_30.append(hairstyles[i])
```
- **Conditional statement** `if` filters *only qualifying items*
- **Index iteration** accesses *multiple lists* simultaneously
- **List building** creates *new list* with **filtered results**

### **💡 Key Programming Concepts**

- **`For Loops`** - Iterating through *list elements* automatically
- **`Range Function`** - Generating *index numbers* for **list access**
- **`List Iteration`** - Processing *each element* in **sequence**
- **`Accumulator Pattern`** - Building *running totals* through **iteration**
- **`Parallel Lists`** - Managing *related data* across **multiple lists**
- **`Conditional Logic`** - Using `if` statements for **data filtering**
- **`Index Access`** - Using *position numbers* to **access elements**
- **`List Methods`** - Using `append()` for **list building**

### **📊 Loop Patterns Breakdown**

**Basic For Loop (Direct Iteration):**
```python
for item in list:
    # Process each item directly
```

**Index-Based Loop:**
```python
for i in range(len(list)):
    # Access list[i] for multiple lists
```

**Accumulator Pattern:**
```python
total = 0
for item in list:
    total += item
```

**List Building with Conditions:**
```python
new_list = []
for i in range(len(list)):
    if condition:
        new_list.append(item)
```

### **💼 Expected Output**

```terminal
Average Haircut Price: 31.875
[25, 20, 35, 15, 15, 30, 45, 30]
Total Revenue: 814
Under 30$ :['bouffant', 'pixie', 'crew', 'bowl', 'bob']
```

### **🔄 Program Flow**

1. **Data Setup** → Initialize *three parallel lists* with **salon data**
2. **Price Analysis** → Calculate *total* and **average prices** using loops
3. **Price Modification** → Create *discounted price list* with **$5 reduction**
4. **Revenue Calculation** → Multiply *prices × quantities* for **total income**
5. **Daily Metrics** → Calculate *average daily revenue* from **weekly data**
6. **Filtering** → Find *affordable cuts* using **conditional logic**

### **💰 Business Insights**

This program helps **salon management** understand:
- **Average pricing** for *menu planning*
- **Total revenue** for *financial tracking*
- **Discount impact** on *price positioning*
- **Affordable options** for *customer segments*

This project demonstrates how **loops and data analysis** can provide *valuable business intelligence* for **decision making** in service industries.

---

### 🙏 **Thank You [Codecademy](https://www.codecademy.com/)**

I want to express my **sincere gratitude** to [**Codecademy**](https://www.codecademy.com/) for their **excellent learning platform**, **quality courses**, and the *opportunity to enhance my coding skills*. The **knowledge and experience** gained from [Codecademy](https://www.codecademy.com/) have **significantly contributed** to creating these projects and **developing my abilities**.