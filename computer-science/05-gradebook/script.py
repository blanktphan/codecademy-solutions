# Previous semester data
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Current semester data
subjects = ['physics', 'calculus', 'poetry', 'history']  # List of subjects

grades = [98, 97, 85, 88]  # Corresponding grades

# Create gradebook combining subjects and grades
gradebook = [['physics', 98], ['calculus', 97], ['poetry', 85], ['history'], 88]

# Add new subjects to gradebook
gradebook.append(["computer science", 100])

gradebook.append(["visual arts", 93])

# Increase visual arts grade by 5 points (93 + 5 = 98)
gradebook[gradebook.index(['visual arts', 93])][1] += 5

# Remove numerical grade from poetry
gradebook[2].remove(85)

# Change poetry to Pass/Fail system
gradebook[2].append("Pass")

# Combine this semester with last semester
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)  # Display complete gradebook