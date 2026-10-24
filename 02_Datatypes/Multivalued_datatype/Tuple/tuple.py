# Tuple - It is a collection of homogeneous or hecterogeneous data items or element enclosed with in the paranthesis ().
number = (1,2,3,4,5,6)
data = ("Mayank",22,5.8,12000)

'''
Properties of Tuple
- Tuple is one of the immutable datatype.
- It is ordered collection
- It will allow any data as an element of tuple and also it will allow duplicates values.
- Tuple will going to take less memory space as compared to list.
'''

# Indexing on Tuple - extracting single character at a tiny. 
data = (10,20,[30,40,60],'MM',('II','RC'))
print(data[0])
print(data[2])
print(data[2][1])
print(data[-2])
print(data[-1][-1])

# Slicing of list - extracting multiple element .
data = (10,20,[30,40,60],'MM',('II','RC'))

print(data[::])
print(data[-2::])
print(data[::2])
print(data[:3:])
print(data[1::2])

# Changing Tuple to List - We can change list to tuple and tuple to list. Tuple is immutable if we want to modify a tuple, we should first chabge it to list.
fruits = ('banana','orange','mango','lemon')
fruit = list(fruits)
print(fruit)

# Checking an item in a Tuple - We can check if an item exists or not in a tuple using 'in', it returns a boolean.
fruits = ('banana','orange','mango','lemon')
print('mango' in fruits)

# Joining Tuple - We can join two or more Tuples using + operator
vegetables = ('Tomato','Potato','Onion','Carrot')
fruits = ('banana','orange','mango','lemon')
result = fruits + vegetables
print(result)

# Deleting Tuple - It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using 'del'.
fruits = ('banana','orange','mango','lemon')
del fruits