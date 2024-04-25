###LIST COMPREHENSION###
# List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list. List comprehension is considerably faster than processing a list using the for loop.

#Creating List Comprehension
language = 'Python'
#using method for change to list
lst = list(language)
print(lst)

#using list comprehension
comp_list = [i for i in language]
print(comp_list)
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)
squares = [i * i for i in range(11)]
print(squares) 


###LAMBDA FUNCTION###
# Lambda function is a small anonymous function without a name. It can take any number of arguments, but can only have one expression. Lambda function is similar to anonymous functions in JavaScript. We need it when we want to write an anonymous function inside another function.

#Creating Lambda Function
def add_two_nums(a, b):
   return a + b
print(add_two_nums(2, 3))

# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))

#Lambda Function Inside Another Function
def power(x):
    return lambda n : x ** n

cube = power(2)(3)
print(cube) 

kubik = power(3)
print(kubik(3))

###EXERCISE###
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers = [i for i in numbers if i <= 0]
print(negative_numbers)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
def flat_list(lists):
   result = []
   for lst in lists:
      if isinstance(lst, list):
         result.extend(flat_list(lst))
      else:
         result.append(lst)
   return result

print(flat_list(list_of_lists))

exponents = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(exponents)