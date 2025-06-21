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