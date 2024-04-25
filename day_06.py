###Tuple###
# Tuple is a collection of different data types which is ordered and unchangeable (immutable), so we can no use add, insert, and remove methods.

#Creating a Tuple
#using built-in function
empty_tuple = tuple()
#only syntax
emty_tuple = ()
tpl = ('item1', 'item2', 'item3')

#Tuple Length
tpl = ('item1', 'item2', 'item3')
print(len(tpl))

#Accessing Tuple Items
tpl = ('item1', 'item2', 'item3')
print(tpl[0])
last_index = len(tpl) - 1
print(tpl[last_index])
print(tpl[-1])

#Slicing Tuple
tpl = ('item1', 'item2', 'item3', 'item4')
all_item = tpl[0:4]
print(all_item)
first_slice = tpl[0:2]
print(first_slice)
second_tpl = tpl[-3:-1]
print(second_tpl)

#Changing Tuple to Lists
tpl = ('item1', 'item2', 'item3', 'item4', 'item5')
lst = list(tpl)
print(lst)
lst[0] = 'apple' #this will modify for lst list
print(lst)

#Checking an item in Tuple
fruits = ('apple', 'banana', 'lemon', 'grape', 'penapple')
print('apple' in fruits)
print('orange' in fruits)

#Joining Tuples
tpl1 = ('item1', 'item2')
tpl2 = ('item3', 'item4')
tpl3 = tpl1 + tpl2
print(tpl3)

#Deleting Tuples
tpl4 = ('item1', 'item2', 'item3')
del tpl4 #this will delete tuple or it will be empty

###Exercise###
#Lvl 1
empty_tpl = tuple()
sister = ('Rose', 'Milo')
brother = ('Ciko', 'Coki')
siblings = sister + brother
print(len(siblings))
parents = ('Sumali', 'Anik')
family = parents + siblings
print(family)