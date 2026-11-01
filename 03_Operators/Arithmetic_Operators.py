# Arithmetic Operations

# 1. Addition - Addition is an operator which is used to find sum between two or more operands.
# Syntax - operand 1 + operand 2 ( Addition for Single value Datatype )
a, b = 5, 10
print(a + b)  # Output - 15
# Syntax - collection 1 + collection 2 ( Concatination for Collection Datatype )
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)  # Output - [1, 2, 3, 4, 5, 6]
# We can add two single value operands of any type but in case of concatination both the collection should be same type. 
# Concatination will not support for set() and dict() data types.  

# 2. Subtraction - Subtraction is an operator which is used to find the difference between two or more operands.
# Syntax - Operand 1 - Operand 2 ( Subtraction for Single value Datatype )
a, b = 10, 5    
print(a - b)  # Output - 5
# It will also suport for collection data types only for set.
a = {1,2,3,4}
b = {3,4,5,6}
print(a - b)  # Output - {1, 2} ( It will return the difference between two sets )

# 3. Multiplication - Multiplication is an operator which is used to find the product between two or more operands.
# Syntax - Operand 1 * Operand 2 ( Multiplication for Single value Datatype )
a, b = 10, 5
print(a * b)  # Output - 50
#  We can multiply one single value datatype with another single value datatype but in case of collection, we can multiply it with interger number.
# Multiplication will not support for set and dictionary.

# 4. Division - Division is an operator which is used to find the division output between two or more operands.
# Division Operator is further classified into 3 types.
# i. True Division - It is division which is used to get the exact division output along with decimal values.
# Syntax - Operand 1 / Operand 2 ( True Division will support for Single value Datatype but not for Collection Datatype )
a, b = 10, 3
print(a / b)  # Output - 3.3333333333333335
