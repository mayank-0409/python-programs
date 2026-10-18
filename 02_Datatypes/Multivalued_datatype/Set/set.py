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