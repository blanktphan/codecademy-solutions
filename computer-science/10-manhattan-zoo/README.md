# 👨‍💻 Project: Manhattan Zoo

## 🎯 The Challenge from [Codecademy](http://www.codecademy.com/)

Ready to explore Git version control? 🚀

In this hands-on project, you'll master **Git fundamentals** by managing *meal guidelines* for animals at the **Manhattan Zoo**. You'll learn to:

- **Initialize** a Git repository for tracking changes
- **Stage and commit** animal feeding schedules  
- **Navigate through** project history and versions
- **Compare differences** between file modifications
- **Manage documentation** using professional Git workflows

This practical exercise demonstrates how **version control** works in real-world scenarios, giving you essential skills for software development and project management.

---

## 🔍 **Code Explanation (Explanation by GitHub Pilot)**

The **Manhattan Zoo project** uses **Git version control** to track and manage *animal meal guidelines* for **zoo operations**. Here's how it works:

### **📋 Git Workflow Structure**

```bash
# Initialize Git repository
git init

# Check repository status
git status

# Add files to staging area
git add filename.txt
git add .  # Add all files

# Create commits with messages
git commit -m "Add initial meal guidelines"
git commit -m "Update feeding schedules"

# View commit history
git log
git log --oneline

# Check differences between versions
git diff HEAD~1
git diff filename.txt

# Navigate between commits
git checkout commit_hash
git checkout main

# View file contents at different commits
git show HEAD:filename.txt
git show commit_hash:filename.txt
```

### **🎯 How Git Works**

**1. Repository Initialization**
```bash
git init
```
- **Creates** a *new Git repository* in **current directory**
- **Sets up** *.git folder* for **version tracking**
- **Enables** *version control* for **project files**

**2. File Tracking and Staging**
```bash
git status  # Check current state
git add meal_guidelines.txt  # Stage specific file
git add .  # Stage all modified files
```
- **`git status`** shows *modified*, *staged*, and **untracked files**
- **`git add`** moves *files* to **staging area** for commit
- **Staging area** prepares *changes* for **permanent recording**

**3. Creating Commits**
```bash
git commit -m "Add lion feeding schedule"
git commit -m "Update elephant meal portions"
```
- **Commits** create *permanent snapshots* of **staged changes**
- **Commit messages** describe *what changes* were **made**
- **Each commit** has *unique hash* for **identification**

**4. Viewing History**
```bash
git log  # Detailed commit history
git log --oneline  # Condensed one-line format
```
- **`git log`** shows *chronological history* of **all commits**
- **Displays** *commit hashes*, *messages*, *authors*, and **timestamps**

**5. Comparing Versions**
```bash
git diff  # Show unstaged changes
git diff HEAD~1  # Compare with previous commit
git diff commit1 commit2  # Compare specific commits
```
- **`git diff`** reveals *line-by-line changes* between **versions**
- **Helps identify** *what was modified* between **commits**

### **💡 Key Git Concepts**

- **`Repository`** - *Project folder* with **version control**
- **`Working Directory`** - *Current files* you're **editing**
- **`Staging Area`** - *Temporary space* for **commit preparation**
- **`Commits`** - *Permanent snapshots* of **project state**
- **`HEAD`** - *Pointer* to **current commit**
- **`Hash`** - *Unique identifier* for **each commit**
- **`Branch`** - *Parallel version* of **project history**

### **🦁 Zoo Project Workflow**

**1. Initial Setup**
- **Create** *meal guidelines* for **different animals**
- **Initialize** *Git repository* for **tracking changes**

**2. File Management**
- **Add** *feeding schedules* for **lions, elephants, bears**
- **Track** *portion sizes* and **dietary requirements**

**3. Version Control**
- **Commit** *initial guidelines* with **descriptive messages**
- **Update** *meal plans* based on **veterinary advice**
- **Track** *seasonal changes* in **animal diets**

**4. History Tracking**
- **Review** *previous versions* of **feeding guidelines**
- **Compare** *changes* between **different time periods**
- **Restore** *previous versions* if **needed**

### **📊 Git Commands Summary**

| Command | Purpose | Example |
|---------|---------|---------|
| `git init` | Initialize repository | Create new Git repo |
| `git status` | Check file states | See modified files |
| `git add` | Stage changes | `git add lion_meals.txt` |
| `git commit` | Save snapshot | `git commit -m "Update portions"` |
| `git log` | View history | See all commits |
| `git diff` | Compare versions | Show file changes |
| `git checkout` | Switch versions | Go to specific commit |

### **🔄 Version Control Flow**

1. **Create/Modify Files** → Edit *animal meal guidelines*
2. **Stage Changes** → Use `git add` to **prepare commits**
3. **Commit Changes** → Use `git commit` with **descriptive messages**
4. **Review History** → Use `git log` to **track progress**
5. **Compare Versions** → Use `git diff` to **see changes**
6. **Navigate History** → Use `git checkout` to **view past versions**

### **📝 Expected Git Output**

```bash
$ git status
On branch main
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)
        new file:   lion_meals.txt
        modified:   elephant_diet.txt

$ git log --oneline
a1b2c3d Add feeding schedule for new tigers
e4f5g6h Update elephant portion sizes
i7j8k9l Initial meal guidelines for all animals
```

### **🏗️ Practical Applications**

This project demonstrates **version control** for:
- **Document management** in *organizational settings*
- **Tracking changes** to *important guidelines*
- **Collaboration** on *shared documents*
- **Backup and recovery** of *critical information*
- **Audit trails** for *regulatory compliance*

This **Git project** shows how **version control systems** can manage *any type of content* and provide **powerful tracking capabilities** for teams and organizations.

---

### 🙏 **Thank You, [Codecademy](https://www.codecademy.com/)**

I want to express my **sincere gratitude** to [**Codecademy**](https://www.codecademy.com/) for their **excellent learning platform**, **quality courses**, and the *opportunity to enhance my coding skills*. The **knowledge and experience** gained from [Codecademy](https://www.codecademy.com/) have **significantly contributed** to creating these projects and **developing my abilities**.