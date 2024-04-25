###Python Error Types###
#Syntax Error -> try execute this file
# print 'hello world' #error because missing parentheses

#Name Error
# print(age) #error beacude age variable not defined

#Index Error
numbers = [1, 2, 3, 4, 5]
# print(numbers[5]) #error because index was out of range

#ModuleNotFound Error
# import maths #this is not module found

#Attribute Error
import math 
# print(math.PI) #PI attribute not found

#Key Error
users = {'name':'Asab', 'age':250, 'country':'Finland'}
# print(users['county']) #key 'county not fount

#Type Error
# print(4 + '3') #'3' error because string cannot calculation with integer

# Import Error
# from math import power #error because no function called power in the math module

# Value Error
# print(int('12a')) #error because of the 'a' letter in it.

# ZeroDivision Error
# print(1 / 0) #error because we cannot divide a number by zero.