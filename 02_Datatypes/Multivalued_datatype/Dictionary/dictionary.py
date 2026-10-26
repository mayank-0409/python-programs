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

# 2. update() - Update the existing dictionary with the specified items.
temp = {'mumbai':20,'Pune':30,'Delhi':50}
temp.update({'Delhi':27, 'Chennai':34})
temp.update(Balglore = 30)
print(temp)

# 3. pop() - Removes the specified item from the dictionary, Returns the removed value as output.
# Syntax - variable_name.pop(key_name, default_value)
# If the specified key dos not exist then it will return default value
data = {'name':'Maya','age':21}
print(data.pop('age','key value is not present in the dict'))
print(data)

# 4. popitem() - Removes the item that was inserted at last or present at last into the dictionary.
# Syantax - variable_name.popite()
data = {'name':'Maya','age':21}
data.popitem()
print(data)

# 5. items() - This method returns a view objecct. Returns the key-value pairs of the dictionary as tuples in a list.
temp = {'mumbai':20,'pune':30,'Banglore':40}
i = temp.items()
print(i)

# 6. keys() - Returns the list of all the keys present in the dictionary.
temp = {'mumbai':20,'pune':30,'Banglore':40}
k = temp.keys()
print(k)

# 7. values() - Returns the list of all the values.
temp = {'mumbai':20,'pune':30,'Banglore':40}
v = temp.values()
print(v)

# 8. del() - Removes an item with specified key name.
temp = {'mumbai':20,'pune':30,'Banglore':40}
del temp['Banglore']
print(temp)