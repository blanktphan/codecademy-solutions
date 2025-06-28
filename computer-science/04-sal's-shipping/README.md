# 👨‍💻 Project: Sal's Shipping

## 🎯 The Challenge from [Codecademy](http://www.codecademy.com/)

**Sal** runs the biggest shipping company in the tri-county area, **Sal's Shippers**. Sal wants to make sure that every single one of his customers has the *best* and *most affordable experience* shipping their packages.

In this project, you'll build a program that will **take the weight of a package** and **determine the cheapest way** to ship that package using *Sal's Shippers*.

### 📦 **Shipping Options Available**

**Sal's Shippers** offers *three different shipping methods* for customers:

1. **🚛 Ground Shipping** - Small *flat charge* + *weight-based rate*
2. **⚡ Ground Shipping Premium** - Higher *flat charge*, **no weight fees**
3. **🚁 Drone Shipping** *(NEW!)* - **No flat charge**, but *triple weight rates*

### 💰 **Pricing Structure**

#### **🚛 Ground Shipping**

| Weight Range | Price per Pound | Flat Charge |
|:-------------|:----------------|:------------|
| **2 lb or less** | `$1.50` | `$20.00` |
| **Over 2 lb ≤ 6 lb** | `$3.00` | `$20.00` |
| **Over 6 lb ≤ 10 lb** | `$4.00` | `$20.00` |
| **Over 10 lb** | `$4.75` | `$20.00` |

#### **⚡ Ground Shipping Premium**

**Flat Rate:** `$125.00` *(regardless of weight)*

#### **🚁 Drone Shipping**

| Weight Range | Price per Pound | Flat Charge |
|:-------------|:----------------|:------------|
| **2 lb or less** | `$4.50` | `$0.00` |
| **Over 2 lb ≤ 6 lb** | `$9.00` | `$0.00` |
| **Over 6 lb ≤ 10 lb** | `$12.00` | `$0.00` |
| **Over 10 lb** | `$14.25` | `$0.00` |

### 🎯 **Your Mission**

Create a **`shipping.py`** Python program that:

1. **📝 Asks the user** for their *package weight*
2. **💻 Calculates costs** for *all three shipping methods*
3. **🔍 Determines** which method is the **cheapest**
4. **📊 Displays** the *best option* and **total cost**

**Goal:** Help customers find the *most affordable shipping solution* with **Sal's Shippers**!

---

## 🔍 **Code Explanation (Explanation by GitHub Copilot)**

The **Sal's Shipping program** uses **control flow** and **conditional logic** to determine the *cheapest shipping method* based on **package weight**. Here's how it works:

### **📋 Complete Code Structure**

```python
weight = 41.5  # Package weight in pounds

# Ground Shipping - Calculate cost based on weight tiers
if weight <= 2:
  cost_ground = (weight * 1.5) + 20  # $1.50/lb + $20 flat rate
elif weight > 2 and weight <= 6:
  cost_ground = (weight * 3) + 20    # $3.00/lb + $20 flat rate
elif weight > 6 and weight <= 10:
  cost_ground = (weight * 4) + 20    # $4.00/lb + $20 flat rate
elif weight > 10:
  cost_ground = (weight * 4.75) + 20 # $4.75/lb + $20 flat rate

print('Ground Shipping $', cost_ground)

# Ground Shipping Premium - Fixed flat rate
cost_premium = 125  # Always $125 regardless of weight

print('Ground Shipping Premium $', cost_premium)

# Drone Shipping - Calculate cost based on weight tiers (no flat rate)
if weight <= 2:
  cost_drone = (weight * 4.5)   # $4.50/lb only
elif weight > 2 and weight <= 6:
  cost_drone = (weight * 9)     # $9.00/lb only
elif weight > 6 and weight <= 10:
  cost_drone = (weight * 12)    # $12.00/lb only
elif weight > 10:
  cost_drone = (weight * 14.25) # $14.25/lb only

print('Drone Shipping $', cost_drone)

# Compare all three options and find cheapest
if cost_ground < cost_drone and cost_ground < cost_premium:
    print(f"Ground Shipping is cheapest at ${cost_ground}")
elif cost_drone < cost_premium:
    print(f"Drone Shipping is cheapest at ${cost_drone}")
else:
    print(f"Premium Ground Shipping is cheapest at ${cost_premium}")
```

### **🎯 How It Works**

**1. Weight Input**
```python
weight = 41.5  # Package weight in pounds
```
- Stores the **package weight** for *cost calculations*
- Can be modified to accept **user input** later

**2. Ground Shipping Calculation**
```python
if weight <= 2:
  cost_ground = (weight * 1.5) + 20  # Tier 1: $1.50/lb + $20
elif weight > 2 and weight <= 6:
  cost_ground = (weight * 3) + 20    # Tier 2: $3.00/lb + $20
```
- **If/elif chain** handles *different weight ranges*
- **Formula:** `(weight × rate) + flat_charge`
- **All tiers** include a *$20 flat rate*

**3. Premium Ground Shipping**
```python
cost_premium = 125  # Fixed $125 regardless of weight
```
- **Simple assignment** - no *calculation needed*
- **Flat rate** pricing for *convenience*

**4. Drone Shipping Calculation**
```python
if weight <= 2:
  cost_drone = (weight * 4.5)   # $4.50/lb only
elif weight > 2 and weight <= 6:
  cost_drone = (weight * 9)     # $9.00/lb only
```
- **Similar structure** to ground shipping
- **Higher rates** but *no flat charge*
- **Weight-only** pricing model

**5. Cost Comparison Logic**
```python
if cost_ground < cost_drone and cost_ground < cost_premium:
    print(f"Ground Shipping is cheapest")
elif cost_drone < cost_premium:
    print(f"Drone Shipping is cheapest")
else:
    print(f"Premium Ground Shipping is cheapest")
```
- **Multiple comparisons** find the *lowest cost*
- **Logical operators** (`<` and `and`) evaluate **conditions**
- **F-string formatting** displays *results clearly*

### **💡 Key Programming Concepts**

- **`Control Flow`** - Using *if/elif/else* for **decision making**
- **`Conditional Logic`** - Multiple *comparisons* and **logical operators**
- **`Mathematical Operations`** - Calculating *costs* using **arithmetic**
- **`Comparison Operators`** - Using `<`, `<=`, `>` for **evaluations**
- **`Logical Operators`** - Using `and` to combine **conditions**
- **`Variables`** - Storing *calculated results* for **comparison**
- **`Print Function`** - Displaying *formatted output* to **console**

### **📊 Weight Tier Breakdown**

**Ground Shipping Tiers:**
- **0-2 lbs:** $1.50/lb + $20 flat
- **2-6 lbs:** $3.00/lb + $20 flat  
- **6-10 lbs:** $4.00/lb + $20 flat
- **10+ lbs:** $4.75/lb + $20 flat

**Drone Shipping Tiers:**
- **0-2 lbs:** $4.50/lb only
- **2-6 lbs:** $9.00/lb only
- **6-10 lbs:** $12.00/lb only
- **10+ lbs:** $14.25/lb only

### **🚚 Expected Output Example**

For a **41.5 lb package:**
```terminal
Ground Shipping $ 217.25
Ground Shipping Premium $ 125
Drone Shipping $ 591.375
Premium Ground Shipping is cheapest at $125
```

### **🔄 Program Flow**

1. **Weight Input** → Define *package weight*
2. **Ground Calculation** → Apply *appropriate tier* and **flat rate**
3. **Premium Assignment** → Set *fixed price* of **$125**
4. **Drone Calculation** → Apply *tier rate* with **no flat charge**
5. **Cost Comparison** → Find *cheapest option* using **logical operators**
6. **Result Display** → Show *best choice* and **final cost**

This program demonstrates how **conditional statements** and **logical operators** can solve *real-world decision-making* problems in **business applications**.

---

### 🙏 **Thank You, [Codecademy](https://www.codecademy.com/)**

I want to express my **sincere gratitude** to [**Codecademy**](https://www.codecademy.com/) for their **excellent learning platform**, **quality courses**, and the *opportunity to enhance my coding skills*. The **knowledge and experience** gained from [Codecademy](https://www.codecademy.com/) have **significantly contributed** to creating these projects and **developing my abilities**.