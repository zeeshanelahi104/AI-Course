# VARIABLES & DATA TYPES in Python

# What is a Variable?
# Variables are containers for storing data values
name = "Alice"        # String (text)
age = 25              # Integer (whole number)
height = 5.6          # Float (decimal number)
is_student = True     # Boolean (True/False)

print("=" * 50)
print("VARIABLES & DATA TYPES")
print("=" * 50)

# STRING (str)
print("\n--- STRING DATA TYPE ---")
greeting = "Hello, World!"
single_quoted = 'Python is fun'
multi_line = """This is
a multi-line
string"""
# print ("String: " + greeting + " | " + single_quoted + " | " + multi_line)
print(f"String: {greeting}")
print(f"Type: {type(greeting)}")
print(f"First character: {greeting[0]}")
print(f"Length: {len(greeting)}")

# INTEGER (int)
print("\n--- INTEGER DATA TYPE ---")
count = 10
negative_num = -5
zero = 0
print(f"Integer: {count}")
print(f"Type: {type(count)}")
print(f"Addition: {count + 5}")
print(f"Subtraction: {count - 3}")

# FLOAT (float)
print("\n--- FLOAT DATA TYPE ---")
price = 19.99
pi = 3.14159
print(f"Float: {price}")
print(f"Type: {type(price)}")
print(f"Multiplication: {price * 2}")

# BOOLEAN (bool)
print("\n--- BOOLEAN DATA TYPE ---")
is_raining = True
has_license = True
print(f"Boolean: {is_raining}")
print(f"Type: {type(is_raining)}")
print(f"NOT operator: {not is_raining}")

# TYPE CONVERSION (Casting)
print("\n--- TYPE CONVERSION ---")
num_str = "123"
num_int = int(num_str)      # String to Integer
num_float = float(num_str)  # String to Float
print(f'String "{num_str}" to int: {num_int}')
print(f'String "{num_str}" to float: {num_float}')

# Checking Variable Types
print("\n--- CHECKING TYPES ---")
print(f"Is 'age' an integer? {isinstance(age, int)}")
print(f"Is 'name' a string? {isinstance(name, str)}")

# # ========== PRACTICE TASKS ==========
# print("\n" + "=" * 50)
# print("PRACTICE TASKS")
# print("=" * 50)

# print("\nTask 1: Create variables for your:")
# print("- First name")
# print("- Last name")
# print("- Age")
# print("- Height")
# print("- Is student?")
# print("Then print them all.")

# print("\nTask 2: Convert the string '99.99' to a float and multiply by 2.")
# print("Hint: float('99.99')")

# print("\nTask 3: Create two numbers and swap their values without using a third variable.")
# print("Hint: a, b = b, a")

# print("\nTask 4: Find the data type of the result: 10 / 3")
# print("Write the code and print the type.")

# print("\nTask 5: Create a variable that stores your favorite quote (multi-line).")
# print("Print it with line breaks.")