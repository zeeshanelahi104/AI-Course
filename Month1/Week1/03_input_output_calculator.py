# INPUT/OUTPUT & BASIC CALCULATOR in Python

print("=" * 50)
print("INPUT/OUTPUT & BASIC CALCULATOR")
print("=" * 50)

# BASIC OUTPUT with print()
print("\n--- BASIC OUTPUT ---")
print("Hello, World!")
print("Python", "is", "awesome", sep="-")  # Custom separator
print("This is on first line", end=" ")    # No newline
print("and this continues on same line")
print()

# USING f-STRINGS (formatted strings)
print("\n--- f-STRINGS ---")
name = "Bob"
age = 30
print(f"My name is {name} and I am {age} years old.")
print(f"In 5 years, I will be {age + 5}.")

# USING .format() METHOD
print("\n--- .format() METHOD ---")
print("My name is {} and I am {} years old.".format(name, age))

# BASIC INPUT with input()
print("\n--- BASIC INPUT ---")
# input() always returns a STRING
user_name = input("What is your name? ")
print(f"Hello, {user_name}!")

# Converting input to numbers
age_input = input("Enter your age: ")
age_number = int(age_input)  # Convert string to integer
print(f"Next year you'll be {age_number + 1}")

# BASIC CALCULATOR
print("\n" + "=" * 50)
print("BASIC CALCULATOR")
print("=" * 50)

print("Welcome to the Python Calculator!")
print("Operations: +, -, *, /, //, %, **")

# Get user input
num1 = float(input("\nEnter first number: "))
operator = input("Enter operator (+, -, *, /, //, %, **): ")
num2 = float(input("Enter second number: "))

# Perform calculation
print("\n" + "-" * 30)
print("RESULT:")
print("-" * 30)

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} × {num2} = {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} ÷ {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")
elif operator == "//":
    if num2 != 0:
        result = num1 // num2
        print(f"{num1} // {num2} = {result} (floor division)")
    else:
        print("Error: Cannot divide by zero!")
elif operator == "%":
    if num2 != 0:
        result = num1 % num2
        print(f"{num1} % {num2} = {result} (remainder)")
    else:
        print("Error: Cannot divide by zero!")
elif operator == "**":
    result = num1 ** num2
    print(f"{num1} ^ {num2} = {result}")
else:
    print("Invalid operator!")

# ========== PRACTICE TASKS ==========
print("\n" + "=" * 50)
print("PRACTICE TASKS")
print("=" * 50)

print("\nTask 1: Create a program that asks for the user's favorite color.")
print("Then print: 'Wow, [color] is a beautiful color!'")

print("\nTask 2: Create a simple interest calculator.")
print("Formula: Simple Interest = (Principal × Rate × Time) / 100")
print("Ask user for Principal, Rate, and Time, then display the interest.")

print("\nTask 3: Create a BMI Calculator.")
print("Formula: BMI = weight(kg) / height(m)²")
print("Ask for weight and height, calculate and display BMI.")

print("\nTask 4: Create a program that converts minutes to hours and minutes.")
print("Example: 130 minutes = 2 hours and 10 minutes.")

print("\nTask 5: Build a 'Shopping Bill' calculator.")
print("Ask for 3 item prices, calculate subtotal, tax (10%), and total.")