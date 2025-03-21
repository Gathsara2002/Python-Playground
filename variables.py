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

# Many Values to Multiple Variables
name1, age1, weight1 = "Alex", 24, 62.5
print(name1, age1, weight1)

mango = 50
apple = 50
orange = 50
print(mango, apple, orange)

# One Value to Multiple Variables
mango1 = apple1 = orange1 = 50
print(mango1, apple1, orange1)

# concat strings
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)  # Python is awesome

"""
Varable naming convention
-A variable name must start with a letter or the underscore character
-A variable name cannot start with a number
-A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
-Variable names are case-sensitive (age, Age and AGE are three different variables)
-A variable name cannot be any of the Python keywords.
"""
