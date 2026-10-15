# String (str) - Collection of character enclosed between the pairs of either single quotes ('') or double quotes ("") or triple quotes (''' ''').
# To repesent multi line string we can use only triple quotes this  string is also called as doc string.
# Default value of string is ''.

str = ''' Python
        is
            easy '''
print(str)

# Indexing a string - A process of extracting single character at a time. Indexing can be positive [starts with 0] or negative [starts with -1].

a = 'hello'
print(a[0]) # Output - 'h' 

a = 'hello'
print(a[-5]) # Output - 'h'

a = 'hello'
print(a[3]) # Output - 'l'

str = 'Python is easy'
print(len(str)) # 14
print(len(str) - 1) # 13
print(str[-len(str)]) # 'P'

# Slicing a string - Process of extracting multiple character at a time simultaneously.
# Note - Element at the end index will not be added in the slice.

str = 'Python is easy'
result = str[0:5:1] # Pytho
result = str[7:9:1] # is
result = str[10:14:1] # easy
result = str[1:14:2] # Pto ses
result = str[-14:-8:1] # Python
print(result)

# Start index -> Default value -> 0
# End index -> Default value -> length of the string
# Step value -> Default value -> 1 

str = 'Python is easy'
result = str[::] # Python is easy
result = str[:6:] # Python
result = str[::2] # Pto ses
result = str[10::] # easy
print(result)

# Note - To extract N number of starting character from the string we can use generalized simplified.
a = 'hello'
result = a[:4:] # 'hell'
print(result)

# Note - To extract N number of last character from the string we can use simplified syntax.
st = 'Python is easy'
result = st[-4::] # 'easy'
print(result)

# Reverse a string
st = 'Python is easy'
result = st[14::-1]
print(result)

# Methods of String

# 1. dir() - It is an in built function, which returns a list of attribute that are attached to the object / class.

# 2. lower() - It converts a string into lower case.
print("GOOD MORNING".lower())

# 3. upper() - It converts a string into upper case.
print("good morning".upper())

# 4. swapcase() - It converts a lowercase character into uppercase and uppercase to lowercase character.
print("GooD MorNinG".swapcase()) 

# 5. count() - Returns the number of occurrence of a substring in the original string.
print("GOOD MORNING".count('O'))