###Lists###
# List a collection which is ordered and changeable(modified). Allow duplicate members and A list can be empty or it may have different data type items. Python have 4 data collections (List, Tuple, Set, and Dictionary)

#Create a List
#Using built-in function
lst = list()
#using square brackets
lst = []

#Example List
fruits = ['apple', 'banana', 'lemon']
vegetables = ['tomato', 'cabbage', 'potato']
web_tech = ['html', 'css', 'javascript', 'python', 'php']
print('fruits:', fruits)
print('Number of fruits:', len(fruits))
print('vegetablse:', vegetables)
print('Number of vegetables:', len(vegetables))
print('web technologies:', web_tech)
print('Number of web technologies:', len(web_tech))
person_bio = ['Rasyid', 25, {'country': 'Indonesia', 'city': 'Sidoarjo'}]

#Accesing List Item Using Index
fruits = ['apple', 'banana', 'lemon']
print(fruits[0])
print(fruits[-1])
vegetables = ['tomato', 'cabbage', 'potato']
print(vegetables[2])
print(vegetables[-2])
web_tech = ['html', 'css', 'javascript', 'python', 'php']
print(web_tech[3])
print(web_tech[-2])

#Unpacking List Item
list_items = ['item1', 'item2', 'item3']
first_item, second_item, third_item = list_items
print(first_item)
print(second_item)
print(third_item)

#Slicing List Item
fruits = ['banana', 'orange', 'mango', 'lemon']
first_slice = fruits[1:3]
print(first_slice)
second_slice = fruits[-3:-1]
print(second_slice)

#Modifying Lists
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)

#Checking Item List
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)

#Adding Item List
fruits = ['banana', 'orange', 'mango']
fruits.append('apple') #adding from end
print(fruits)
fruits.insert(2, 'lime') #adding with position index
print(fruits)

#Removing Items List
fruits = ['banana', 'orange', 'mango', 'apple', 'lemon', 'grapes']
fruits.remove('mango') #removing specific element/item
print(fruits)
fruits.pop() #removing last item
print(fruits)
del fruits[0]
del fruits[1:2]
print(fruits)
fruits.clear()
print(fruits)

#Copying List
fruits = ['banana', 'orange', 'mango']
fruits_copy = fruits.copy()
print(fruits_copy)
fruits_copy.append('apple')
print(fruits_copy)
print(fruits)

#Joning List
positive_number = [1, 2, 3, 4, 5]
zero = [0]
negative_number = [-5, -4, -3, -2, -1]
integer = negative_number + zero + positive_number
print(integer)
negative_number.extend(zero) #using extend() function
print(negative_number)

#Counting Item in List
fruits = ['banana', 'orange', 'apple']
print(fruits.count('banana'))

#Finding Item Index in List
fruits = ['banana', 'orange', 'lemon']
print(fruits.index('orange'))

#Reversing List
fruits = ['banana', 'orange', 'grape']
fruits.reverse()
print(fruits)

#Sorting List
fruits = ['banana', 'orange', 'apple', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True) #make this oposite
print(fruits)
numbers = [12, 2, 33, 4, 15]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

###Exercise###
empty_list = list()
first_list = ['Ciko', 'Coki', 'Caplin', 'Koski', 'Cemeng', 'Tompel']
print(len(first_list))
print(first_list[0])
mixed_data_types = ['Rasyid', 25, 161, 'single', 'Sidoarjo, Indonesia']