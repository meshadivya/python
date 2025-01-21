Here's an overview of Python loops:

For Loops

For loops are used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each item in the sequence.


for variable in sequence:
    # code to be executed


Example:

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)


While Loops

While loops are used to execute a block of code as long as a certain condition is true.


while condition:
    # code to be executed


Example:

i = 0
while i < 5:
    print(i)
    i += 1


Nested Loops

Nested loops are used to execute a loop inside another loop.


for variable1 in sequence1:
    for variable2 in sequence2:
        # code to be executed


Example:

colors = ['red', 'green', 'blue']
shapes = ['circle', 'square', 'triangle']
for color in colors:
    for shape in shapes:
        print(f"{color} {shape}")


Break and Continue Statements

- break: used to exit a loop prematurely
- continue: used to skip to the next iteration of a loop

Example:

for i in range(5):
    if i == 3:
        break
    print(i)



for i in range(5):
    if i == 3:
        continue
    print(i)


Loop Control Statements

- enumerate: used to iterate over a sequence and have access to the index and value of each item
- zip: used to iterate over multiple sequences simultaneously

Example:

fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")



fruits = ['apple', 'banana', 'cherry']
colors = ['red', 'yellow', 'pink']
for fruit, color in zip(fruits, colors):
    print(f"{fruit}: {color}")


Infinite Loops

Infinite loops are loops that have no termination condition.

Example:

while True:
    print("Hello, World!")


Note: Infinite loops should be avoided in most cases, as they can cause the program to run indefinitely.
