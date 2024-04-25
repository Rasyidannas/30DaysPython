# NOTE: 
# some most of common built-in functions :  print(), len(), type(), int(), float(), str(), input(), list(), dict(), min(), max(), sum(), sorted(), open(), file(), help(), and dir().

### Built it Function ###
# Built-in functions are globally available for your use that mean you can make use of the built-in functions without importing or configuring.

print('Hello World!')   # it print the text values Hello, World!
len('Hello World!')     # it counts the number of characters including space
type("Hello World!")    # it check the type data
str(10)                 # it converts number to string
int('10')               # it convert string to number
float(10)               # it convert integer to decimal
#input('Enter your name:')   # it takes user input and write exit()
min(20,30,40,50)        # it gives the minimum value
max(20,30,40,50)        # it gives the maximum value
min([20,30,40,50])      # it takes list as an argument and return min value
max([20,30,40,50])      # it takes list as an argument and return max value
sum([20,30,40,50])      # it takes only list as an argument and return the sum 140

### Variables ###
# Variables is store data in computer memory. A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.

# Python Variable Name Rules:
# 1. A variable name must start with a letter or the underscore character (recomended is snake_case)
# 2. A variable name cannot start with a number
# 3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# 4. Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)

# Example of valid variable names
first_name = 'Rasyid'
last_name = 'Annas'
age = 25
country = 'Indonesia'
city = 'Sidoarjo'
skills = ['HTML', 'CSS', 'JavaScript', 'Python', 'Php']
person_info = {
    'firstname': 'Rasyid',
    'lastname': 'Annas',
}

# Print the values stored in the variable
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name:', last_name)
print('Last name length:', len(last_name))

# Declaring multiple variable in a line
first_name, last_name, country, age = 'Rasyid', 'Annas', 'Indonesia', 25
print(first_name, last_name, country, age)
print('First name:', first_name)
print('Last name:', last_name)
print('Country:', country)
print('Age:', age)


### Exercise ###
## Lvl 1 ##
# 2. Day 2: 30 Days of Python Programming
first_name = 'Rasyid'
last_name = 'Annas'
full_name = 'Rasyid Annas'
country = 'Indonesia'
city = 'Sidoarjo'
age = 25
year = 2024
is_married = False
is_true = True
is_light_on = True
first_name, last_name, age = 'Rasyid', 'Annas', 25
## Lvl 2 ##
type(first_name)
len(first_name)
print(len(first_name), len(last_name))
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

area_of_circle = 3.14 * 30 ** 2
circum_of_circle = 2 * 3.14 * 30
radius = float(input('Enter the radius of the circle: '))
area = radius ** 2 * 3.14
print(area)
inputFirstName = input('Enter your first name: ')
inputLastName = input('Enter your last name: ')
inputCountry = input('Enter your country:')
inputAge = input('Enter your age:')
