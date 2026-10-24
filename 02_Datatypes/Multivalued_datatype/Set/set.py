# Set - It is a collection of homogeneous and hetrogeneous element enclose in {}.
number = {10,20,30,40,50}
data = {'yash', 101,5.8,True,(4,7)}

'''
Properties of Set - 
- It is one of the datatype which will not allow duplicate values.
- It will be useful in data filteration process.
- It is unordered datatype.
- It will not allow any mutable datatype as a element of a set.
- Set is mutable datatype.
- Because of unordered it will not support indexing and slicing.
- Default value of set is {}
'''

# Checking an item - To check if an item exists in a set we use 'in' operator.
st = {10,20,30,40,50,60}
print(20 in st)

# Method on Set - 

# 1. add() - add() method is a method ehich is use to add individual element to an existing set either it can be single value datatype or multi value datatype [ only immutable ].
# It will insert element at random position..
st = {20,30,40,50}
st.add(10)
st.add((1,2))
print(st)

# 2. update() - This method is used to update the existing set with other value of multivalued datatype.
st = {20,30,40,50}
st.update((1,2))
st.update([12,13])
st.update({14,15,16,17,18})
print(st)

# 3. pop() - It is method which is used to remove or delete the value from existing set one by one from the first position or it will return and remove the first value of set.
# It takes no arguments
st = {20,30,40,50}
st.pop()
print(st)

# 4. remove() - This method is used to remove the value from existing set based on the specified value.
# It takes exactly one arguments
st = {20,30,40,50}
st.remove(20)
st.remove(50)
print(st)

# 5. clear() - If we want to clear pr empty the set then we use 'clear' method.
st = {10,20,30,40,50,60}
st.clear()

# 6. del() - If we want to delete a set itself we use 'del'.
st = {10,20,30,40,50,60,70,80,90}
del st