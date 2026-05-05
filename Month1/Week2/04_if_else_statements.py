# IF-ELSE STATEMENTS in Python

print("=" * 50)
print("IF-ELSE STATEMENTS")
print("=" * 50)

# SIMPLE IF STATEMENT
print("\n--- SIMPLE IF STATEMENT ---")
age = 20
if age >= 18:
    print("You are eligible to vote!")

# # IF-ELSE STATEMENT
print("\n--- IF-ELSE STATEMENT ---")
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's pleasant outside!")

# IF-ELIF-ELSE STATEMENT
print("\n--- IF-ELIF-ELSE STATEMENT ---")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# MULTIPLE CONDITIONS with AND/OR
print("\n--- MULTIPLE CONDITIONS ---")
age = 20
has_license = True

if age >= 18 and has_license:
    print("You can drive a car!")
else:
    print("You cannot drive yet.")

# NESTED IF STATEMENTS
print("\n--- NESTED IF STATEMENTS ---")
num = 15

if num > 0:
    print(f"{num} is positive")
    if num % 2 == 0:
        print(f"{num} is also even")
    else:
        print(f"{num} is also odd")
else:
    print(f"{num} is not positive")

# TERNARY OPERATOR (Short-hand if-else)
print("\n--- TERNARY OPERATOR ---")
age = 16
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age}: {status}")

# REAL-WORLD EXAMPLE: Login System
print("\n--- REAL-WORLD EXAMPLE: Login System ---")
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("✅ Login successful! Welcome admin.")
elif username == "admin":
    print("❌ Incorrect password!")
else:
    print("❌ Username not found!")

# ========== PRACTICE TASKS ==========
print("\n" + "=" * 50)
print("PRACTICE TASKS")
print("=" * 50)

print("\nTask 1: Number Guesser")
print("Ask user for a number. Print:")
print("- 'Positive' if > 0")
print("- 'Negative' if < 0")
print("- 'Zero' if = 0")

print("\nTask 2: Even or Odd Checker")
print("Ask for a number and tell if it's even or odd.")

print("\nTask 3: Leap Year Checker")
print("A year is leap if: divisible by 4 BUT not by 100, OR divisible by 400")
print("Check with year = 2024, 1900, 2000")

print("\nTask 4: Maximum of Three Numbers")
print("Ask for 3 numbers and print the largest one.")

print("\nTask 5: Simple Calculator with Validation")
print("Ask for two numbers and an operator.")
print("Check if operator is valid before calculating.")