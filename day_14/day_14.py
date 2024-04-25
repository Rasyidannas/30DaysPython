###HIGH ORDER FUNCTION###
# In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:
# A function can take one or more functions as parameters
# A function can be returned as a result of another function
# A function can be modified
# A function can be assigned to a variable

#Function as a Parameter in js we call it callback function
def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f, lst):
    summation = f(lst)
    return summation

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)

#Function as a Return Value
def square(x):          
    return x ** 2

def cube(x):            
    return x ** 3

def absolute(x):        
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): 
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))

#Python Closures is a nested function to access the outer scope of the enclosing function.
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))

#Python Decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.

#Creating Single Decorator
'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

#Applying Multiple Decorator to a Single Function
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator    
def greeting():
    return 'Welcome to Python'
print(greeting()) # ['WELCOME', 'TO', 'PYTHON']

# Accepting Parameters in Decorator Functions
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')

#Built-in Higher Order Functions
#Map() is a built-in function that takes a function and iterable as parameters.
numbers = [1, 2, 3, 4, 5]
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))

#Filter() is function calls the specified function which returns boolean for each item of the specified iterable (list).
numbers = [1, 2, 3, 4, 5] 

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))

#Reduce() is defined in the functools module and we should import it from this module
import functools
numbers_str = ['1', '2', '3', '4', '5']
def add_two_nums(x, y):
    return int(x) + int(y)

total = functools.reduce(add_two_nums, numbers_str)
print(total)

###EXERCISE###
#Lvl 1
# Map is for execution eact item, Filter is same like Map but it is return boolean, and Reduce Execution not each item but before item too
# highorder is callback and can return value of callback function. Closure write a function in body of function, decorator is for modify return value of another function
from countries import countries, names, numbers
for country in countries:
    print(country)

names_list = [name for name in names]
print(names_list)

numbers_list = [number for number in numbers]
print(numbers_list)

#Lvl 2
new_countries = map(lambda country: country.upper(), countries)
print(list(new_countries))