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

# remove
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']