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
result = str[10::1] # easy
result = str[::2] # Pto ses
result = str[-14:-8:1] # Python
print(result)

# Start index -> Default value -> 0
# End index -> Default value -> length of the string
# Step value -> Default value -> 1 