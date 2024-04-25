###String###
#Text is a string data type. Any data type written as text is a string. Any data under single, double or triple quote are strings.

#Example creating a string
letter = 'P'
print(letter)
print(len(letter))
greeting = 'Hello World'
print(greeting)
print(len(greeting))
sentence = 'I hope you are enjoying 30 days of Python Challenge'
print(sentence)
#Multiline string using (''') or (""")
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Concatination
first_name = 'Rasyid'
last_name = 'Annas'
full_name = first_name + ' ' + last_name
print(full_name)
#using f-string
print(f"I'm {first_name} {last_name}")

# Escape Sequences
# \n -> new line
# \t -> tab means (8 spaces)
# \\ -> back slash
# \' -> single quotes
# \" -> double quotes

# String Formatting
#old style formatting
# %s - string
# %d - integers
# %f - floating point numbers
# %.number of digitf - floating point numbers with fixed precision atau pembulatan
# Example
# String
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)
# String and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string)

# New style formatting
# String
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3
# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

# Python Strings as Sequences of Characters
# Unpacking Characters
language = 'Python'
a,b,c,d,e,f = language
print(a,b,c,d,e,f)
# Accessing Characters in Strings by Index
language2 = 'Python'
print(language2[0])
print(language2[-1])
# Slicing Python Strings
language3 = 'Python'
first_slice = language3[0:3]
print(first_slice)
second_slice = language3[3:]
print(second_slice)
third_slice = language3[-3:]
print(third_slice)
# Reversing a String
reversed = language3[::-1]
print(reversed)
# Skipping Characters While Slicing
skipping = language3[0:6:2]
print(skipping)

# String Methods
challenge = 'thirty days of python'
#capitalize(): Converts the first character of the string to capital letter
print(challenge.capitalize())
#count(): returns occurrences of substring in string, count(substring, start=.., end=..).
print(challenge.count('y'))
#endswith(): Checks if a string ends with a specified ending
print(challenge.endswith('on'))
#expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge2 = 'thirty\tdays\tof\tpython'
print(challenge2.expandtabs())
print(challenge2.expandtabs(5))
#find(): Returns the index of the first occurrence of a substring, if not found returns -1
print(challenge2.find('th'))
#rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
print(challenge.rfind('th'))
#index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
print(challenge.index('th'))
#rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
print(challenge.rindex('th'))
#isalnum(): Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())
challenge = '30DaysPython'
print(challenge.isalnum())
challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character
#isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha())
#isdecimal(): Checks if all characters in a string are decimal (0-9)
challenge = 'thirty days of python'
print(challenge.isdecimal()) # False, space is not decimal
challenge = '123'
print(challenge.isdecimal())
#isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
challenge = 'Thirty'
print(challenge.isdigit())
challenge = '30'
print(challenge.isdigit())
#isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
num = '10'
print(num.isnumeric())
num = '\u00BD' # ½
print(num.isnumeric())
#isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier())
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())
#islower(): Checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower())
challenge = 'Thirty days of python'
print(challenge.islower())
#isupper(): Checks if all alphabet characters in the string are uppercase
challenge = 'thirty days of python'
print(challenge.isupper())
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())
#join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result)
#strip(): Removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth'))
#replace(): Replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))
#split(): Splits the string, using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split())
challenge = 'thirty, days, of, python'
print(challenge.split(', '))
#title(): Returns a title cased string
challenge = 'thirty days of python'
print(challenge.title())
#swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
challenge = 'thirty days of python'
print(challenge.swapcase())
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())
#startswith(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.startswith('thirty'))

###Exercise###
first_arr = ['Thirty', 'Days', 'of', 'Python']
result = ' '.join(first_arr)
print(result)
second_arr = ['Coding', 'For', 'All']
result = ' '.join(second_arr)
print(result)
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(f'{company.capitalize()}, {company.title()}, {company.swapcase()}')
first_slice = company[0:6]
print(first_slice)
print(company.index('Coding'))
print(company.replace('Coding', 'Python'))
