# FUNCTIONS in Python

print("=" * 50)
print("FUNCTIONS")
print("=" * 50)

# ========== DEFINING FUNCTIONS ==========

# Simple function (no parameters, no return)
print("\n--- SIMPLE FUNCTION ---")
def greet():
    print("Hello! Welcome to Python functions!")

greet()  # Calling the function

# Function with parameters
print("\n--- FUNCTION WITH PARAMETERS ---")
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Ali")
greet_person("Ahmad")

# Function with multiple parameters
print("\n--- FUNCTION WITH MULTIPLE PARAMETERS ---")
def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add(5, 3)
# add(10, 20)

# Function with return value
print("\n--- FUNCTION WITH RETURN VALUE ---")
def multiply(x, y):
    return x * y

product = multiply(4, 5)
print(f"4 × 5 = {product}")

# Function with default parameters
print("\n--- FUNCTION WITH DEFAULT PARAMETERS ---")
def introduce(name, age=18, country="Pakistan"):
    print(f"Name: {name}, Age: {age}, Country: {country}")

introduce("Ali")
introduce("Sara", 22)
introduce("John", 25, "USA")

# Function with keyword arguments
print("\n--- FUNCTION WITH KEYWORD ARGUMENTS ---")
def student_info(name, course, grade):
    print(f"{name} is taking {course} and got grade {grade}")

student_info(course="Python", name="Ahmed", grade="A")

# ========== SCOPE OF VARIABLES ==========
print("\n--- VARIABLE SCOPE ---")

global_var = "I am global"  # Global variable

def show_scope():
    local_var = "I am local"  # Local variable
    print(f"Inside function: {local_var}")
    print(f"Inside function - accessing global: {global_var}")

show_scope()
# print(local_var)  # This would cause an error (local_var not accessible)
print(f"Outside function: {global_var}")

# ========== LAMBDA FUNCTIONS (Anonymous Functions) ==========
print("\n--- LAMBDA FUNCTIONS ---")

# Regular function
def square(x):
    return x ** 2

# Lambda function (one-liner)
square_lambda = lambda x: x ** 2 # same as above but shorter syntax

print(f"Regular function: square(5) = {square(5)}")
print(f"Lambda function: square_lambda(5) = {square_lambda(5)}")

# # Lambda with multiple parameters
add_lambda = lambda a, b: a + b
print(f"Lambda add: {add_lambda(10, 20)}")


# # ========== PRACTICE PROJECTS ==========
# print("\n" + "=" * 50)
# print("PRACTICE PROJECTS")
# print("=" * 50)

# print("\nProject 1: Temperature Converter Functions")
# print("Create functions: celsius_to_fahrenheit(c) and fahrenheit_to_celsius(f)")

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print(f"100°C = {celsius_to_fahrenheit(100)}°F")
print(f"212°F = {fahrenheit_to_celsius(212)}°C")

# print("\nProject 2: Area Calculator")
# print("Create separate functions for area of: circle, rectangle, triangle")

def area_circle(radius):
    import math
    return math.pi * radius ** 2
def area_rectangle(length, width):
    return length * width
def area_triangle(base, height):
    return 0.5 * base * height

area_circle = area_circle(5)
area_rectangle = area_rectangle(4, 6)
area_triangle = area_triangle(4, 5)

print(f"Area of circle: {area_circle}")
print(f"Area of rectangle: {area_rectangle}")
print(f"Area of triangle: {area_triangle}")

# print("\nProject 3: Simple Calculator with Functions")
# print("Create functions: add(), subtract(), multiply(), divide()")
# print("Then create a main calculator function that uses them")

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
    
def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")
    
    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        result = "Invalid operation"
    
    print(f"Result: {result}")

calculated_value = calculator()

print(f"Calculated value: {calculated_value}")

# print("\nProject 4: Number Properties")
# print("Create functions:")
# print("- is_even(n) - returns True/False")
# print("- is_prime(n) - returns True/False")
# print("- get_factors(n) - returns list of factors")

def is_even(n):
    return n % 2 == 0
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # Check up to square root of n for efficiency why? Because if n is divisible by any number greater than its square root, it must have a corresponding factor that is less than the square root. Therefore, we only need to check for factors up to the square root to determine if n is prime.
        if n % i == 0: # If n is divisible by any number other than 1 and itself, it's not prime
            return False
    return True
def get_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors
number = int(input("Enter a number to check properties: "))
print(f"Is {number} even? {is_even(number)}")
print(f"Is {number} prime? {is_prime(number)}")
print(f"Factors of {number}: {get_factors(number)}")


# print("\nProject 5: Mini Game - Guess the Number")
# print("Create functions:")
# print("- generate_secret() - returns random number")
# print("- get_guess() - gets user input")
# print("- check_guess(guess, secret) - returns hint")
# print("- play_game() - main game loop")


def generate_secret():
    import random
    return random.randint(1, 10)
def get_guess():
    return int(input("Guess the number (1-10): "))
def check_guess(guess, secret):
    if guess < secret:
        return "Too low!"
    elif guess > secret:
        return "Too high!"
    else:        
        return "Correct!"
def play_game():
    secret_number = generate_secret()
    attempts = 0
    # max_attempts = 5
    while True:
        # if attempts >= max_attempts:
        #     print("You've reached the maximum number of attempts.")
        #     break
        guess = get_guess()
        attempts += 1
        hint = check_guess(guess, secret_number)
        print(hint)
        if hint == "Correct!":
            print(f"You got it in {attempts} attempts!")
            break
play_game()

# print("\nProject 6: Password Strength Checker")
# print("Create function check_password_strength(password)")
# print("Returns: 'Weak', 'Medium', or 'Strong' based on:")
# print("- Length (min 8 chars)")
# print("- Contains uppercase, lowercase, digit, special char")


def check_password_strength(password):
    import re # Regular expressions for pattern matching
    if len(password) < 8:
        return "Weak"
    elif (re.search(r'[A-Z]', password) and # Check for uppercase letter
          re.search(r'[a-z]', password) and # Check for lowercase letter
          re.search(r'[0-9]', password) and # Check for digit
          re.search(r'[@$!%*?&]', password)): # Check for special character
        return "Strong"
    else:
        return "Medium"
password = input("Enter a password to check strength: ")
strength = check_password_strength(password)
print(f"Password strength: {strength}")