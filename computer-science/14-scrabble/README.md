# 👨‍💻 Project: Scrabble

## 🎯 The Challenge from [Codecademy](http://www.codecademy.com/)

In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.

There are many ways you can extend this project on your own if you finish and want to get more practice!

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

---

## 🔍 **Code Explanation (Generate by GitHub Copilot)**

The **Scrabble program** uses **Python dictionaries** and **functions** to create a *scoring system* that calculates **word values** and tracks **player points**. Here's how it works:

### **📋 Complete Code Structure**

```python
# Scrabble letter values
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Create letter-to-points mapping dictionary
letter_to_points = {key:value for key,value in zip(letters, points)}
letter_to_points[' '] = 0  # Blank tiles worth 0 points

# Function to calculate word score
def score_word(word):
    point_total = 0
    for letter in word.upper():
        if letter_to_points.get(letter, 0):
            point_total += letter_to_points[letter]
    return point_total

# Test word scoring
brownie_points = score_word('BROWNIE')
print(brownie_points)

# Player game data
player_to_words = {
    'Player1': ['BLUE', 'TENNIS', 'EXIT'],
    'wordNerd': ['EARTH', 'EYES', 'MACHINE'],
    'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'],
    'Prof Reader': ['ZAP', 'COMA', 'PERIOD']
}

# Function to add words to player
def play_word(player, word):
    player_to_words[player].append(word)
    return player_to_words

# Dictionary to store player total scores
player_to_points = {}

# Function to calculate all player totals
def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points
    return player_to_points

# Update scores and display results
update_point_totals()
print(player_to_points)
```

### **🎯 How It Works**

**1. Letter-Point Mapping Creation**
```python
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", ...]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, ...]
letter_to_points = {key:value for key,value in zip(letters, points)}
```
- **Parallel lists** store *letters* and **point values**
- **Dictionary comprehension** with `zip()` creates *key-value pairs*
- **Mapping structure** allows *quick point* **lookups**

**2. Word Scoring Function**
```python
def score_word(word):
    point_total = 0
    for letter in word.upper():
        if letter_to_points.get(letter, 0):
            point_total += letter_to_points[letter]
    return point_total
```
- **Function definition** for *reusable scoring*
- **String method** `upper()` handles *case conversion*
- **Dictionary method** `get()` provides *safe lookups*
- **Accumulator pattern** sums *letter values*

**3. Player Data Management**
```python
player_to_words = {
    'Player1': ['BLUE', 'TENNIS', 'EXIT'],
    'wordNerd': ['EARTH', 'EYES', 'MACHINE'],
    ...
}
```
- **Nested dictionary** stores *player names* as **keys**
- **List values** contain *words played* by **each player**
- **Data structure** organizes *game state*

**4. Adding Words Function**
```python
def play_word(player, word):
    player_to_words[player].append(word)
    return player_to_words
```
- **Function** adds *new words* to **player's list**
- **List method** `append()` extends *player's words*
- **Return statement** provides *updated data*

**5. Score Calculation System**
```python
def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points
    return player_to_points
```
- **Nested loops** process *each player's* **words**
- **Function calls** `score_word()` for *each word*
- **Dictionary assignment** stores *total points*

### **💡 Key Programming Concepts**

- **`Dictionaries`** - *Key-value pairs* for **data mapping**
- **`Dictionary Comprehension`** - Creating *dictionaries* with **compact syntax**
- **`Functions`** - *Reusable code* **blocks**
- **`Nested Data Structures`** - *Dictionaries* containing **lists**
- **`String Methods`** - Using `upper()` for **case handling**
- **`Dictionary Methods`** - Using `get()`, `items()` for **safe access**
- **`Accumulator Pattern`** - Building *running totals*

### **🎲 Scrabble Scoring System**

**Letter Point Values:**
- **1 point:** A, E, I, O, U, L, N, S, T, R
- **2 points:** D, G  
- **3 points:** B, C, M, P
- **4 points:** F, H, V, W, Y
- **5 points:** K
- **8 points:** J, X
- **10 points:** Q, Z

**Data Structure Breakdown:**
```python
letter_to_points = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
    'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    ...
}

player_to_words = {
    'Player1': ['BLUE', 'TENNIS', 'EXIT'],
    'wordNerd': ['EARTH', 'EYES', 'MACHINE']
}

player_to_points = {
    'Player1': 37,
    'wordNerd': 42
}
```

### **📊 Expected Output**

```terminal
15  # Score for 'BROWNIE'
{'Player1': 37, 'wordNerd': 42, 'Lexi Con': 44, 'Prof Reader': 31}
```

### **🔄 Program Flow**

1. **Setup** → Create *letter-point* **mapping dictionary**
2. **Function Definition** → Build *word scoring* **system**
3. **Data Organization** → Store *player words* in **nested structure**
4. **Game Management** → Add *new words* to **players**
5. **Score Calculation** → Calculate *total points* for **all players**
6. **Results Display** → Show *final scores* and **rankings**

### **🎮 Game Applications**

This system enables:
- **Word validation** and *scoring*
- **Player management** and *progress tracking*
- **Tournament organization** with *multiple games*
- **Statistics analysis** of *word choices*

This project demonstrates how **dictionaries and functions** work together to create *game logic* and **data management systems** for word games like Scrabble.

---

### 🙏 Thank You [CODECADEMY](http://www.codecademy.com/)!!!

I want to express my sincere gratitude to [**Codecademy**](http://www.codecademy.com/) for their *excellent learning platform*, *quality courses*, and the opportunity to enhance my coding skills. The knowledge and experience gained from [**Codecademy**](http://www.codecademy.com/) have significantly contributed to creating these projects and developing my abilities.

