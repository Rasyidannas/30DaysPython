###EXCEPTION HANDLING###
# Python uses try and except to handle errors gracefully. A graceful exit (or graceful handling) of errors is a simple programming idiom - a program detects a serious error condition and "exits gracefully", in a controlled manner as a result. 

#Creating try and except
try:
   print(10 + '5')
except:
   print('Something went wrong')

#Handle the error by type error
try:
   name = input('Enter your name:')
   year_born = input('Year you were born:')
   age = 2019 - year_born
   print(f'You are {name}. And your age is {age}.')
except TypeError:
   print('Type error occured')
except ValueError:
   print('Value error occured')
except ZeroDivisionError:
   print('zero division error occured')

#Handle else (it will run when no except or except not execute)
try:
   name = input('Enter your name:')
   year_born = input('Year you born:')
   age = 2019 - int(year_born)
   print('You are {name}. And your age is {age}.')
except TypeError:
   print('Type error occur')
except ValueError:
   print('Value error occur')
except ZeroDivisionError:
   print('zero division error occur')
else:
   print('I usually run with the try block')
finally: #this will always run
   print('I always run.')

#Packing and Unpacking Arguments in Python
#Unpacking Lists
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst)) #call with arguments unpacked (*) from a list
args = [2, 7]
numbers = range(*args) #call with arguments unpacked (*) from a list
print(numbers)
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries #using unpacked like rest operator
print(fin, sw, nor, rest)

#Unpacking Dictionaries
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct))

#Packing Lists
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3)) 
print(sum_all(1, 2, 3, 4, 5, 6, 7)) 

# Packing Dictionaries
def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))

#Spreading in Python
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst) 
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)

#Enumerate
for index, item in enumerate(countries):
    print('hi')
    if item == 'Finland':
        print(f'The country {item} has been found at index {index}')

#Zip
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)

###EXERCISE###
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*res, es, ru = names
nordic_countries = es, ru
print(nordic_countries)