#Task 1 Calculate the Body Mass Index (BMI)
#Description: Body Mass Index (BMI) is a measure of body fat based on height and weight. It is calculated by dividing a person's weight in kilograms by the square of their height in meters. The formula for BMI is:

#[BMI = \frac{weight (kg)}{height (m)^2}]

#Write a Python program that prompts the user to enter their weight in kilograms and their height in meters, then calculates and displays their BMI.

#Example Output:

#Enter your weight in kilograms: 70
#Enter your height in meters: 1.75
#Your BMI is: 22.86

# Your code

# create a variable for weight for user to input, make it a float
weight = float(input('Please enter your weight in kg: '))
# create a variable for height for user to input, make it a float
height = float(input('Please enter your height in meters: '))
# create a variable for BMI and assign the given formula, round it to 2 decimal places
bmi = round((weight/(height**2)), 2)
# print the result, use f-string for formatting
print(f'Your BMI is: {bmi}')



