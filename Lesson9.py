# defining function with def
# this function is void, it does not return a value
def cleaner(item, fluid, times): # defining and naming the function, and providing a (parameter)
  print(f'I have cleaned the {item} with {fluid} {times} times.')
  print(type(item))
  print(type(fluid))
  print(type(times))


# parameter data types can be anything, can write (item: str, fluid: str, times: int) but it only gives an information of data type and does not enfore it
# the function has to be called to be run
cleaner('smartphone', 'water', 5)

# a function that returns a value
def sum_two_numbers(number1, number2):
  return number1 + number2

sum_two_numbers(4, 5) # returns value to function call, but does not show it
print(sum_two_numbers(4,5)) # need to use print function to see the result

class Cat: # class name is capitalized
  def __init__(self, name, age): # defining standard method (constructor) of the class
  # this method runs authomatically when an object from this class is created
  # (self) is a required parameter and refers to the instance, it's best to use 'self' as it's a naming convention
  # name and age are constructor paramaters that must be passed when constructor is called, these parameters do not belong to the class but the object created form the class
    #pass # means do nothing
    self.name = name
    self.age = age
    # as it is not defined as a parameter, it is not necessary for an object to be created
    self.sound = 'Meow' # assigning a default sound, it cannot be overwritten

  # defining a custom method
  def voice(self):
    print(f'{self.sound}!')

  def eat(self, food):
    print(f'{self.name} is eating {food}')

  def introduce(self, fav_food):
    print(f'Hi, my name is {self.name}. I am {self.age} years old. My favourite food is {self.eat(fav_food)}.')

# creating instances of class Cat called objects
cat1 = Cat('Minka', 6)
cat2 = Cat('Miisu', 1)
cat3 = Cat('Muris', 8)

# read the instance/object variables
print(cat1.name)
print(cat2.age)

# gives the location in the memory
print(cat1)

# calling the custom "voice" method
cat3.voice()
cat1.voice()

# calling eat method
cat2.eat('fish')

# calling introduce method
cat1.introduce('fish')
