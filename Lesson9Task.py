You can create any class (Cat, Dog, Car, Account, Client, etc...)

To make a data structure which will hold all instances/objects together

Print out object data using loops

Use methods of all created objects using loops

Allow programmer to override a parameter

class Country:
  # constructor
  def __init__(self, name, location, capital_city):
    self.name = name
    self.location = location
    self.capital_city = capital_city
    self.independence_day = '1st January'

 # getters and setters
  def set_population(self, popul_number, popul_unit):
    self.popul_number = popul_number
    self.popul_unit = popul_unit

  def get_population(self):
    return f'{self.popul_number} {self.popul_unit}'

  def set_independence_day(self, date):
    self.independence_day = date

  def get_independence_day(self):
    return f'{self.independence_day}'

# creating objects from COuntry class
latvia = Country('Latvia', 'Europe', 'Riga')
estonia = Country('Estonia', 'Europe', 'Tallinn')
brazil = Country('Brazil', 'South America', 'Brasilia')

# storing countries in a list
countries = [latvia, estonia, brazil]

# printing country info
for country in countries:
  print(f'{country.name} is located in {country.location}, the capital city is {country.capital_city}.')

# setting population
latvia.set_population(1.9, 'million')
estonia.set_population(1.3, 'million')
brazil.set_population(211, 'million')

# printing population
for country in countries:
  print(f"{country.name}'s population is {country.get_population()}.")

# printing independance days method
def print_ind_days():
  for country in countries:
    print(f"{country.name}'s independence day is {country.independence_day}.")

#default independence days
print_ind_days()

latvia.set_independence_day('18th November')
estonia.set_independence_day('24th February')
brazil.set_independence_day('7th September')

#updated independence days
print_ind_days()
