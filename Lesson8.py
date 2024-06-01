my_dict = {} # defining dictionary
my_list = [] # defining list
my_tuple = () # defining tuple

my_tuple = (1, 2, 3)
print(my_tuple)

new_list = [1,2,3,4]
print(new_list)

# transform a list to tuple
new_tuple = tuple(new_list)
type(new_tuple) # now the list is a tuple

new_tuple[0] # accessing the first element of tuple, using index
new_tuple[0:3] # slicing a tuple

# other objects that can be transformed to tuple
# once an object is transformed to tuple, it CANNOT BE MODIFIED

# common functions for tuples
len(new_tuple) # length
min(new_tuple) # min value
max(new_tuple) # max value
sum(new_tuple) # sum

# new_tuple.append(1) # error, as tuple cannot be modifiend
# tuple == immutable


# dictionary is key & value pair
# create a dictionary
dictionary = {} # curly braces method
dictionary2 = dict() # using dictionary method

dictionary == dictionary2 # True

dictionary['key1'] = 'value1' # syntax
dictionary['key2'] = 'value2'

# can only access the elements by using a key
dictionary['key1']

# a key can store many values, e.g. list
dictionary['key3'] = [1,2,3]

# a key cannot be changed, but a value to an existing key can be changed

# storing a list in a dictionary
dictionary['datorium_list'] = ['Python', 'Java', 'C#']
dictionary

# the value can be overwritten
# cannot have two keys that are the same, each key in a dictionary is unique

dictionary['datorium_list'] = [1,2,3]

DICTIONARY METHODS

my_friends = {'Alice':30,
              'John':40,
              'Linda':28} # initializing dictionary

my_friends['Linda'] # how old is Linda

# update() - adds new dict to an existing one

incoming_friends = {'Arta': 28} # new friends dictionary
my_friends.update(incoming_friends) # updating the friends dictionary with new friends dictionary

integer_key = {123: 'name'} # int can also be a key
#pop() = removing an element pair from dictionary

my_friends.pop('Alice') # removes the key and a value
my_friends

# get() - to specify a fallback value when item is not in a dictionary
# my_freinds['Alice'] # KeyError 'Alice' as the element does not exist anymore

my_friends.get('Alice') # returns nothing, as they don't exist in the dict
my_friends.get('Alice', 'This person does not exist') # will return This person does not exist as it is set instead of the default value - nothing
my_friends.get('John', 'This person does not exist') # Will return John's age, as he exists in the dict

# items(), keys(), values()

# items(): Returns all key-value pairs
my_friends.items() # returns list of tuples

# keys(): Returns all keys
my_friends.keys()

# values(): Returns all values
my_friends.values()

EXERCISE - CREATE CONTACT BOOK

contact_book = {} # initiate

while True:
  name = input('Enter the name, write STOP to quit: ')
  if name == "STOP":
    print('Stopped the update')
    print(contact_book)
    break
  number = input('Enter the phone number: ')

  # new_dict = {name:number}
  # contact_book.update(new_dict) # a way to add the names to the contact dictionary

  contact_book[name] = number # adding the element to dictionary
  print(f'Contact {name} added successfully!')

FUNCTIONS

EXERCISE - STORE INVENTORY MANAGEMENT
inventory = {}
# function of adding an item to a dictionary
def add_item(inventory):
  key = input('Enter the item name: ')
  value = input('Enter the amount: ')

  new_dict = {key:value}
  inventory.update(new_dict) # a way to add the names to the contact dictionary

  print(f'Item {key} added successfully!')

while True:
    exit = input('Enter YES to start, write STOP to quit: ')
    if exit == "STOP":
      print('Stopped the inventory update')
      print('Final inventory list: ', inventory)
      break
    add_item(inventory) # calling a function

