###REGULAR EXPRESSION###
# A regular expression or RegEx is a special text string that helps to find patterns in data. A RegEx can be used to check if some pattern exists in a different data type. To use RegEx in python first we should import the RegEx module which is called re.

import re
# Methods in re Module
# re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
txt = 'I love to teach python and javaScript, and I love cat too.'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)
print(match.span())

# re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
search = re.search('love', txt)
print(search)

# q: what is difference between match and search?
# a: match searches only in the beginning of the first line of the string and returns matched objects if found, else returns None. search returns a match object if there is one anywhere in the string, including multiline strings.

# re.findall: Returns a list containing all matches
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
# It return a list
matches = re.findall('language', txt, re.I)
print(matches)

# re.sub: Replaces one or many matches within a string
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced) 

# re.split: Takes a string, splits it at the match points, returns a list
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt))

###WRITING REGULAR EXPRESSION PATTERNS###
#  To declare RegEx variable r''. The r is for raw string, which means unescaped string.
regex_pattern = r'apple' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)

# Square Bracket
regex_pattern = r'[Aa]pple' # this square bracket means either A or a
matches = re.findall(regex_pattern, txt)
print(matches)

# Escape character(\) in RegEx
regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)

# One or more times(+)
regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)

# Period(.)
regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)
regex_pattern = r'[a].+'  # . any character, + any character one or more times 
matches = re.findall(regex_pattern, txt)
print(matches)

# Zero or more times(*)
regex_pattern = r'[a].*'  # . any character, * any character zero or more times 
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches) 

# Zero or one times(?)
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)

# Quantifier in RegEx
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)

# Cart(^)
# Start with
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)

# Negation
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)


###EXERCISE###
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall(r'\b\w+\b', paragraph)
result = []
for word in words:
   if(word in words):
      result.append((word, words.count(word)))

print(result)

points = ['-12', '-4', '-3', '-1', '0', '4', '8']
num_points = [int(point) for point in points]
num_points.sort()
print(num_points)
diff = num_points[-1] - num_points[0]
print(diff)