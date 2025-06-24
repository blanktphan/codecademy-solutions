# 👨‍💻 Project: Hacking The Fender

## 🎯 The Challenge from [Codecademy](http://www.codecademy.com/)

The Fender, a notorious computer hacker and general villain of the people, has compromised several top-secret passwords including your own. Your mission, should you choose to accept it, is threefold. You must acquire access to The Fender‘s systems, you must update his "passwords.csv" file to scramble the secret data. The last thing you need to do is add the signature of Slash Null, a different hacker whose nefarious deeds could be very conveniently halted by The Fender if they viewed Slash Null as a threat.

Use your knowledge of working with Python files to retrieve, manipulate, obscure, and create data in your quest for justice. Work with CSV files and other text files in this exploration of the strength of Python file programming.

If you get stuck during this project, check out the project walkthrough video which can be found in the help menu.

---

## 🔍 **Code Explanation**

The **Hacking The Fender program** uses **Python file I/O operations** to investigate *security breaches* and manipulate **different file formats** for cybersecurity analysis. Here's how it works:

### **📋 Complete Code Structure**

```python
import csv
import json

compromised_users = []

# Read usernames from CSV password file
with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    for password_row in password_csv:
        compromised_users.append(password_row['Username'])

# Write compromised users to text file
with open('compromised_users.txt', 'w') as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(user)
        compromised_user_file.write('\n')

# Create JSON message for boss
with open('boss_message.json', 'w') as boss_message:
    boss_message_dict = {'recipient': 'The Boss', 'message': 'Mission Success'}
    json.dump(boss_message_dict, boss_message)

# Write hacker signature to new passwords file
with open('new_passwords.csv', 'w') as new_passwords_obj:
    slash_null_sig = '''
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
    '''
    new_passwords_obj.write(slash_null_sig)
```

### **🎯 How It Works**

**1. CSV File Reading**
```python
import csv
with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    for password_row in password_csv:
        compromised_users.append(password_row['Username'])
```
- **CSV module** imports for *structured data* **processing**
- **Context manager** `with open()` ensures *proper file* **closure**
- **DictReader** treats *CSV rows* as **dictionaries**
- **Data extraction** pulls *usernames* from **password records**

**2. Text File Writing**
```python
with open('compromised_users.txt', 'w') as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(user)
        compromised_user_file.write('\n')
```
- **Write mode** `'w'` creates *new file* or **overwrites existing**
- **Loop iteration** writes *each username* **separately**
- **Newline characters** format *output* for **readability**

**3. JSON Data Creation**
```python
import json
boss_message_dict = {'recipient': 'The Boss', 'message': 'Mission Success'}
json.dump(boss_message_dict, boss_message)
```
- **JSON module** handles *structured data* **serialization**
- **Dictionary creation** stores *message data*
- **JSON dump** writes *Python objects* as **JSON format**

**4. ASCII Art Signature**
```python
slash_null_sig = '''
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
...
'''
new_passwords_obj.write(slash_null_sig)
```
- **Multi-line string** contains *ASCII art* **signature**
- **File writing** adds *hacker signature* to **evidence file**
- **Obfuscation technique** for *investigation scenario*

### **💡 Key Programming Concepts**

- **`File I/O`** - *Reading* and **writing files**
- **`Context Managers`** - Using `with` statements for *safe file* **handling**
- **`CSV Processing`** - Working with *structured data* **files**
- **`JSON Handling`** - *Serializing* and **deserializing data**
- **`File Modes`** - Understanding `'r'`, `'w'` for **different operations**
- **`Import Statements`** - Using *external modules* like **csv and json**
- **`Multi-line Strings`** - Creating *formatted text* **blocks**

### **🕵️ Security Investigation Workflow**

**1. Evidence Collection**
- **Read compromised** *password file*
- **Extract usernames** from *CSV data*
- **Build list** of *affected users*

**2. Report Generation**
- **Write user list** to *text file*
- **Create JSON** *status message*
- **Document findings** for *investigation*

**3. Counter-Intelligence**
- **Plant false** *evidence*
- **Add signature** of *different hacker*
- **Mislead investigation** with *fake clues*

### **📊 File Format Handling**

| Format | Purpose | Method |
|--------|---------|--------|
| CSV | Password data | `csv.DictReader()` |
| TXT | User list | `file.write()` |
| JSON | Status message | `json.dump()` |

### **🔄 Program Flow**

1. **Import Modules** → Load *csv* and **json libraries**
2. **Read CSV** → Extract *usernames* from **password file**
3. **Process Data** → Build *compromised users* **list**
4. **Write Text** → Create *investigation* **report file**
5. **Create JSON** → Generate *status message* **data**
6. **Plant Evidence** → Add *fake hacker* **signature**

### **🛡️ Cybersecurity Applications**

This investigation workflow demonstrates:
- **Data forensics** techniques for *security analysis*
- **File manipulation** for *evidence processing*
- **Multi-format** *data handling* in **investigations**
- **Counter-intelligence** methods for *misdirection*

This project shows how **file I/O operations** can be used for *cybersecurity investigations* and **data manipulation** in security scenarios.

---

### 🙏 **Thank You [Codecademy](https://www.codecademy.com/)**

I want to express my **sincere gratitude** to [**Codecademy**](https://www.codecademy.com/) for their **excellent learning platform**, **quality courses**, and the *opportunity to enhance my coding skills*. The **knowledge and experience** gained from [Codecademy](https://www.codecademy.com/) have **significantly contributed** to creating these projects and **developing my abilities**.

