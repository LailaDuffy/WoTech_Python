x = 5 # '=' to assign a variable
y = 5

# eaqual to
print(x == 5) # '==' compare two values
print('1' == 1)

# not eaqual to

print(x != y)

# greater than

print(x > y)
print(x > 2)

# less than

print(x < y)
print(x < 10)

# greater/less than or eaqual to

print(x >= 6)
print(y <= 6)

# IF ELSE statements

x = 100

if x < 50:
  print('Less than 50') # must have an indent in Python to have the statement only assigned to the 'if' block
else:
  print('More than or equal to 50') # the statement only assigned to the 'else' block
print('Finished') # printed every time as outside the if else blocks

a = 20

if a > 10:
  print('a is above 10')
  print('still part of the if block')
print('this is outside if block')

age = int(input('How old are you? '))

if age >= 18:
  print('You are eligible to vote')
  print('Please proceed to the voting booth')
else:
  print('You are not eligible to vote')
  print("Please return when you've reached 18 years of age")
print('Thank you for participating')

# modulus operator 4:2 = 2, modulus 0, for 3:2 = 1, modulus 1

number = int(input('ENter a whole number: '))

# check if number is even or odd

if number % 2 == 0:
  print(f'The number {number} is even!')
else:
  print(f'The number {number} is odd!')

# PAYMENT APPROVAL
# if the transaction can be done based on the account balance

account_balance = float(input('Enter your account balance: '))
transaction_amount = float(input('Enter the transaction amount: '))

if account_balance >= transaction_amount:
  print('Transaction is approved')
else:
  print('Transaction is not approved. Insufficient balance')

# access management system
# username
# password
# check if username and password match the stored credentials

username = input('Enter your username: ')
password = input('Enter your password: ')

STORED_USERNAME = 'user123' # capitals because its hardcoded/global variable
STORED_PASSWORD = 'pass123'

# AND
if STORED_USERNAME == username and STORED_PASSWORD == password:
  print('You are logged in')
else:
  print('Log in credentials incorrect. Access denided.')

# MULTIWAY DECISIONS
# ELIF == else if

x = 10
if x < 5:
  print('small')
elif x < 15:
  print('medium')
else:
  print('large')

print('All done!')

# Grading Task
# grading in scale 100, convert 100 to ABCDEF

# TRY & EXCEPT
# TO USE TRY CODE THE WHOLE BLOCK MUST BE INDENTED
try:
  score = int(input('Enter your score: '))

  if score >= 90:
    print('Grade is A!')
  elif score >= 80:
    print('Grade is B!')
  elif score >= 70:
    print('Grade is C!')
  elif score >= 60:
    print('Grade is D!')
  elif score >= 50 and score < 60:
    print('Grade is E!')
  else:
    print('Grade is F!')
except Exception as e: # use codewoed EXCEPTION AS to catch the error as a variable and print later for clarity
  print(f'Wrong input received! The exception is {e}')

try:
  account_balance = float(input('Enter your account balance: '))
  transaction_amount = float(input('Enter the transaction amount: '))

  if account_balance >= transaction_amount:
    print('Transaction is approved')
  else:
    print('Transaction is not approved. Insufficient balance')
except Exception as e:
  print(f'Wrong input. Exception was {e}')

GROUP TASK
# Team work: Create a Python program for temperature conversion between Celsius and Fahrenheit scales.
# The program should prompt users to select the direction of conversion, accept input for the temperature value, and accurately perform the conversion (use IF and/or ELSE).
# Output should be displayed with formatted strings showing both the original and converted temperatures.

print('Temperature Conversion Calculator')
print()
print('To convert from Celsius to Farenheit please type: F')
print('To convert from Farenheit to Celsius please type: C')

try:

  temp_scale = input('Please choose the conversion: ')

  if temp_scale == 'F':
    degC = float(input('Please enter the temperature in °C: '))
    degF = round((degC * 9/5 + 32), 1)
    print(f'Temperature in Celsius: {degC}°C\nTemperature in Fahrenheit: {degF}°F')
  elif temp_scale == 'C':
    degF = float(input('Please enter the temperature in °F: '))
    degC = round((5/9 * (degF - 32)), 1)
    print(f'Temperature in Farenheit: {degF}°F\nTemperature in Celsius: {degC}°C')
  else:
    print('Invalid conversion character!')

except Exception as e:
  print(f'Wrong input! The exception is {e}')
