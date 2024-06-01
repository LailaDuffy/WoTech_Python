# USING LISTS

fruits = ['apple', 'orange', 'banana', 'grape', 'kiwi'] # creating a list object
# The user is prompted to enter a fruit name using the input() function. We use an if-else statement to check if the entered fruit is present in the fruits list. If the entered fruit is in the list, it prints a confirmation message. Otherwise, it prints a message indicating that the fruit is not in the list.

your_fruit = input('Please enter a fruit: ')
if your_fruit in fruits:
  print(f"Yes, {your_fruit} is in the list")
else:
  print(f"No, {your_fruit} isn't in the list")

# nested decision
numbers = [1, 2, 3, 4, 5]

# The user is prompted to enter a number using the input() function, and the input is converted to an integer using int(). We first check if the entered number is in the numbers list using an if statement. If the number is in the list, we further check if it's even or odd using another if-else statement nested inside the first one. Depending on the result, it prints a message indicating whether the number is even or odd and whether it's in the list or not.
your_number = int(input('Please write a whole number: '))

if your_number in numbers:
  if your_number % 2 == 0:
    print(f'{your_number} is in the list and it is an even number')
  else:
    print(f'{your_number} is in the list and it is an odd number')
else:
  print(f'{your_number} is not in the list')

# LIST METHODS

# APPEND METHOD

items = ['apple', 'kiwi', 'orange']
print(f'original items {items}') # prints the original list

my_value = 'banana'
items.append(my_value) # too add the new item to the end of the original list
print(f'changed items {items}')

# COPY

original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy() # copy of the original list
print(f'copy of the original list {copied_list}')

original_list.append(6)
print(f'original list {original_list}') # original list has been changed
print(f'copied list {copied_list}') # but it does not affect the copy of the original list

# COUNT

numbers = [1, 2, 7, 6, 5, 5]

print(f'The number 5 appears {numbers.count(5)} times in the list') # how many times an item appear in the list
print(f'THe list has {len(numbers)} items') # how many items in total there are in the list

# INDEX

fruits = ['apple','banana','orange']
fruits_index = fruits.index('banana') # to find the index of the defined item within a list

print(f'The index of banana is {fruits_index}')

# INSERT

numbers = [1, 2, 3, 4, 5]

numbers.insert(2, 10) # to insert number 10 in the 2nd index area .insert(index, new item)
print(numbers)

# REMOVE ---> POP

numbers.pop(2) # to get the item off the list, need to provide the index
print(numbers)

# SORT

numbers = [6,9,10,3,4]
print(numbers.sort())
print(numbers)

numbers = [2, 8, 30, 7, 44]

print(max(numbers))

print(min(numbers))

average = sum(numbers)/len(numbers)
print(average)

if average > 3:
  print(f'Average is greater than 3')
else:
  print(f' Average is not greater')

sorted = numbers.sort()
print(numbers)

numbers.pop(0)

numbers.insert(0, 'Laila')

numbers.index('Laila')
print(numbers)

# RANGE FUNCTION
# RANGE FUNCTION

list(range(0, 7, 1)) # range of sequence (first number, last number +1, step) needs to be in list object to iterate

numbers_with_range = range(1,7) # iterable object
for number in numbers_with_range: # use for:each loop to go through each element of the list, for example to double each element and print them
  number = number*2
  print(number)

