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