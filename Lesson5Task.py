import random

numbers = []
for number in range(10):
  numbers.append(random.randint(1,100))
for number in numbers:
  if number > 5:
    print(f'{number} is bigger than 5')
  elif number < 5:
    print(f'{number} is smaller than 5')
  else:
    print(f'{number} is equal to 5')
