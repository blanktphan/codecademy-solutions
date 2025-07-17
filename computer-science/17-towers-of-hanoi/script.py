from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# Create the Stacks for the game (Left, Middle, Right)
stacks = []
left_stack = Stack('Left')      # Stack for the left pole
middle_stack = Stack('Middle')  # Stack for the middle pole
right_stack = Stack('Right')    # Stack for the right pole
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))  # Ask user for number of disks
while (num_disks < 3):  # Ensure at least 3 disks for a valid game
  num_disks = int(input("Enter a number greater than or equal to 3\n"))
for disk in range(num_disks, 0, -1):  # Add disks to the left stack (largest at the bottom)
  left_stack.push(disk)
num_optimal_moves = (2**left_stack.get_size()) - 1  # Calculate minimum moves required
print("\nThe fastest you can solve this game is in {} moves".format(num_optimal_moves))

# Function to get user input for stack selection
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]  # First letter of each stack name
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print('Enter {} for {}'.format(letter, name))  # Show choices to user
    user_input = input("")
    if user_input in choices:  # Validate input
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]  # Return selected stack

# Play the Game
num_user_moves = 0  # Track number of moves made by user
while right_stack.get_size() != num_disks:  # Continue until all disks are moved to right stack
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()  # Display current state of all stacks
  while True:
    print("\nWhich stack do you want to move form?\n")
    from_stack = get_input()  # Get source stack from user
    print(("\nWhich stack do you want to move to?\n"))
    to_stack = get_input()    # Get destination stack from user
    if from_stack.is_empty():  # Check if source stack is empty
      print("\n\nInvalid Move. Try Again")
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():  # Valid move if destination is empty or top disk is larger
      disk = from_stack.pop()  # Remove disk from source
      to_stack.push(disk)      # Add disk to destination
      num_user_moves += 1      # Increment move counter
      break
    else:
      print("\n\nInvalid Move. Try Again")  # Invalid move (can't place larger disk on smaller)
print('\n\nYou completed the game in {} moves, and the optimal number of moves is {}'.format(num_user_moves, num_optimal_moves))