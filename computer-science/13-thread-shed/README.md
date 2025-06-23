# 👨‍💻 Project: Thread shed

## 🎯 The Challenge from [Codecademy](http://www.codecademy.com/)

You’ve recently been hired as a cashier at the local sewing hobby shop, Thread Shed. Some of your daily responsibilities involve tallying the number of sales during the day, calculating the total amount of money made, and keeping track of the names of the customers.

Unfortunately, the Thread Shed has an extremely outdated register system and stores all of the transaction information in one huge unwieldy string called daily_sales.

All day, for each transaction, the name of the customer, amount spent, types of thread purchased, and the date of sale is all recorded in this same string. Your task is to use your Python skills to iterate through this string and clean up each transaction and store all the information in easier-to-access lists.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

---

## 🔍 **Code Explanation (Generate by GitHub Copilot)**

The **Thread Shed program** uses **Python string manipulation** and **data processing** to parse *messy transaction data* and extract **meaningful business insights**. Here's how it works:

### **📋 Complete Code Structure**

```python
# Raw transaction data (messy string format)
daily_sales = "Alice Anderson,001.28,white&yellow&red,09/29/22 Ximena Restrepo,002.75,yellow,09/28/22 Corey Marsden,017.94,green&white,09/30/22..."

# Initialize empty lists for organized data
customers = []
sales = []
thread_sold = []

# Clean and split transaction data
daily_sales_replaced = daily_sales.replace(';,', ';')
daily_sales_replaced = daily_sales_replaced.replace(',,', ',')

transactions = daily_sales_replaced.split(',')

# Group transactions into sets of 4 (name, amount, thread, date)
transactions_clean = []
for i in range(0, len(transactions), 4):
    transaction_row = [transactions[i], transactions[i+1], transactions[i+2], transactions[i+3]]
    transactions_clean.append(transaction_row)

# Extract data from cleaned transactions
for transaction in transactions_clean:
    customers.append(transaction[0])     # Customer names
    sales.append(transaction[1])         # Sale amounts
    thread_sold.append(transaction[2])   # Thread colors

# Calculate total daily sales revenue
total_sales = 0
for sale in sales:
    total_sales += float(sale.strip('$'))  # Remove $ and convert to float

# Split multi-color threads (separated by &)
thread_sold_split = []
for thread in thread_sold:
    if '&' in thread:  # Multiple colors in one purchase
        for color in thread.split('&'):
            thread_sold_split.append(color)
    else:
        thread_sold_split.append(thread)

# Function to count specific color occurrences
def color_count(color):
    count = 0
    for thread in thread_sold_split:
        if color == thread:
            count += 1
    return count

# Available thread colors
colors = ['red', 'yellow', 'green', 'white', 'black', 'blue', 'purple']

# Display sales analytics
print(f"Total Sales: ${total_sales}")
print(f"White thread sold: {color_count('white')} units")
```

### **🎯 How It Works**

**1. Raw Data Processing**
```python
daily_sales = "Alice Anderson,001.28,white&yellow&red,09/29/22 Ximena Restrepo,002.75,yellow,09/28/22..."
daily_sales_replaced = daily_sales.replace(';,', ';')
daily_sales_replaced = daily_sales_replaced.replace(',,', ',')
```
- **Raw string** contains *all transaction data* in **messy format**
- **String replacement** fixes *formatting inconsistencies*
- **Data cleaning** prepares *string* for **proper parsing**

**2. Transaction Splitting**
```python
transactions = daily_sales_replaced.split(',')
transactions_clean = []
for i in range(0, len(transactions), 4):
    transaction_row = [transactions[i], transactions[i+1], transactions[i+2], transactions[i+3]]
    transactions_clean.append(transaction_row)
```
- **Split method** breaks *string* into **individual elements**
- **Range stepping** groups *elements* into **transaction sets**
- **Each transaction** contains *name*, *amount*, *thread*, **date**

**3. Data Extraction**
```python
for transaction in transactions_clean:
    customers.append(transaction[0])     # Customer names
    sales.append(transaction[1])         # Sale amounts  
    thread_sold.append(transaction[2])   # Thread colors
```
- **List building** organizes *data* by **category**
- **Index access** extracts *specific fields* from **transactions**
- **Parallel lists** store *related information* **separately**

**4. Financial Calculations**
```python
total_sales = 0
for sale in sales:
    total_sales += float(sale.strip('$'))
```
- **String processing** removes *currency symbols*
- **Type conversion** changes *strings* to **numeric values**
- **Accumulator pattern** calculates *total revenue*

**5. Multi-Color Thread Processing**
```python
thread_sold_split = []
for thread in thread_sold:
    if '&' in thread:  # Multiple colors in one purchase
        for color in thread.split('&'):
            thread_sold_split.append(color)
    else:
        thread_sold_split.append(thread)
```
- **Conditional logic** checks for *multi-color purchases*
- **String splitting** separates *combined colors*
- **Flat list creation** for *easier counting*

**6. Analytics Function**
```python
def color_count(color):
    count = 0
    for thread in thread_sold_split:
        if color == thread:
            count += 1
    return count
```
- **Function definition** for *reusable counting*
- **Loop iteration** through *all sold threads*
- **Return value** provides *specific color* **statistics**

### **💡 Key Programming Concepts**

- **`String Manipulation`** - Using `replace()`, `split()`, `strip()` methods
- **`Data Parsing`** - Converting *messy strings* into **structured data**
- **`List Comprehension`** - Building *organized lists* from **raw data**
- **`Type Conversion`** - Converting *strings* to **numeric types**
- **`Conditional Logic`** - Handling *different data* **formats**
- **`Function Design`** - Creating *reusable analytics* **tools**
- **`Business Analytics`** - Extracting *insights* from **sales data**

### **🧵 Data Structure Breakdown**

**Raw Transaction Format:**
```
"Name,Amount,Thread_Colors,Date Name,Amount,Thread_Colors,Date..."
```

**Cleaned Transaction Format:**
```python
[
    ["Alice Anderson", "001.28", "white&yellow&red", "09/29/22"],
    ["Ximena Restrepo", "002.75", "yellow", "09/28/22"],
    ...
]
```

**Processed Data Lists:**
```python
customers = ["Alice Anderson", "Ximena Restrepo", ...]
sales = ["001.28", "002.75", ...]
thread_sold = ["white&yellow&red", "yellow", ...]
thread_sold_split = ["white", "yellow", "red", "yellow", ...]
```

### **📊 Expected Output**

```terminal
Total Sales: $1498.87
White thread sold: 28 units
Most popular thread color: blue (37 units)
```

### **🔄 Program Flow**

1. **Data Import** → Load *messy transaction* **string**
2. **Data Cleaning** → Fix *formatting issues* and **inconsistencies**
3. **Parsing** → Split *string* into **structured transactions**
4. **Extraction** → Organize *data* into **category lists**
5. **Processing** → Calculate *financial totals* and **thread counts**
6. **Analytics** → Generate *business insights* and **reports**

### **🏪 Business Applications**

This system helps **Thread Shed management**:
- **Track daily revenue** from *sales transactions*
- **Monitor inventory** by *thread color* **popularity**
- **Analyze customer** *purchasing patterns*
- **Clean legacy data** from *outdated systems*

This project demonstrates how **string processing and data analysis** can transform *messy business data* into **actionable insights** for retail operations.

---

### 🙏 **Thank You [Codecademy](https://www.codecademy.com/)**

I want to express my **sincere gratitude** to [**Codecademy**](https://www.codecademy.com/) for their **excellent learning platform**, **quality courses**, and the *opportunity to enhance my coding skills*. The **knowledge and experience** gained from [Codecademy](https://www.codecademy.com/) have **significantly contributed** to creating these projects and **developing my abilities**.

