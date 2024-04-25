###LOOPS###
#While Loop
count = 0
while count < 5:
    print(count)
    count = count + 1

#While loop with else
count = 0
while count < 5:
    print(count)
    count = count + 1
else: #this will execute when loop is done
    print(f'this loop is done and count is {count}')

#Break and Continue - Part 1
#Break: We use break when we like to get out of or stop the loop.
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

#Continue: With the continue statement we can skip the current iteration, and continue with the next:
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

#For Loop
#For Loop with List
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)

#For Loop with String
language = 'Python'
for letter in language:
    print(letter)
#or
for i in range(len(language)):
    print(language[i])

#For Loop with Tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

#For Loop with Dictionary
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)
#or
for key, value in person.items():
    print(key, value)

#For Loop in Set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

#For Loop with Break and Continue
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

# The Range Function
# The range() function is used list of numbers. The range(start, end, step) takes three parameters: starting, ending and increment. Default argument is end
lst = list(range(11))
print(lst)
st = set(range(1, 11))
print(st)
#Example in For Loop
for number in range(11):
    print(number)

#Nested For Loop
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

#For Else
for number in range(11):
    print(number)
else:
    print('The loop stops at', number)

#Pass
for number in range(6):
    pass #this for if you don't want to pass any code in here

###Exercise###
#Lvl 1
num = 0
while num <= 10:
    print(num)
    num += 1

dec = 10
while dec >= 0:
    print(dec)
    dec -= 1
# Triangle
for row in range(1, 8):
    for col in range(1, row + 1):
        print("#", end=" ")
    print("")

print("______")
# Square
for row in range(1, 8):
    for col in range(1, 8):
        print("#", end=" ")
    print("")

number = 10
for num in range(number):
    result = num * num
    print(f'{num} * {num} = {result}')

skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
for skill in skills:
    print(skill)

for number in range(100):
    if number % 2 == 0:
        print(number)

for number in range(100):
    if number % 2 != 0:
        print(number)