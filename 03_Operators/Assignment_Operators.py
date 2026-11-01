# Assignment Operators
Assignment operators are programming constructs used to assign values to variables, with the simple assignment operator (=) taking the value from the right-hand side and storing it in the left-hand variable. 

Compound assignment operators combine arithmetic, bitwise, or logical operations with assignment to update a variable concisely:

Arithmetic: += (add), -= (subtract), *= (multiply), /= (divide), %= (modulus), and **= (exponent, Python-specific). 
Bitwise: &= (AND), |= (OR), ^= (XOR), <<= (left shift), >>= (right shift). 
Logical/Null: &&=, ||=, and ??= (assign only if left operand is null/undefined, supported in JavaScript, C#, and PHP). 
These operators are syntactic sugar where x op= y is equivalent to x = x op y, though they often evaluate the left-hand operand only once, which can affect side effects in complex expressions.
