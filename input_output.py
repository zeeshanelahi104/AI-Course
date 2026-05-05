# INPUT and OUTPUT

# Basic output
print("Hello! Welcome to Python")

# Basic input
name = input("What is your name? ")
print("Nice to meet you,", name)

# Input always returns string - need to convert for numbers
age = input("How old are you? ")
age = int(age)  # Convert string to integer
print("Next year you will be", age + 1)

# Better way - convert on the spot
height = float(input("Enter your height in meters: "))
print(f"Your height is {height} meters")

# Building a sentence with f-strings (formatted strings)
name = input("Enter name: ")
city = input("Enter city: ")
print(f"Hello {name} from {city}!")

# Multiple inputs in one line
x, y = input("Enter two numbers separated by space: ").split()
x = int(x)
y = int(y)
print(f"Sum: {x + y}")
# Complete Calculator Program
# SIMPLE CALCULATOR
print("=" * 30)
print("     SIMPLE CALCULATOR")
print("=" * 30)

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculate results
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2 if num2 != 0 else "Cannot divide by zero"

# Display results
print("\n--- RESULTS ---")
print(f"{num1} + {num2} = {sum_result}")
print(f"{num1} - {num2} = {difference}")
print(f"{num1} × {num2} = {product}")
print(f"{num1} ÷ {num2} = {division}")
