#Make a coin toss game where you need to guess if computer has selected 'heads' or 'tails' (0 or 1).

#Steps (for simplifying the code logic):

#Step 1: Print a welcoming message to the player.

#Step 2: Initialize variables to keep track of the number of correct guesses and the total number of guesses.

#Step 3: Use a while loop to keep the game running until the player decides to quit.

#Step 4: If the player enters 'quit', exit the game loop.

#Step 5: Ask the player to guess the outcome of the coin toss (heads or tails).

#Step 6: Generate a random number (0 or 1) to represent the outcome of the coin toss. (If the number is 0, the outcome is heads. If it's 1, the outcome is tails.)

#Step 7: Compare the player's guess with the generated outcome.

#Step 8: Increment the correct and total number of guesses

import random

print("Hello player! Let's play a coin toss game!")
print('I have tossed a coin and you need to guess if it landed heads on top or tails on top.. or on the edge!')

guesses_count = []

while True:
  random_num = random.randint(0, 1)
  guess = input('Please type "0" if you think it is HEADS, type "1" for TAILS, type "quit" to end the game! ')
  if guess == 'quit':
    print('Game over!')
    break

  try:
    guess = int(guess)
    guesses_count.append(guess)
    if guess == 0 or guess == 1:
      if guess == random_num and random_num == 0:
        print("You're correct! It was HEADS!")
        continue
      elif guess == random_num and random_num == 1:
        print("You're correct! It was TAILS!")
        continue
      else:
        print("Bad luck this time... Let's play again!")
      continue
    else:
      print('Please type 0 or 1! ')
      continue
  except:
    print('Wrong input! Please type 0 or 1, or "quit"! ')
    continue

print(f'Thank you for playing! You played {len(guesses_count)} times.')
