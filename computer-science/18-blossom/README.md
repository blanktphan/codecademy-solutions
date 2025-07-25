# 📋 Project: Blossom

## 🎯 The Challenge from [Codecademy](http://www.codecademy.com/)

---
## 🌸 Explore the Language of Flowers

Blossom lets you discover the fascinating symbolism behind flowers!  
Flower meanings, once hidden in ancient texts, are now accessible and interactive.

---

### 🗂️ What You'll Build

- **Hash Map:**  
    Link each flower name to its symbolic meaning.

- **Collision Handling:**  
    Use **separate chaining** with linked lists to resolve hash collisions (when two flower names share the same hash).

### ⚡ Why This Matters

- Efficient organization of flower data  
- Quick lookup for meanings  
- Learn practical data structure concepts

Uncover the hidden messages in flowers with Blossom!

---

## 🔍 Code Explanation (Generated by AI)

The Blossom program uses Python classes and data structures to create an interactive hash map that links flower names to their symbolic meanings. Here's how it works:

### 📋 Complete Code Structure

```python
from linked_list import Node, LinkedList

# HashMap class implements a basic hash map using separate chaining with linked lists
class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]

  def hash(self, key):
    return sum(key.encode())

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    list_at_array = self.array[array_index]
    for item in list_at_array:
        if key == item[0]:
            item[1] = value
            return
    payload = Node([key, value])
    list_at_array.insert(payload)

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    for item in list_at_index:
        if item[0] == key:
            return item[1]
    return None

from blossom_lib import flower_definitions 

blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy'))
```

### 🎯 How It Works

1. **HashMap Class**
   - Implements a hash map using an array of linked lists (separate chaining)
   - Handles collisions by storing multiple key-value pairs in a linked list at each array index
2. **Hashing & Compression**
   - Hashes each flower name to a numeric value
   - Compresses the hash to fit the array size using modulo
3. **Assign & Retrieve**
   - `assign(key, value)`: Adds or updates a flower's meaning in the hash map
   - `retrieve(key)`: Looks up the meaning for a given flower name
4. **Demo**
   - Loads flower definitions from `blossom_lib.py`
   - Inserts all flowers into the hash map
   - Prints the meaning of 'daisy' as an example

### 💡 Key Programming Concepts

- `Hash Map` - Fast lookup for key-value pairs
- `Separate Chaining` - Resolves hash collisions using linked lists
- `Linked List` - Flexible storage for multiple items at the same index
- `Modular Design` - Code is split into reusable components

### 🌸 Data Structure Design

HashMap Structure:
- Attributes: `array_size`, `array` (list of linked lists)
- Methods: `hash()`, `compress()`, `assign()`, `retrieve()`
- Behavior: Store and retrieve flower meanings efficiently

LinkedList & Node Structure:
- Used for chaining multiple key-value pairs at the same hash index

### 🔄 Program Flow

1. Create a HashMap sized to the number of flowers
2. Insert each flower and its meaning
3. Retrieve and print the meaning for a specific flower

### 🌼 Example Output

```terminal
daisy: innocence, purity, new beginnings
```

This project demonstrates how hash maps and linked lists can be combined for efficient data storage and lookup, making flower symbolism easy to explore interactively.

---

### 🙏 Thank You [Codecademy](https://www.codecademy.com/)

I want to express my sincere gratitude to [Codecademy](https://www.codecademy.com/) for their excellent learning platform, quality courses, and the opportunity to enhance my coding skills. The knowledge and experience gained from [Codecademy](https://www.codecademy.com/) have significantly contributed to creating these projects and developing my abilities.