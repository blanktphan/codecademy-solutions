# Scrabble letter values setup
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Create letter-to-points mapping dictionary
letter_to_points = {key:value for key,value in zip(letters, points)}

letter_to_points[' '] = 0  # Blank tiles worth 0 points

# Function to calculate word score
def score_word(word):
  point_total = 0
  for letter in word.upper():  # Convert to uppercase
      if letter_to_points.get(letter, 0):  # Safe dictionary lookup
        point_total += letter_to_points[letter]  # Add letter points
  return point_total

brownie_points = score_word('BROWNIE')  # Test word scoring

print(brownie_points)

# Player game data - nested dictionary structure
player_to_words = {
  'Player1': ['BLUE', 'TENNIS', 'EXIT'],
  'wordNerd': ['EARTH', 'EYES', 'MACHINE'],
  'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'],
  'Prof Reader': ['ZAP', 'COMA', 'PERIOD']
}

# Function to add words to player
def play_word(player, word):
  player_to_words[player].append(word)  # Add word to player's list
  return player_to_words

player_to_points = {}  # Dictionary to store player scores

# Function to calculate all player totals
def update_point_totals():
  for player, words in player_to_words.items():  # Iterate through players
    player_points = 0
    for word in words:  # Calculate points for each word
      player_points += score_word(word)
    player_to_points[player] = player_points  # Store total score
  return player_to_points

