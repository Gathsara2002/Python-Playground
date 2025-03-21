# Variables are containers for storing data values

"""
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
"""

name = "John"
age = 23
weight = 60.4

print(name)
print(age)
print(weight)

print(type(name))  # string
print(type(age))  # int
print(type(weight))  # float

"""
In python can't create variable without assigning a value.Otherise it will give erro

height 
print(height)

output -> NameError: name 'height' is not defined.
"""

name1, age1, weight1 = "Alex", 24, 62.5
print(name1, age1, weight1)

mango = 50
apple = 0
orange = 0
print(mango, apple, orange)

mango1 = apple1 = orange1 = 50
print(mango1, apple1, orange1)
