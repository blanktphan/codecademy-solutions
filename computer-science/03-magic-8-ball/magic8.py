import random  # Import random module for generating random numbers

name = "Blank"  # Person asking the question
question = "Blank is handsome?"  # Question to ask the Magic 8-Ball
answer = ''  # Variable to store the Magic 8-Ball's response

# Generate random number between 1 and 9
random_number = random.randint(1, 9)

# Use if/elif statements to assign different answers based on random number
if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2:
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = 'Without a doubt'
elif random_number == 4:
  answer = 'Reply hazy, try again'
elif random_number == 5:
  answer = 'Ask again later'
elif random_number == 6:
  answer = 'Better not tell you now'
elif random_number == 7:
  answer = 'My sources say no'
elif random_number == 8:
  answer = 'Outlook not so good'
elif random_number == 9:
  answer = 'Very doubtful'
else:
  print('Error')  # Fallback for unexpected values

# Display the question with or without name
if name == '':
    print('Question: ' + question)  # Anonymous question
else:
    print(name + ' asks: ' + question)  # Named question

print('Magic 8-Ball\'s answer: ' + answer)  # Display the random answer