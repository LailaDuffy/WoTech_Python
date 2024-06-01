for letter in "I LOVE PYTHON": # string iterable object
  print(letter, end = '\n') # end specifies the end of print conditions, \n for new line

# FOR LOOP LIST
cities_i_have_been_to = ['Tallin', 'Riga', 'Tartu', 'Aluksne', 'Viru', 'Ventspils']

for city in cities_i_have_been_to:
  print(f'I have been to ' + city)

counter = 1 # initializing counter variable

for city in cities_i_have_been_to:
  print(f'{counter}. I have been to {city}')
  counter = counter + 1

# adding the previous city in the for loop
previous_city = None # initilize the variable before the for loop
next_city = None

for city in cities_i_have_been_to:
  counter = counter + 1
  if previous_city == None:
    print(f'{counter}. I have been to {city}.')
  else:
    print(f'{counter}. I have been to {city}. The previous city I visited was {previous_city}.')
  previous_city = city

cities_i_have_been_to = ['Tallin', 'Riga', 'Tartu', 'Aluksne', 'Viru', 'Ventspils']
which_year_I_visited = [2020, 2024, 2020, 2021, 2024, 2022]

len(cities_i_have_been_to) # count fo elements

range(len(cities_i_have_been_to)) # range of elements
list(range(len(cities_i_have_been_to))) # LIST OF RANGE OF ELEMENTS

range(len(cities_i_have_been_to)) # range of elements
for i in range(len(cities_i_have_been_to)):
  print(f'This is the index {i}')
  print(cities_i_have_been_to[i])
  print(which_year_I_visited[i])range(len(cities_i_have_been_to)) # range of elements

range(len(cities_i_have_been_to)) #elements  [0, 1, 2, 3, 4, 5]
for i in range(len(cities_i_have_been_to)):
  print(f'I have been to {cities_i_have_been_to[i]}. I visited that city in {which_year_I_visited[i]}')

matrix_2d = [ # nested list
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

for i in matrix_2d:
  print(f'This is the sublist: {i}')
  for j in i:
    print(f'These are the elements of the sublist: {j}')


# GRADE MAPPING DATA EXERCISE

grade_mapping = [[90, 'A'], [80, 'B'], [70, 'C'], [60, 'D'], [0, 'F']] # nested list
grade_mapping[0] # [90, 'A']
grade_mapping[0][1] # A
grade_mapping[3][1] # D

for threshold, letter_grade in grade_mapping:
  print(threshold)
  print(letter_grade)

student_names = ["Alice", "Bob", "Charlie", "David", "Eva"]
student_scores = [85, 72, 93, 60, 77]
grade_mapping = [[90, 'A'], [80, 'B'], [70, 'C'], [60, 'D'], [0, 'F']]

for i in range(len(student_names)):
  print(f"{student_names[i]}'s is {student_scores[i]}") # and their grade is {grade_mapping[i][j]}')

for i in range(len(student_names)):
  for threshold, letter_grade in grade_mapping:
    if student_scores[i] >= threshold:
      print(f"Hi {student_names[i]}, Your score is {student_scores[i]}. Your grade is {letter_grade}.")
      break
# ENUMERATE

student_names = ["Alice", "Bob", "Charlie", "David", "Eva"]
for index, student in enumerate(student_names, start=1): # enumerate(list_name, starting counter value)
  print(f'Student {index}: {student}')
