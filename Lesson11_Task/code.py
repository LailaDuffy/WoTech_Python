import json

with open('students.json') as json_file:
  data = json.load(json_file)

# calculate average age  and average grade of all students
total_students = len(data["Students"])
total_age = 0
total_grade = 0
for student in data["Students"]:
  total_age += int(student["Age"])
  total_grade += int(student["Grade"])

average_age = total_age/total_students
average_grade = total_grade/total_students

print(f'The average age of students is {average_age}')
print(f'The average grade of students is {average_grade}')

# calculate average age by Major
majors = {}
for student in data["Students"]:
  major = student['Major']
  grade = int(student['Grade'])
  if major not in majors:
    majors[major] = {'total_grade_per_major': 0, 'count': 0}
  majors[major]['total_grade_per_major'] += grade
  majors[major]['count'] +=1

for major, totals in majors.items():
  average_per_major = totals['total_grade_per_major']/totals['count']
  print(f'The average grade of {major} is {average_per_major}')
