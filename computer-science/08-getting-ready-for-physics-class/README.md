# 👨‍💻 Project: Getting Ready for Physics Class

## 🎯 The Challenge form [Codecademy](http://www.codecademy.com/)

You are a physics teacher preparing for the upcoming semester. You want to provide your students with some functions that will help them calculate some fundamental physical properties.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

---

## 🔍 **Code Explanation (Generate by GitHub Copilot)**

The **Physics Class program** uses **Python functions** to create *physics calculators* for **fundamental formulas**. Here's how it works:

### **📋 Complete Code Structure**

```python
# Initial values for physics calculations
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Temperature conversion: Fahrenheit to Celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9  # Formula: (F - 32) × 5/9
  return c_temp

f100_in_celsius = f_to_c(100)  # Convert 100°F to Celsius

# Temperature conversion: Celsius to Fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32  # Formula: C × 9/5 + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)  # Convert 0°C to Fahrenheit

# Newton's Second Law: Force = mass × acceleration
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Einstein's Energy Formula: E = mc²
def get_energy(mass, c = 3*10**8):  # c = speed of light
  return mass * c ** 2

bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")

# Work Formula: Work = Force × distance
def get_work(mass, acceleration, distance):
  return (mass * acceleration) * distance  # Force × distance

train_work = get_work(train_mass, train_acceleration, train_distance)

print('The GE train does ' + str(train_work) + ' Joules of work over ' + str(train_distance) + ' meters')
```

### **🎯 How It Works**

**1. Variable Setup for Physics Data**
```python
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
```
- **Variables** store *physical properties* for **calculations**
- **Real-world examples** - train mass, acceleration, distance

**2. Temperature Conversion Functions**
```python
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
```
- **Function definition** with *parameter* `f_temp`
- **Physics formula** implementation: `(F - 32) × 5/9`
- **Return statement** provides *calculated result*

**3. Function with Multiple Parameters**
```python
def get_force(mass, acceleration):
  return mass * acceleration
```
- **Two parameters** for *mass* and **acceleration**
- **Newton's Second Law** implementation: `F = ma`
- **Direct return** of *calculated value*

**4. Function with Default Parameter**
```python
def get_energy(mass, c = 3*10**8):
  return mass * c ** 2
```
- **Default parameter** `c` set to *speed of light*
- **Einstein's formula** implementation: `E = mc²`
- **Exponentiation** using `**` operator

**5. Function Calls and Results**
```python
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")
```
- **Function calls** pass *arguments* to **parameters**
- **Return values** stored in *variables*
- **String conversion** with `str()` for **output formatting**

### **💡 Key Programming Concepts**

- **`Function Definition`** - Creating *reusable code blocks* with `def`
- **`Parameters`** - Input *variables* for **function data**
- **`Return Values`** - Output *results* from **function calculations**
- **`Default Parameters`** - *Preset values* for **optional arguments**
- **`Function Calls`** - *Executing functions* with **specific arguments**
- **`Mathematical Operations`** - Implementing *physics formulas* in **code**
- **`String Formatting`** - Converting *numbers* to **text** for display

### **⚗️ Physics Formulas Implemented**

**Temperature Conversions:**
- **Fahrenheit to Celsius:** `(F - 32) × 5/9`
- **Celsius to Fahrenheit:** `C × 9/5 + 32`

**Newton's Laws:**
- **Force:** `F = ma` (mass × acceleration)
- **Work:** `W = F × d` (force × distance)

**Einstein's Relativity:**
- **Energy:** `E = mc²` (mass × speed of light²)

### **📊 Function Structure Breakdown**

**Basic Function:**
```python
def function_name(parameter):
    calculation = parameter * value
    return calculation
```

**Multiple Parameters:**
```python
def function_name(param1, param2):
    return param1 * param2
```

**Default Parameter:**
```python
def function_name(param1, param2=default_value):
    return param1 * param2
```

### **🔬 Expected Output**

```terminal
The GE train supplies 226800 Newtons of force.
A 1kg bomb supplies 90000000000000000 Joules
The GE train does 22680000 Joules of work over 100 meters
```

### **🔄 Program Flow**

1. **Variable Setup** → Define *physical constants* and **measurement values**
2. **Function Creation** → Define *reusable calculators* for **physics formulas**
3. **Temperature Tools** → Create *conversion functions* for **Celsius/Fahrenheit**
4. **Force Calculation** → Apply *Newton's Second Law* to **train example**
5. **Energy Calculation** → Apply *Einstein's formula* to **mass-energy**
6. **Work Calculation** → Combine *force and distance* for **work done**

### **🎓 Educational Value**

This program helps **physics students** by:
- **Automating calculations** for *complex formulas*
- **Providing reusable tools** for *different problems*
- **Demonstrating programming** in *scientific contexts*
- **Connecting math** to **real-world applications**

This project shows how **functions make code modular** and *reusable* while **solving practical scientific problems**.

---

### 🙏 **Thank You [Codecademy](https://www.codecademy.com/)**

I want to express my **sincere gratitude** to [**Codecademy**](https://www.codecademy.com/) for their **excellent learning platform**, **quality courses**, and the *opportunity to enhance my coding skills*. The **knowledge and experience** gained from [Codecademy](https://www.codecademy.com/) have **significantly contributed** to creating these projects and **developing my abilities**.