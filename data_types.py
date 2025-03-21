"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

# Integer - (int)
a = 10
b = -25
c = 775585748300303839330
print(type(a))  # <class 'int'>
print(c.__sizeof__())

# Float
d = 12.334
print(type(d))  # <class 'float'>

# Boolean (first letter capital)
e = True
f = False
print(type(e))  # <class 'bool'>
print(type(f))  # <class 'bool'>

# Complex
g = 5 + 6j
print(type(g))  # <class 'complex'>
print((g.real))
print(g.imag)
