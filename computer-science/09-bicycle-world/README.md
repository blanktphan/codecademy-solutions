# 👨‍💻 Project: Bicycle World

## 🎯 The Challenge from [Codecademy](http://www.codecademy.com/)

Welcome to Bicycle World, the premier text-based bicycle shop! This shop is only accessible to programmers like you, who are familiar with the command line.

In this project, you’ll use the commands you learned to navigate and edit the filesystem of this special shop.

The starting filesystem is shown below. (Bicycle World recently changed owners, who named the main directory bicycle-world-ii.)

```
bicycle-world-ii
|—— brands.txt
|—— freight/
|   |—— messenger/
|   |—— porteur/
|—— mountain/
|   |—— downhill/
|   |   |—— heavyweight/
|   |   |—— lightweight/
|   |—— hardtail/
|—— racing/
    |—— road/
    |—— track/

```

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

---

## 🔍 **Code Explanation (Generate by GitHub Copilot)**

The **Bicycle World project** uses **Bash shell commands** to navigate and manipulate the *file system* of a **bicycle shop directory structure**. Here's how it works:

### **📋 Complete Code Structure**

```bash
#!/bin/bash
pwd  # Print current working directory
# /home/ccuser/workspace/bicycle-world-ii

ls  # List files and directories in current location
# brans.txt freight mountain racing

cd freight  # Change directory to freight folder
ls  # List contents of freight directory
# messnger porteur

cd porteur  # Navigate into porteur subdirectory
cd ../..    # Go back two levels (parent of parent)

ls  # List current directory contents again
# brans.txt freight mountain racing

cd mountain/downhill  # Navigate to mountain/downhill path
touch dirt.txt  # Create new empty file dirt.txt
touch mud.txt   # Create new empty file mud.txt

ls  # List files in downhill directory
# dirt.txt heavyweight lightweight mud.txt

mkdir safety  # Create new directory named safety
pwd  # Show current location
# /home/ccuser/workspace/bicycle-world-ii/mountain/downhill/

cd ../..  # Go back to root bicycle-world directory
ls  # List root directory contents
# brans.txt freight mountain racing

mkdir bmx  # Create new directory named bmx
touch bmx/tricks.txt  # Create file tricks.txt inside bmx directory
ls  # List updated directory contents
```

### **🎯 How It Works**

**1. Directory Navigation**
```bash
pwd  # Print working directory
cd freight  # Change to freight directory
cd ../..  # Go up two directory levels
```
- **`pwd`** shows *current location* in the **file system**
- **`cd`** changes *directory* to specified **path**
- **`../..`** navigates *up two levels* in the **directory tree**

**2. File System Exploration**
```bash
ls  # List directory contents
cd freight
ls  # List contents of freight directory
```
- **`ls`** displays *files and folders* in **current directory**
- **Directory traversal** helps *explore* the **shop structure**

**3. File Creation**
```bash
touch dirt.txt  # Create empty file
touch mud.txt   # Create another file
```
- **`touch`** creates *new empty files* if they **don't exist**
- **File naming** follows *bicycle categories* and **product types**

**4. Directory Creation**
```bash
mkdir safety  # Create new directory
mkdir bmx     # Create bmx directory
```
- **`mkdir`** creates *new directories* in the **file system**
- **Organizing structure** for *different bicycle* **categories**

**5. Path Navigation**
```bash
cd mountain/downhill  # Navigate to specific path
cd porteur           # Move to subdirectory
```
- **Relative paths** move *through directory* **hierarchy**
- **Directory structure** reflects *bicycle shop* **organization**

### **💡 Key Command Line Concepts**

- **`pwd`** - Print *Working Directory* (shows **current location**)
- **`ls`** - *List* directory **contents**
- **`cd`** - *Change Directory* (navigate **file system**)
- **`touch`** - *Create* empty **files**
- **`mkdir`** - *Make* new **directories**
- **`../`** - *Parent directory* **navigation**
- **Path Navigation** - Moving through *directory* **hierarchies**

### **🚴 File System Structure**

**Original Structure:**
```
bicycle-world-ii/
├── brands.txt
├── freight/
│   ├── messenger/
│   └── porteur/
├── mountain/
│   ├── downhill/
│   │   ├── heavyweight/
│   │   └── lightweight/
│   └── hardtail/
└── racing/
    ├── road/
    └── track/
```

**After Script Execution:**
```
bicycle-world-ii/
├── brands.txt
├── bmx/                    # NEW
│   └── tricks.txt         # NEW
├── freight/
│   ├── messenger/
│   └── porteur/
├── mountain/
│   ├── downhill/
│   │   ├── dirt.txt       # NEW
│   │   ├── heavyweight/
│   │   ├── lightweight/
│   │   ├── mud.txt        # NEW
│   │   └── safety/        # NEW
│   └── hardtail/
└── racing/
    ├── road/
    └── track/
```

### **🔄 Command Execution Flow**

1. **Orientation** → Check *current location* with `pwd`
2. **Exploration** → List *directory contents* with `ls`
3. **Navigation** → Move through *directory structure* with `cd`
4. **File Creation** → Add *new files* with `touch`
5. **Directory Creation** → Add *new folders* with `mkdir`
6. **Structure Building** → Organize *bicycle shop* **categories**

### **📊 Command Summary**

| Command | Purpose | Example |
|---------|---------|---------|
| `pwd` | Show current location | `/home/user/bicycle-world-ii` |
| `ls` | List directory contents | `brands.txt freight mountain racing` |
| `cd` | Change directory | `cd mountain/downhill` |
| `touch` | Create empty file | `touch dirt.txt` |
| `mkdir` | Create directory | `mkdir safety` |
| `../` | Go to parent directory | `cd ../..` |

### **🛠️ Practical Applications**

This project demonstrates **command line skills** for:
- **File system navigation** in *development environments*
- **Directory organization** for *project structures*
- **File creation** and *management*
- **Path manipulation** and *relative navigation*
- **Shell scripting** for *automation tasks*

This **bash scripting exercise** shows how **command line tools** can efficiently manage *file systems* and **directory structures** in real-world scenarios.

---

### 🙏 **Thank You [Codecademy](https://www.codecademy.com/)**

I want to express my **sincere gratitude** to [**Codecademy**](https://www.codecademy.com/) for their **excellent learning platform**, **quality courses**, and the *opportunity to enhance my coding skills*. The **knowledge and experience** gained from [Codecademy](https://www.codecademy.com/) have **significantly contributed** to creating these projects and **developing my abilities**.