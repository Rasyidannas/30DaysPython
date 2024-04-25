###Conditional###
#If Condition
a = 3
if a > 0:
    print('A is a positive number')

#If Else
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

#If Elif Else
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

#Short Hand
a = 3
print('A is positive') if a > 0 else print('A is negative')

#Nested Condition
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

#If Condition and Logical Operators
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

# If and Or Logical Operators
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')

###Exercise###
#Lvl 1
age = input('Enter your age: ')
int_age = int(age)
diff = 18 - int_age
if int_age >= 18:
    print('You are old enough to learn to drive')
else:
    print(f'You need{diff} more year to learn to drive')

my_age = 25
your_age = input('Enter your age: ')
if int(your_age) > my_age:
    diff = int(your_age) - my_age
    print(f'you are {diff} older than me')
elif int(your_age) < my_age:
    diff = my_age - int(your_age)
    print(f'you are {diff} younger than me')
else:
    print('your age same with my age')

first_num = input('Enter first number: ')
second_num = input('Enter second number: ')
if int(first_num) > int(second_num):
    print(f'{first_num} is greater than {second_num}')
elif int(first_num) < int(second_num):
    print(f'{second_num} is greater than {first_num}')
else:
    print(f'{first_num} is equal to {second_num}')

#Lvl 2
score = input('Enter your score: ')
if int(score) >= 90 and int(score) <= 100:
    print('Your grade is A')
elif int(score) >= 70 and int(score) <= 89:
    print('Your grade is B')
elif int(score) >= 60 and int(score) <= 69:
    print('Your grade is C')
elif int(score) >= 50 and int(score) <= 59:
    print('Your grade is D')
elif int(score) >= 40 and int(score) <= 0:
    print('Your grade is F')
else:
    print('Your score is invalid')