filename = '/content/births.txt' # find location by copying file path

with open(filename, 'r') as file: # file, mode of opening 'r' = read mode
  content = file.read()

print('Standard file input/output')
print(content)

for line in content:
  print(line)

### USING READLINES FUNCION
with open(filename, 'r') as file:
  content = file.readlines()

print('Standard file input/output')
print(content)

for line in content:
  print(line)

# modify code and make filename as input from the user,
# enclose in try except to catch


filename = input('Please provide a file: ')

try:
  with open(filename, 'r') as file:
    content = file.readlines()
except:
  print(f'File loading failed.')

print('Standard file input/output')
print(content)

for line in content:
  print(line)

# births
with open('/content/births.txt', 'r') as file:
  births = file.readlines()

print('Standard file input/output')
for birthline in births:
  print(birthline[4:])

# sum up all the elements
sum = 0
for birthline in births:
  sum += int(birthline[4:])

print(f'Total elements: {sum}')

# births
with open('/content/births.txt', 'r') as file:
  births = file.readlines() # list separated by comma

# deaths
with open('/content/deaths.txt', 'r') as file:
  deaths = file.readlines()

# accessing the number: int(birthline[4:])
for i in range(len(births)):
  birthline = births[i] # accessing one line at a time
  deathline = deaths[i]
  print(birthline)
  print(deathline)

  birthnumber = int(birthline[4:])
  deathnumber = int(deathline[4:])
  growth = birthnumber - deathnumber
  print(f'Growth: {growth}')
  month = birthline[:3]
  if growth > 0:
    print(month, growth)
# PANDAS
import pandas as pd # pd is abbreviation for pandas to not to have write 'pandas' in code

births = pd.read_csv('/content/births.txt', header=None, delimiter = ' ')
deaths = pd.read_csv('/content/deaths.txt', header=None, delimiter =' ')

birth_column_names = ['Month', 'no_of_births']
births.columns = birth_column_names
print(births)

deaths.columns = ['Month', 'no_of_deaths']
print(deaths)

births['Saldo'] = births['no_of_births'] - deaths['no_of_deaths']
births['no_of_deaths'] = deaths['no_of_deaths']
# EXPORTING
file_name = '/content/output.csv'
births.to_csv(file_name, index=False)
