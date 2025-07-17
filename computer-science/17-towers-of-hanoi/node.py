class Node:
  # Node class represents a single element in a linked list (used for Stack)

  def __init__(self, value, link_node=None):
    # Constructor: initializes the node with a value and an optional link to the next node
    self.value = value            # The data value stored in this node
    self.link_node = link_node    # Reference to the next node in the list (default: None)

  def set_next_node(self, link_node):
    # Sets the reference to the next node in the list
    self.link_node = link_node

  def get_next_node(self):
    # Returns the reference to the next node in the list
    return self.link_node

  def get_value(self):
    # Returns the value stored in this node
    return self.value