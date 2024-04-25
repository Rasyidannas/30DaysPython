###SET###
# Set is a collection of items, used to store unique items and this also same the Mathematics definition.

#Creating a Set
#using built-in function
st = set()
#using syntax
st = {'item1', 'item2', 'item3'}

#Getting Set Length
fruits = {'apple', 'banana', 'grape'}
print(len(fruits))

#Accessing item in Set
fruits = {'apple', 'banana', 'lemon'}
print('apple' in fruits)

#Adding items to Set
fruits = {'apple', 'banana', 'lemon'}
fruits.add('lime')
print(fruits)
#add using update()
fruits.update(['mango', 'tomato'])
print(fruits)

#Removing items to Set
fruits = {'apple', 'banana', 'mango', 'lime', 'lemon'}
fruits.remove('apple')
print(fruits)
fruits.pop() #this will random item
print(fruits)

#Clearing all items Set
fruits = {'apple', 'banana'}
fruits.clear()
print(fruits)

#Deleting set
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

#Converting List to Set
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits_set = set(fruits)
print(fruits_set)

#Joining Sets (union() or update())
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables))
first_item = {'item1', 'item2', 'item3'}
second_item = {'item4', 'item5', 'item6'}
first_item.update(second_item)
print(first_item)

#Finding Intersection Items / irisan
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
irisan = st1.intersection(st2)
print(irisan)

#Checking Subset and Super Set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.issubset(st1))
print(st1.issuperset(st2))

#Checking the Difference Between Two Sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1))
print(st1.difference(st2))

#Finding Symmetric Difference Between Two Sets or mathematically: (A\B) ∪ (B\A)
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
print(st2.symmetric_difference(st1))

#Joining Sets for check common item
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) #False because item2 and item3
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

###Exercise###
it_companies = {'facebook', 'google', 'instagram', 'amazon'}
it_companies.add('twitter')
print(it_companies)
it_companies.update(['shopee', 'tokopedia'])
print(it_companies)
it_companies.pop()
print(it_companies)
#remove() will show error but discard() will not show any error