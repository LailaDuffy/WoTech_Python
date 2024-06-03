# DATA TYPES

# data type integer - whole numbers, can be negative or positive
x = 14
print(x)
print(type(x))

x1 = -1
print(type(x))

# data type float - decimal numbers
nearly_pi = 3.14
print(nearly_pi)
print(type(nearly_pi))

nearly_pi1 = 22/7
print(nearly_pi1)
print(type(nearly_pi1))

# how to round the float up to 2 decimal places
rounded_nearly_pi1 = round(nearly_pi1, 2) # round function needs the variable to be rounded  and how many decimals after the coma, default is 0
print(rounded_nearly_pi1)

type(round(nearly_pi1)) # float rounded with default decimals (0) becomes int type
print(type(round(nearly_pi1)))
type(round(nearly_pi1, 0)) # float rounded with decimals definded (even if 0) it stays float type
print(type(round(nearly_pi1, 0)))

# Booleans
bool1 = False # true/false needs to be with capital letters True/False

print(bool1)
print(type(bool1))
print()

bool2 = (1 < 2)
print(bool2)
print(type(bool2))
print()

bool3 = (5 < 3)
print(bool3)
print()

bool4 = not bool3 # opposite to the variable
print(bool4)
print()

# Adding boolean
# True == 1
# False == 0
bool5 = True + False + True
# bool5 = 1 + 0 + 1
print(bool5)
print()

# OR boolean
bool6 = True or False or True
print(bool6)

# strings
string1 = 'Hello'
print(string1)
print(type(string1))
print()

# counts and prints how many characters are in the string
print(len(string1))
print()

nearly_pi_string = '3.14'
print(type(nearly_pi_string))
print()

# cast string to float
nearly_pi_string_converted = float(nearly_pi_string)
print(type(nearly_pi_string_converted))
print()

# string concatination with "+" sign
new_string = 'abc' + 'def'
print(new_string)

# Arithmetic calculations
# addition
a = 5
b = 3
sum = a + b
print(f'SUM: {sum}')
print()

# substraction
difference = a - b
print(f'DIFFERENCE: {difference}')
print()

# multiplication
multiply = a * b
print(f'MULTILPY RESULT: {multiply}')
print()

# division
divide = a/b
print(f'DIVIDE RESULT: {divide}')
print()

# exponentials
power = a ** b
print(f'EXPONENSION: {power}')

# !!!ALL USER INPUTS ARE SAVED AS STRINGS!!!
input1 = input('How old are you? ')
input2 = input('How old am I? ')
sum = input1 + input2 # this will concatinated the two strings
print(input1)
print(type(input1))
print(sum)
print()

# if need a number, MUST CAST INTO INT, FLOAT ETC.
input1_int = int(input1)
input2_int = int(input2)
sum_inputs = input1_int + input2_int
print(f'Our ages added together are: {sum_inputs}')

# Density
area = int(input('Enter area size: '))
population = int(input('Enter the population amount: '))

density = population / area

print(f'Average density is: {density}')

# Converting pounds to kilograms
# 1 pound is 0.453592 kg
pounds = float(input('Please enter weight in pounds: '))
CONVERSION_FACTOR = 0.453592 # this is a constant, written with capitals
kg = round(pounds * CONVERSION_FACTOR, 1)
print(f'The weight in pounds is: {pounds}lbs, \nWeight in kilograms is: {kg}kg')

# Converting Celsius to Fahrenheit
# F = (C * 9/5) + 32

degC = float(input('PLease enter temperature in degC: '))
degF = (degC * 9/5) + 32
print(f'Temperature in Celsius: {degC}degC\nTemperature in Fahrenheit: {degF}F')

# Convering miles to kilometers
# 1 mile is 1.6 km
miles = float(input('Please enter distance in miles: '))
CONVERSION_FACTOR = 1.6 # this is a constant, written with capitals
km = round(miles * CONVERSION_FACTOR, 1)
print(f'The distance in miles is: {miles}m, \nDistance in kilometers is: {km}km#')

