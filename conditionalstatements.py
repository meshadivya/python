# Indentation: Indentation in Python refers to the use of spaces or tabs to indent lines of code within a block of code, such as a function, loop, or conditional statement. This indentation is used to denote the grouping of statements and to show the structure of the code.

# In Python, indentation is used instead of brackets or semicolons to define the scope of a block of code. This means that the indentation level of a line of code determines its position within the block.

# Conditional Statements:

# If Statement

# The if statement is used to execute a block of code if a certain condition is true.


if condition:
    # code to be executed


#Example:

x = 5
if x > 10:
    print("x is greater than 10")


# If-Else Statement

# The if-else statement is used to execute a block of code if a certain condition is true, and another block of code if the condition is false.


if condition:
    # code to be executed if condition is true
else:
    # code to be executed if condition is false


Example:

x = 5
if x > 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 10")


# If-Elif-Else Statement

# The if-elif-else statement is used to check multiple conditions and execute different blocks of code based on those conditions.


if condition1:
    # code to be executed if condition1 is true
elif condition2:
    # code to be executed if condition1 is false and condition2 is true
else:
    # code to be executed if all conditions are false


# Example:

x = 5
if x > 10:
    print("x is greater than 10")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")


# Nested If Statement

# The nested if statement is used to check multiple conditions and execute different blocks of code based on those conditions.


if condition1:
    if condition2:
        # code to be executed if both conditions are true
    else:
        # code to be executed if condition1 is true and condition2 is false
else:
    # code to be executed if condition1 is false


# Example:

x = 5
y = 10
if x > 5:
    if y > 10:
        print("x is greater than 5 and y is greater than 10")
    else:
        print("x is greater than 5 but y is less than or equal to 10")
else:
    print("x is less than or equal to 5")


# Conditional Expressions (Ternary Operator)

# The ternary operator is used to evaluate a condition and execute one of two possible blocks of code.


# value_if_true if condition else value_if_false


# Example:

x = 5
result = "x is greater than 10" if x > 10 else "x is less than or equal to 10"
print(result)
