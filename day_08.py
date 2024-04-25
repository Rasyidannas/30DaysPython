###DICTIONARY###
# Dictionary is a collection of unordered, modifiable(mutable) paired (key:value) data type. It is like object in javascript

#Creating a Dictionary
#syntax
empty_dict = {}
dct = {'key1': 'value1', 'key2': 'value2'}
person = {
    'first_name': 'Rasyid',
    'last_name': 'Annas',
    'age': 25,
    'country': 'Indonesia',
    'skills': ['javascript', 'python', 'php', 'react']
}

#Dictionary Length
person = {
    'first_name': 'Rasyid',
    'last_name': 'Annas',
    'age': 25,
    'country': 'Indonesia',
    'skills': ['javascript', 'python', 'php', 'react']
}
print(len(person))

#Accessing Dictionary Items
person = {
    'first_name': 'Rasyid',
    'last_name': 'Annas',
    'age': 25,
    'country': 'Indonesia',
    'skills': ['javascript', 'python', 'php', 'react']
}
print(person['first_name'])
print(person['last_name'])

# Adding Items to a Dictionary
person = {
    'first_name': 'Rasyid',
    'last_name': 'Annas',
    'age': 25,
    'country': 'Indonesia',
    'skills': ['javascript', 'python', 'php', 'react']
}
person['skills'].append('HTML')
print(person['skills'])

# Modifying Items in a Dictionary
person = {
    'first_name': 'Rasyid',
    'last_name': 'Annas',
    'age': 25,
    'country': 'Indonesia',
    'skills': ['javascript', 'python', 'php', 'react'],
}
person['last_name'] = 'Nur Annas'
print(person['last_name'])

#Checking Keys in a Dictionary
person = {
    'first_name': 'Rasyid',
    'last_name': 'Annas',
    'age': 25,
    'country': 'Indonesia',
    'skills': ['javascript', 'python', 'php', 'react'],
}
print('last_name' in person)

#Removing Key and Value Pairs from a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
print(dct)
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item
print(dct)

#Changing Dictionary to a List of Items
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
lst = dct.items()
print(lst)

#Clearing all items Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear())

#Deleting a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

#Copy a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()
print(dct_copy)

#Getting Dictionary Keys as a List
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)

#Getting Dictionary Values as a List
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)

###Exercise###
dog = {
    'name': 'Ciko',
    'color': 'white',
    'legs': 4,
    'age': 3
}
student = {
    'first_name': 'Rasyid',
    'last_name': 'Annas',
    'gender': 'Male',
    'age': 25,
    'marital_status': 'single',
    'skills': ['python', 'javascript', 'php', 'HTML', 'CSS'],
    'country': 'Indonesia',
    'city': 'Sidoarjo'
}
print(len(student))
print(type(student['skills']))

