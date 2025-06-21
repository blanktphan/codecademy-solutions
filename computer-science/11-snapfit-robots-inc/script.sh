# Initialize repository and create initial content
git init
git add .
git commit -m "Initial commit with robot assembly instructions"

# Create and switch to feature branch
git branch feature/assembly-updates
git checkout feature/assembly-updates

# Make changes to assembly instructions
# Edit robot assembly files
git add assembly_instructions.txt
git commit -m "Add detailed motor assembly steps"

# Switch between branches
git checkout main
git checkout feature/assembly-updates

# Merge feature branch into main
git checkout main
git merge feature/assembly-updates

# Delete merged feature branch
git branch -d feature/assembly-updates

# View branching history
git log --graph --oneline