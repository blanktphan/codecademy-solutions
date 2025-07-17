
# Import the Node class to build the linked list structure for the stack
from node import Node

class Stack:
  # Stack class implements a stack data structure using a singly linked list
  def __init__(self, name):
    # Constructor: initializes an empty stack with a name and a size limit
    self.size = 0              # Number of items in the stack
    self.top_item = None       # Reference to the top Node in the stack
    self.limit = 1000          # Maximum number of items allowed in the stack
    self.name = name           # Name of the stack (for display purposes)
  
  def push(self, value):
    # Push: Add a new value to the top of the stack if there is space
    if self.has_space():
      item = Node(value)                  # Create a new node with the given value
      item.set_next_node(self.top_item)   # Link new node to the current top
      self.top_item = item                # Update the top to the new node
      self.size += 1                      # Increment the stack size
    else:
      print("No more room!")              # Stack is full

  def pop(self):
    # Pop: Remove and return the value at the top of the stack if not empty
    if self.size > 0:
      item_to_remove = self.top_item                # Node to remove
      self.top_item = item_to_remove.get_next_node()# Move top to next node
      self.size -= 1                                # Decrement the stack size
      return item_to_remove.get_value()             # Return the value of the removed node
    print("This stack is totally empty.")           # Stack is empty

  def peek(self):
    # Peek: Return the value at the top of the stack without removing it
    if self.size > 0:
      return self.top_item.get_value()
    print("Nothing to see here!")  # Stack is empty

  def has_space(self):
    # Returns True if the stack has space for more items, False if full
    return self.limit > self.size

  def is_empty(self):
    # Returns True if the stack is empty, False otherwise
    return self.size == 0
  
  def get_size(self):
    # Returns the current number of items in the stack
    return self.size
  
  def get_name(self):
    # Returns the name of the stack (useful for display)
    return self.name
  
  def print_items(self):
    # Prints the items in the stack from bottom to top
    pointer = self.top_item
    print_list = []
    while(pointer):
      print_list.append(pointer.get_value())
      pointer = pointer.get_next_node()
    print_list.reverse()  # To display from bottom to top
    print("{0} Stack: {1}".format(self.get_name(), print_list))