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
print(len(str))
print(len(str) - 1)
print(str[-len(str)])