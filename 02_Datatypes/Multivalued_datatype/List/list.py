# List - Collection of homogeneous or heterogeneous element seperatedd by commas, element in the list are ordered list can holdup duplicated elements.
number = [1,2,3,4,5]
data = ['Myank', 22, 5.8, 12000,[4,8,10]]

# Indexing on List
name = ["Steve Jobs","Bill Gates","Tim Cook","Alex"] 

print(name[0]) # Steve Jobs
print(name[1]) # Bill Gates
print(name[-2]) # Tim Cook
print(name[0][6]) # J
print(name[:2:]) # Steve Jobs, Bill Gates
print(name[0][-4::])

# Index lookup method - It is a procedure to replace the value of a list by using  index number. This method only supports for mutable datatype.

# For replacing single element
name = ["Steve Jobs","Bill Gates","Tim Cook","Alex"] 
name[1] = "Sundar" 
print(name)

# For replacing multiple element at a time.
name = ["Steve Jobs","Bill Gates","Tim Cook","Alex"] 
name[:2:] = ["Yash","Maya"]
print(name)

# Methods on List - 
# 1. append() - It puts the item at the last position.
fruits = ['banana','orange','mango','lemon']
fruits.append('apple')
fruits.append('kiwi')
print(fruits)

# 2. insert() - it puts the item at a specified position
fruits = ['banana','orange','mango','lemon']
fruits.insert(2,'apple')
print(fruits)
fruits.insert(3,'lime')
print(fruits)

# 3. remove() - It removes the specified item from the list. It takes one argument
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']

# pop() - It removes the last item from the list
fruits = ['banana','orange','mango','lemon']
fruits.pop()
print(fruits)

# del() - It is used to delete the particular item
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
print(fruits)      
del fruits[1]
print(fruits)
del fruits

# clear() - It is used to clear all the items from the list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits) 

# count() - It counts the number of occurence present in the list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange')) 
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

# index() - It is used to give the index of the particular item.
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))

# Reverse() - It is used to reverse the list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)

# sort() - This method is used to sort the elements of a list in ascending order by default.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
ages = [9,8,7,6,5,4,3,2,1]
ages.sort()
print(ages)