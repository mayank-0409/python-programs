# Dictionary - It is a collection of key value pairs seperated by commas and ecnclosed in curly braces {}. Each element is associated with unique key.
# It does not support indexing and slicing. 
data = {1:'Maya',2:'Amit',3:'Jack'}

'''
Characteristics of Dictionary
- Key cannot be duplicate
- Key will be single element
- Value can be of any datatype 
- Vallues can be accessed through keys only
- Key must be of immutable datatype
- Dict is a mutable data type
'''

# Dictionary value lookup method -
# It is produce to access the dictionary values based on the keys. If the key is present it will return the value of the key if key is not there it will throw the key error.
temp = {'mumbai':20,'Pune':30,'Delhi':50}
print(temp['mumbai'])
print(temp['Delhi'])


# If the key is already existed it will update the value if the key is not present in the dictionary then it will insert both the key and value pair at the last position of the existing dictionary.
temp['Banglore'] = 20
print(temp)

# Methods on Dictionary - 
# 1. get() - Returns the value of the item with the specified key.
data = {'name':'Maya', 'age':23, 'Punjab':30}
print(data['name'])
print(data.get('age'))

# If the value is not present, then it will not throw the error instead it will return 'None' by default if the second argument is not given.
print(data.get('Banglore'))
print(data.get('Banglore', 'The Banglore key is not present in the Dict'))

# 2. update() - 
