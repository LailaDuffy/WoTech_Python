student_names = ["Alice", "Bob", "Charlie", "David", "Eva"]
for name in student_names:
  print(f'Student name: {name}')

# WHILE LOOPS

# executes while the logical expression remains true
# infinite while loop
counter = 0 # initialize counter to see how many times the while loop has run
while True: # will run forever, until it's stopped manually
  counter = counter + 1
  print(counter)

counter = 0
while counter < 10: # a statement that will stop while loop when False
  counter = counter + 1
  print(counter)

counter = 0
while counter < 10:
  counter = counter + 1
  print(counter)
  break # break the while loop after the first iteration

counter = 0

while True:
  counter = counter + 1
  print(counter)
  if counter < 10:  # a statement that will break while loop when False
      continue # send the logic back up through the loop
  else:
      break # stops the loop

city = input('Write a city you have been to in LV or EE? To STOp write "stop". ')

if city == 'stop':
  print('You have written "stop".')
else:
  print(f'I have seen you have to been to the {city}.') # code stops after the first iteration

cities = []
counter = 0
while True: # code will continue executing until "stop"
  city = input('Write a city you have been to in LV or EE? To STOp write "stop". ')

  if city == 'stop':
    print('You have written "stop".')
    break
  else:
    cities.append(city)
    counter = counter + 1
    print(f'{counter}.I see you have been to {city}.') # counter can be replaced with len(cities)

print(f'You have been to {len(cities)} cities.')


# IMPORTING A LIBRARY

import random
random_number = random.randint(1, 101)
print(random_number)

random_number = random.randint(1, 101)
guesses_count = []

while True:
  guess = input('Guess the number between 1 and 100! To quit write "stop". ')
  if guess == 'stop':
      print('The game has been stopped.')
      break
  try:
    guess = int(guess)
  except:
    print('Please input a whole number!')
    continue
  guesses_count.append(guess)

  if guess == random_number:
      print('You have guessed it!')
      break
  elif guess > random_number:
      print('Too high! Try again!')
  else:
      print('Too low! Try again!')


print(f'You did {len(guesses_count)} guesses.')


