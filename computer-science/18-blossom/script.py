from linked_list import Node, LinkedList

# HashMap class implements a basic hash map using separate chaining with linked lists
class HashMap:
  def __init__(self, size):
    # Initialize the hash map with a fixed-size array of linked lists
    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]

  def hash(self, key):
    # Hash function: converts key to bytes and sums their values
    return sum(key.encode())

  def compress(self, hash_code):
    # Compress hash code to fit array size using modulo
    return hash_code % self.array_size

  def assign(self, key, value):
    # Assigns a value to a key in the hash map
    array_index = self.compress(self.hash(key))
    list_at_array = self.array[array_index]
    # Check if key already exists in the linked list
    for item in list_at_array:
        if key == item[0]:
            item[1] = value  # Update value if key found
            return
    # If key not found, insert new node with [key, value]
    payload = Node([key, value])
    list_at_array.insert(payload)

  def retrieve(self, key):
    # Retrieves the value associated with a key
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    # Search for the key in the linked list
    for item in list_at_index:
        if item[0] == key:
            return item[1]  # Return value if key found
    return None  # Return None if key not found


from blossom_lib import flower_definitions 

# Create a HashMap with size equal to the number of flower definitions
blossom = HashMap(len(flower_definitions))
# Insert each flower's name and definition into the hash map
for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

# Print the definition of 'daisy'
print(blossom.retrieve('daisy'))