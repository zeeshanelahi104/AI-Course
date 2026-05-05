# DATA TYPES in Python

# String (text) - use quotes
name = "Ahmed"
message = 'Hello Python'
multiline = """This is
a multi-line
string"""

print("String examples:")
print(name)
print(type(name))  # Check type

# Integer (whole number)
age = 25
score = -10
population = 8400000

print("\nInteger examples:")
print(age)
print(type(age))

# Float (decimal number)
price = 19.99
temperature = 36.5
pi = 3.14159

print("\nFloat examples:")
print(price)
print(type(price))

# Boolean (True/False)
is_student = True
is_graduated = False

print("\nBoolean examples:")
print(is_student)
print(type(is_student))

# Check type of any variable
print("\nType checking:")
print(type("Hello"))   # <class 'str'>
print(type(100))       # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type(True))      # <class 'bool'>
