###Modules###
#A module is a file containing a set of codes or a set of functions which can be included to an application. A module could be a file containing a single variable, a function or a big code base.

#Creating a module is mymodule.py

#Importing mymodule.py and a function
import mymodule
print(mymodule.generate_full_name('Rasyid', 'Annas'))

#Importing functions from a module
from mymodule import generate_full_name, sum_two, weight
print(generate_full_name('Ciko', 'Mentul'))
print(sum_two(10, 12))
print(weight(80))

#Importing functions from a module and renaming
from mymodule import generate_full_name as full_name, sum_two as sum, weight as berat
print(full_name('Rasyid', 'Nur Annas'))
print(sum(13, 12))
print(berat(10))

#Import Built-in Modules
#OS Module is possible to automatically perform many operating system tasks.
import os 
# Creating a directory
# os.mkdir('test')
# Changing the current directory
# os.chdir('./')
# Getting current working directory
# os.getcwd()
# Removing directory
# os.rmdir()

#Sys Module provides functions and variables used to manipulate different parts of the Python runtime environment
import sys
#  # this line would print out: filename argument1 argument2
print('Welcome {}.'.format(sys.argv[0]))
# to exit sys
# sys.exit()
# To know the largest integer variable it takes
# sys.maxsize
# To know environment path
# sys.path
# To know the version of python you are using
# sys.version

#Statistic Module provides functions for mathematical statistics of numeric data
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))  
print(median(ages))     
print(mode(ages))       
print(stdev(ages))      

#Math Module is Module containing many mathematical operations and constants.
import math
print(math.pi)
print(math.sqrt(2)) 
print(math.pow(2, 3))
print(math.floor(9.81))
print(math.ceil(9.81))
print(math.log10(100))

#String Module is a useful module for many purposes.
import string
print(string.ascii_letters) 
print(string.digits)        
print(string.punctuation)

#Random Module which gives us a random number between 0 and 0.9999....
from random import random, randint
print(random())  
print(randint(5, 20))

###Exercise###
#Lvl 1
from random import randint
import string

def index_random(limit):
   return randint(0, limit)

def alpha_random():
   alpha = string.ascii_letters
   return alpha[index_random(int(len(str(alpha))))]

def random_user_id():
   digit_random = randint(0, 9999)
   list_digit_random = list(str(digit_random))
   length_list_random = int(len(list_digit_random) - 1)

   for _ in range(3):
      alpha = alpha_random()
      list_digit_random.insert(index_random(length_list_random), alpha)

   return ''.join(list_digit_random)

print(random_user_id())

def user_id_gen_by_user(num):
   digit_random = randint(0, num)
   list_digit_random = list(str(digit_random))
   length_list_random = int(len(list_digit_random) - 1)

   for _ in range(num - randint(2, 5)):
      alpha = alpha_random()
      list_digit_random.insert(index_random(length_list_random), alpha)

   return ''.join(list_digit_random)

print(user_id_gen_by_user(16))

def rgb_color_gen():
   result = []

   for _ in range(3):
      result.append(randint(0, 255))
   
   return result

print(rgb_color_gen())