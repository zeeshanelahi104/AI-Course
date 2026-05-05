# OPERATORS in Python

# Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print(f"{a} + {b} = {a + b}")   # Addition
print(f"{a} - {b} = {a - b}")   # Subtraction
print(f"{a} * {b} = {a * b}")   # Multiplication
print(f"{a} / {b} = {a / b}")   # Division (float result)
print(f"{a} // {b} = {a // b}") # Floor division (integer) 10//3 = 3
print(f"{a} % {b} = {a % b}")   # Modulus (remainder)
print(f"{a} ** {b} = {a ** b}") # Exponent (power) 1000

# Order of Operations (PEMDAS)
print("\nOrder of Operations:")
print("2 + 3 * 4 =", 2 + 3 * 4)      # Multiplication first: 2 + 12 = 14
print("(2 + 3) * 4 =", (2 + 3) * 4)  # Parentheses first: 5 * 4 = 20

# Assignment Operators
x = 5
print(f"\nInitial x = {x}")
x += 3  # Same as x = x + 3
print(f"After x += 3: {x}")
x -= 2  # Same as x = x - 2
print(f"After x -= 2: {x}")
x *= 4  # Same as x = x * 4
print(f"After x *= 4: {x}")
x /= 2  # Same as x = x / 2
print(f"After x /= 2: {x}")


number = 10
isEven = (number % 2 == 0)  # True if number is even
print(f"\nIs {number} even? {isEven}")