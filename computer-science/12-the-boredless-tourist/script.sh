#!/bin/bash
git init  # Initialize new Git repository

git add script.py  # Stage initial Python file

git commit -m "initial commit"  # Create first commit

git add script.py  # Stage updated file

git commit -m "Added test objects"  # Commit traveler test data

git add script.py  # Stage file changes

git commit -m "Added logic to find traveler destinations and convert to internal data"  # Commit destination functions

git add script.py  # Stage next changes

git commit -m "Created attractions and functionality for adding new attractions"  # Commit attraction management

git add script.py  # Stage updated code

git commit -m "Added interest finder logic"  # Commit matching algorithm

git add script.py  # Stage final changes

git commit -m "Added function to generate message for traveler and present attractions they might be interested in."  # Commit recommendation engine