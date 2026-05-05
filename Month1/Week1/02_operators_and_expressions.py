# OPERATORS & EXPRESSIONS in Python

print("=" * 50)
print("OPERATORS & EXPRESSIONS")
print("=" * 50)

# ARITHMETIC OPERATORS
print("\n--- ARITHMETIC OPERATORS ---")
a = 10
b = 3

print(f"{a} + {b} = {a + b}")   # Addition
print(f"{a} - {b} = {a - b}")   # Subtraction
print(f"{a} * {b} = {a * b}")   # Multiplication
print(f"{a} / {b} = {a / b:.3f}")   # Division (float)
print(f"{a} / {b} = {round(a / b, 2)}")   # Division (float)
print(f"{a} // {b} = {a // b}") # Floor division (integer)
print(f"{a} % {b} = {a % b}")   # Modulus (remainder)
print(f"{a} ** {b} = {a ** b}") # Exponentiation (power)

# ORDER OF OPERATIONS (PEMDAS)
print("\n--- ORDER OF OPERATIONS (PEMDAS) ---")
print("PEMDAS: Parentheses → Exponents → Multiplication/Division → Addition/Subtraction")
print(f"2 + 3 * 4 = {2 + 3 * 4}")        # Multiplication first: 2 + 12 = 14
print(f"(2 + 3) * 4 = {(2 + 3) * 4}")    # Parentheses first: 5 * 4 = 20
print(f"2 ** 3 + 1 = {2 ** 3 + 1}")      # Exponent first: 8 + 1 = 9
print(f"10 - 2 * 3 + 4 = {10 - 2 * 3 + 4}")  # 10 - 6 + 4 = 8

# COMPARISON OPERATORS
print("\n--- COMPARISON OPERATORS ---")
x = 10
y = 20
print(f"x = {x}, y = {y}")
print(f"x == y (equal to): {x == y}")
print(f"x != y (not equal): {x != y}")
print(f"x > y (greater than): {x > y}")
print(f"x < y (less than): {x < y}")
print(f"x >= y (greater or equal): {x >= y}")
print(f"x <= y (less or equal): {x <= y}")

# LOGICAL OPERATORS
print("\n--- LOGICAL OPERATORS ---")
is_sunny = True
is_warm = True
print(f"is_sunny = {is_sunny}, is_warm = {is_warm}")
print(f"is_sunny and is_warm: {is_sunny and is_warm}")  # Both True = True
print(f"is_sunny or is_warm: {is_sunny or is_warm}")    # At least one True = True
print(f"not is_sunny: {not is_sunny}")                  # Opposite

# ASSIGNMENT OPERATORS
print("\n--- ASSIGNMENT OPERATORS ---")
num = 5
print(f"Initial: num = {num}")
num += 3    # num = num + 3
print(f"After num += 3: {num}")
num -= 2    # num = num - 2
print(f"After num -= 2: {num}")
num *= 4    # num = num * 4
print(f"After num *= 4: {num}")
num /= 2    # num = num / 2
print(f"After num /= 2: {num}")
num //= 2   # Floor division assignment
print(f"After num //= 2: {num}")

# ========== PRACTICE TASKS ==========
print("\n" + "=" * 50)
print("PRACTICE TASKS")
print("=" * 50)

print("\nTask 1: Calculate the area of a rectangle (length * width).")
print("Use length = 15, width = 8.")

print("\nTask 2: Check if a number is even or odd using modulus operator.")
print("Hint: number % 2 == 0 means even.")

print("\nTask 3: Write an expression that is True only if:")
print("a is greater than 10 AND b is less than 20")

print("\nTask 4: Use PEMDAS to calculate: (5 + 3) * 2 ** 2 / 4")
print("Write the code and check the result.")

print("\nTask 5: Create a temperature converter: Celsius to Fahrenheit")
print("Formula: F = (C * 9/5) + 32")
print("Test with C = 25")