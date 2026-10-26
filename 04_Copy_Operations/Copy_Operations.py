from copy import deepcopy
# Copy Operation - Copt Operation is a phenomenon of copying the content of one variable to another variable.
# We can do copy operation only on list collection.
# Copy Operation is classified into 3 types - 

# 1. General Copy / Normal Copy - It is a phenomenon of copying the content of variable space of one variable to another variable.
# In case of general copy the modification of one variable will affect another variable because both the variables are pointing to the same memory address.

a = [1,3,4,5,6]
b = a
print(a)
print(b)

# 2. Shallow Copy - It is phenomenon of copying the content of values space of one variable to another variable.
# Syntax - variable_name = variable_name.copy()
# The list consist of linear values init then modification of one variable do not effect another variable.
a = [1,2,3,4]
b = a.copy()

# 3. Deep Copy - It is a phenomenon of copying everything from one variable to another variable as a new collection.
# Syntax - variable_name = copy.deepcopy(variable_name)
# Once copy is omported we can use it any number of times.
# In deepcopy the modification of one variable will not affect another variable where the collection can be linear or nested.
a = [1,2,[10,20]]
b = deepcopy(a)