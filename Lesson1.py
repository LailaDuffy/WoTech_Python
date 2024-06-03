# comment
this_is_a_greeting = "Good morning!"
print(this_is_a_greeting)

# variable naming - use snake_case, cannot start the name with a number
greeting = 14 # number value assigned to the same variable
print(greeting)

name = "Anna" #text/string
surname = "Johnson" #text/string
age = 35 #int
occupation = "programmer" #text/string
university_graduate = False #bool
height = 172.23 #float
print("Name: " + name, surname, age, occupation, university_graduate, height)
print(f"Full name: {name} {surname}\nOccupation: {occupation}\nUni degree: {university_graduate}\nHeight: {height}")

# We are preparing for a party
guest1 = "Anna"
guest2 = "John"
guest3 = "Jenny"

print(guest1, guest2, guest3)

guest_list = ['Anna', 'John', 'Jenny', 'Kerli', 'Madara'] # Strings can be defined with "" or '', in Python mostly used ''
print(guest_list)

for guest in guest_list:
  print(guest)
  
var_2 = 100
print(var_2)

name = 'trees ' * 10 # text can be multiplied to print as many times
print(name, end = '') # end = '' defines the end value in the print

name = input('Enter your name please: ') # requires user input and saves it as a variable
print(f'Hello, {name}, nice to meet you!') # f for formatted, called f-string

print('Hello, ', name, 'nice to meet you!') # formatting without f-string

print(f'Hello {name}, I would like to read the book "Hamlet"') # f-string with '' does not work if there is text in quot marks, for example 'Hamlet', then need to use double quot marks "Hamlet"

print("Anna", "Johnson")
print("Anna Johnson") # same result

name = "Anna"
surname = 'Johnson'
print(name, surname) # stores values in variables and transfers values to functions
print('Hello', name)
print('Hello', name, '!') # not great casuse ! doesn't need space before
print(f'Hello {name}!') # using f-string fixes the space issue before !
print('Hello', name, end='!') # works but is longer to type, and end='' removes the new line character \n
print('Hello', name, end='!\n') # now the following text is a new line
print(f'{name} wants to read "Hamlet"') # either use '' for f-string and "" for quot name OR "" for f-string and '' for quot name
