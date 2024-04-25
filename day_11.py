###FUNCTION###
#Declaring and Calling Function
#Funtion without Parameters and no return
def generate_full_name():
    first_name = 'Rasyid'
    last_name = 'Annas'
    print(first_name + ' ' + last_name)
generate_full_name()

def add_two_numbers():
    num_one = 1
    num_tw0 = 2
    result = num_one + num_tw0
    print(result)
add_two_numbers()

#Function Returning a Value
def generate_full_name():
    first_name = 'Rasyid'
    last_name = 'Annas'
    full_name = first_name + ' ' + last_name
    return full_name
print(generate_full_name())

def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

#Funtion with Parameters
#Single Parameters
def greeting(name):
    message = 'Hello ' + name + '!'
    return message
print(greeting('Rasyid'))

#Two Parameters
def generate_full_name(first_name, last_name):
    return first_name + ' ' + last_name
print(generate_full_name('Rasyid', 'Nur Annas'))

#Passing Arguments with Key and Value
def print_fullname(first_name, last_name):
    return first_name + ' ' + last_name
print(print_fullname(first_name='Rasyid', last_name='Annas'))

#Function with Default Value Parameters
def greeting(name='Rasyid'):
    message = name + ' Welcome to Python for Everyone'
    return message
print(greeting())

#Arbitrary Number of Arguments
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_nums(2, 3, 4, 5))

#Default and Arbitrary Number of Parameters in Functions
def generate_groups(team, *args):
    print(f'{team} this is first argument')
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))

#Function as a Parameter of Another Function
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) 

###Exercise###
def add_two_numbers (num1, num2):
    sum = num1 + num2
    return sum
print(add_two_numbers(10, 12))

def area_of_circle (r):
    area = 3.14 * r * r
    return area
print(area_of_circle(7))

def add_all_nums (*nums):
    result = 0
    for num in nums:
        result += num
    return result
print(add_all_nums(8, 9, 8))

def convert_celsius_to_fahrenheit (c):
    result = (c - 32) * 5 / 9
    return result
print(convert_celsius_to_fahrenheit(59))

def check_season (month):
    spring = ['march', 'april', 'may']
    summer = ['june', 'july', 'august']
    fall = ['september', 'october', 'november']
    winter = ['december', 'january', 'february']

    if(month in spring):
        return 'spring'
    elif(month in summer):
        return 'summer'
    elif(month in fall):
        return 'fall'
    else:
        return 'winter'
print(check_season('march'))
print(check_season('january'))