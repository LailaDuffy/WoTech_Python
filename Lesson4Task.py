
#1.Define a list of numbers [10, 20, 30, 40, 50].

#2.Print the length of the list.

#3.Print the first element of the list.

#4.Print the last element of the list.
#
#5.Append a new number (e.g., 60) to the list.

#6.Print the updated list.

#7.Remove the second element from the list.

#8.Print the list after removal.

#9.Check if a specific number (e.g., 30) exists in the list and print the result.

# task 1
numbers = [10, 20, 30, 40, 50]

# task 2
print(len(numbers))

# task 3
print(numbers[0])

# task 4
print(numbers[-1])

# task 5
numbers.append(60)

# task 6
print(numbers)

# task 7
numbers.pop(1)

# task 8
print(numbers)

# task 9
for num in numbers:
  if (num == 30):
    print(f'{num} exists in the list at index {numbers.index(num)}')
