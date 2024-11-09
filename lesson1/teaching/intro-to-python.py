# This is a comment
'''
This is a multiline comment
'''

print("Hello world!") #This is a function

## Looking at errors
# print(Hello world!)
      
# print("Hello world!)

hello = "Hello world" ## Creates a variable called hello using the assignment operator
x = 5
print(x)
x = x+1
## What is the difference between = in python and = in math?
print(x)
print(hello)

## Variables are case sensitive
# print(Hello)

## Errors
# Theres 2 main types of error in python
# Syntax and Runtime
# Syntax error is when the code you write isn't allowed in the python language
# print("Hello, world)
# Runtime error is when the code is allowed but cannot be run
# print(Hello)
# This code has correct syntax. However, there is no variable called Hello or world to be printed
# This can be only known when the code is run, hence the name

## Printing
# You can print out values of variables and strings
print(hello, "! What's up?")
print("One kilobyte is ", 2**10, "bytes")
# Or you can use f-strings (which we will delve into more detail in the future)
print(f"The value of the hello variable is {hello}")
print(f"One kilobyte is {2**10} bytes")

print("hello")
print(hello)

name = "James"
print("Hello", name)