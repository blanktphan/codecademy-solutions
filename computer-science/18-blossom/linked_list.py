class Node:
  def __init__(self, value):
    self.value = value  # Store the value of the node
    self.next_node = None  # Reference to the next node in the list, initially None
    
  def get_value(self):
    return self.value  # Return the value stored in this node
  
  def get_next_node(self):
    return self.next_node  # Return the reference to the next node
  
  def set_next_node(self, next_node):
    self.next_node = next_node  # Set the reference to the next node

class LinkedList:
  def __init__(self, head_node=None):
    self.head_node = head_node  # Reference to the first node in the list
  
  def insert(self, new_node):
    current_node = self.head_node  # Start from the head node

    if not current_node:
      self.head_node = new_node  # If the list is empty, set new_node as head

    while(current_node):
      next_node = current_node.get_next_node()  # Get the next node
      if not next_node:
        current_node.set_next_node(new_node)  # If at the end, link new_node
      current_node = next_node  # Move to the next node

  def __iter__(self):
    current_node = self.head_node  # Start from the head node
    while(current_node):
      yield current_node.get_value()  # Yield the value of each node
      current_node = current_node.get_next_node()  # Move to the
