# Project: Len's Slice

## 🎯 The Challenge form [Codecademy](http://www.codecademy.com/)

You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.

---

## 🔍 **Code Explanation (Generate by GitHub Copilot)**

The **Len's Slice program** uses **Python lists** and **list methods** to manage *pizza shop data* including **prices**, **toppings**, and **sales analysis**. Here's how it works:

### **📋 Complete Code Structure**

```python
# Pizza toppings and prices (parallel lists)
toppings = ['pepperonil', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

# Count how many pizzas cost $2
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Get total number of pizza types
num_pizzas = len(toppings)
print('We sell '+ str(num_pizzas) + " different kinds of pizza!")

# Combine prices and toppings into nested list
pizza_and_prices = [[2, 'pepperonil'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]
print(pizza_and_prices)

# Sort by price (first element in each sublist)
pizza_and_prices.sort()

# Get cheapest and most expensive pizzas
cheapest_pizza = pizza_and_prices[0]  # First item after sorting
priciest_pizza = pizza_and_prices[-1]  # Last item

# Remove the most expensive pizza
pizza_and_prices.pop()

# Add new pizza to menu
pizza_and_prices.append([2.5, "peppers"])

# Get the three cheapest pizzas using slicing
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)
```

### **🎯 How It Works**

**1. Data Structure Setup**
```python
toppings = ['pepperonil', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]
```
- **Parallel lists** store *related data* at **corresponding indexes**
- **Toppings list** contains *pizza names* as **strings**
- **Prices list** contains *costs* as **numbers**

**2. Data Analysis with List Methods**
```python
num_two_dollar_slices = prices.count(2)  # Count occurrences
num_pizzas = len(toppings)  # Get list length
```
- **`count()` method** finds *how many times* a value **appears**
- **`len()` function** returns *total number* of **list elements**

**3. Data Restructuring**
```python
pizza_and_prices = [[2, 'pepperonil'], [6, 'pineapple'], [1, 'cheese'], ...]
```
- **Nested lists** combine *price and topping* data **together**
- Each **inner list** contains *[price, topping]* format

**4. Data Sorting**
```python
pizza_and_prices.sort()  # Sorts by first element (price)
```
- **`sort()` method** arranges *nested lists* by **first element**
- **Ascending order** - *cheapest* to **most expensive**

**5. Data Access with Indexing**
```python
cheapest_pizza = pizza_and_prices[0]   # First element
priciest_pizza = pizza_and_prices[-1]  # Last element
```
- **Positive indexing** `[0]` gets *first* element
- **Negative indexing** `[-1]` gets *last* element

**6. Menu Management**
```python
pizza_and_prices.pop()  # Remove last item
pizza_and_prices.append([2.5, "peppers"])  # Add new item
```
- **`pop()` method** removes *last element* from **list**
- **`append()` method** adds *new element* to **end**

**7. List Slicing**
```python
three_cheapest = pizza_and_prices[0:3]  # Get first 3 elements
```
- **Slice notation** `[start:end]` extracts *portion* of **list**
- **`[0:3]`** gets *elements 0, 1, 2* (3 is **excluded**)

### **💡 Key Programming Concepts**

- **`Lists`** - Storing *multiple related items* in **ordered collections**
- **`Parallel Lists`** - *Related data* stored in **separate lists**
- **`Nested Lists`** - *Lists within lists* for **structured data**
- **`List Methods`** - Using `count()`, `len()`, `sort()`, `pop()`, `append()`
- **`List Indexing`** - Accessing *elements* by **position**
- **`List Slicing`** - Extracting *portions* of **lists**
- **`Data Analysis`** - Finding *patterns* and **statistics** in data

### **🍕 List Operations Breakdown**

**Counting & Measuring:**
- **`count(value)`** - *How many times* value **appears**
- **`len(list)`** - *Total number* of **elements**

**Accessing Elements:**
- **`[index]`** - *Single element* at **position**
- **`[start:end]`** - *Multiple elements* in **range**
- **`[-1]`** - *Last element* using **negative index**

**Modifying Lists:**
- **`sort()`** - *Arrange elements* in **ascending order**
- **`pop()`** - *Remove* and return **last element**
- **`append(item)`** - *Add item* to **end of list**

### **📊 Expected Output**

```terminal
3
We sell 7 different kinds of pizza!
[[2, 'pepperonil'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]
[[1, 'cheese'], [2, 'pepperonil'], [2, 'olives']]
```

### **🔄 Program Flow**

1. **Data Setup** → Create *parallel lists* for **toppings and prices**
2. **Analysis** → Count *specific values* and **measure list size**
3. **Restructuring** → Combine *related data* into **nested lists**
4. **Sorting** → Arrange *by price* for **easy comparison**
5. **Data Access** → Find *cheapest* and **most expensive** items
6. **Menu Updates** → Remove *expensive items*, add **new options**
7. **Filtering** → Extract *top choices* using **slicing**

This program demonstrates how **list operations** can manage *business data* and perform **sales analysis** for a pizza shop.

---

### 🙏 **Thank You [Codecademy](https://www.codecademy.com/)**

I want to express my **sincere gratitude** to [**Codecademy**](https://www.codecademy.com/) for their **excellent learning platform**, **quality courses**, and the *opportunity to enhance my coding skills*. The **knowledge and experience** gained from [Codecademy](https://www.codecademy.com/) have **significantly contributed** to creating these projects and **developing my abilities**.