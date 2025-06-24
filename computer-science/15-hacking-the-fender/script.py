import csv
import json

compromised_users = []

# Read usernames from CSV password file
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)  # Create CSV reader
  for password_row in password_csv:
    compromised_users.append(password_row['Username'])  # Extract usernames
  
# Write compromised users to text file
with open('compromised_users.txt', 'w') as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user)  # Write each username
    compromised_user_file.write('\n')  # Add newline
  
# Create JSON message for boss
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {'recipient': 'The Boss', 'message': 'Mission Success'}
  json.dump(boss_message_dict, boss_message)  # Write JSON data

# Write hacker signature to new passwords file
with open('new_passwords.csv', 'w') as new_passwords_obj:
  slash_null_sig = '''
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/

  '''  # ASCII art signature
  new_passwords_obj.write(slash_null_sig)  # Write signature to file