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

# 6. index() - Returns the index of first occurrence of the letter.
print("Good Morning".index('o'))

# 7. rindex() - Searches the string for a specified value and returns the last position of where it was found.
print("Good Morning".rindex('o'))

# 8. startswith() - This function returns True if the string starts with the given specified value, otherwise it returns false. 
print("Good Morning".startswith('Good'))
print("Good Morning".startswith('Morning'))

# 9. endswith() - This function returns True if the string ends with the given specified value, otherwise it returns false.
print("Good Morning".endswith('Good'))
print("Good Morning".endswith('Morning'))           

# 10. expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty days of python'
print(challenge.expandtabs())   # 'thirty days      of       python'
print(challenge.expandtabs(10))  # 'thirty    days      of        python'

# 11. find(): Returns the index of first occurrence of substring
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0

# Unpacking Character - 
language = 'Python'
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Escape Sequence
print("I hope everyone is enjoying the python. \nDo you?")
print("Days\tTopics\tExcersise")
print("Day 1\t3\t5")
print("Day 2\t2\t4")
print("Day 3\t1\t6")
print("Day 4\t4\t5")
print("This is the back slash symbol (\\)")
print("In every programming language it starts with \'Hello world!\' ")