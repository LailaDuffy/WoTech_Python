if # TRUE
  #this code block will take place
elif # ELSE IF is TRUE
  #this code block will run
else # if, elif blocks are FALSE
  #this code block will run

# compare two numbers

num1 = int(input('Write number 1: '))
num2 = int(input('Write number 2: '))

if num1 >= num2:
  if num1 == num2:
    print(f'{num1} is equal to {num2}')
  else:
    print(f'{num1} is greater than {num2}')
else:
  print(f'{num1} is less than {num2}')

# TRY, EXCEPT and ELSE

stock = input('Stock: ')
try:
  product_stock = int(stock)
except:
  print('Wrong input')
else: # to make the rest of the code a part of the same code functionality
  if product_stock > 10:
    print('Stock level sufficient')
  else:
    print('Low stock')

#Prompt the user to enter their name, the speed limit (in km/h), and their actual speed (in km/h). Calculate the difference between the actual speed and the speed limit, and then calculate the fine based on the difference (3 euros per km/h over the limit). Handle potential non-integer inputs for speed limit and actual speed using a try block. If non-integer inputs are detected, set the speed limit to -1 to indicate wrong speed values. If the speed limit is -1, print "Wrong speed values entered. Please enter km/h." If the actual speed does not exceed the speed limit, print "Speed limit is not exceeded. No fine applied." If the actual speed exceeds the speed limit, check if the fine is less than or equal to 190 euros. If so, print "{name}, your fine for speeding is {fine} euros." - Otherwise, print "{name}, your fine for speeding is 190 euros."

name = input('Enter your name: ')

try:
  speed_limit = input('Enter the speed limit (km/h): ')
  actual_speed = input('Enter your actual speed (km/h): ')
except:
  print('Invalid input! Please write the speed as a whole number!')
else:
  actual_speed = int(actual_speed)
  speed_limit = int(speed_limit)
  if actual_speed > speed_limit:
    speed_difference = actual_speed - speed_limit
    fine = speed_difference * 3
    if fine > 190:
      print(f'{name}, your fine for speeding is 190 euros.')
    else:
      print(f'{name}, your fine for speeding is {fine} euros.')
  else:
    print('Speed limit is not exceeded. No fine applied.')

LISTS

# String of different flowers
flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"
print(type(flowers))

# List uses [] brackets and each item needs to be in ''
flowers = ['pink primrose','hard-leaved pocket orchid','canterbury bells','sweet pea','english marigold','tiger lily','moon orchid','bird of paradise','monkshood','globe thistle']
print(type(flowers))

# to find out how many items in the list
print(len(flowers))

# print first item from the list
print('First entry in the list flowers:', flowers[0])
# last entry
print('Last entry: ', flowers[-1])

print(flowers[:5]) # print up to iem no 5 of the list

print('Every other item:', flowers[::2]) # [start_index : end_index : step]

for item in flowers[::2]: # to print the list items without the list notation [ , , ]
  print(item)

my_list = ['one', 'two', 'three', 4, 5] # mixed type list

# print one to last element
print(my_list[-2])

# add new element to list
my_list +['new item'] # gets added to the end of the list

print(my_list) # new list wasn't saved, it needs to replace the old list

my_list = my_list + ['new item']
print(my_list)

# to replace an item into a list
my_list[1] = 2
print(my_list)

# append an item to the list
my_list.append('append me')
print(my_list)

# remove an item using pop method
my_list.pop(3) # to remove number 4 item

print(my_list)
