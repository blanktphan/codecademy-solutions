# Cat class definition with attributes and methods
class Cat():
  def __init__(self, name, old, color):  # Constructor with cat properties
    self.name = name
    self.old = old
    self.color = color

  def info(self):  # Display cat information
    print('This cat is name {}, color is {}. and {} year old'.format(self.name, self.color, self.old))

  def moew(self):  # Cat sound method
    print('{}: say moew!'.format(self.name))

  def birthday(self):  # Age increment method
    now = self.old + 1
    print('Now {} has growth up from {} to {}'.format(self.name, self.old, now))
    self.old = now

  def __repr__(self):  # String representation method
    return 'This cat is name {}. and {} year old.'.format(self.name, self.old)

# Person class definition with cat ownership
class Person():
  def __init__(self, name, old):  # Constructor with person properties
    self.name = name
    self.old = old
    self.owner = []  # List to store owned cats

  def info(self):  # Display person information
    print('This person is name {},owner cat is {} now  and {} year old.'.format(self.name, self.owner, self.old))

  def addCat(self, name):  # Method to add cat ownership
    if type(name) is Cat:  # Type checking for Cat objects
      self.owner.append(name.name)

  def birthday(self):  # Age increment method
    now = self.old + 1
    print('Now {} has growth up from {} to {}'.format(self.name, self.old, now))
    self.old = now

  def __repr__(self):  # String representation method
    return 'this person is name {}. and owner cat is {}'.format(self.name, self.owner)

# Create object instances
cat1 = Cat('preem', 0, 'black')  # Black cat named preem
cat2 = Cat('AA', 1, 'white')     # White cat named AA
person1 = Person('Thai', 20)     # Person named Thai
person2 = Person('Next', 20)     # Person named Next

# Test object methods
cat1.info()          # Display cat info
cat1.birthday()      # Age the cat
cat1.info()          # Show updated info
cat1.moew()          # Make cat sound

person1.addCat(cat1) # Add cat to person's ownership
print(person1)       # Display person with cat