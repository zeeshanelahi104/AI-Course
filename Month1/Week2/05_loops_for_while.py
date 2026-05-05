print("=" * 50)
print("LOOPS (FOR & WHILE)")
print("=" * 50)

# ========== FOR LOOPS ==========
print("\n--- FOR LOOPS ---")

# Looping through a range
print("\n1. Looping through range:")
for i in range(5):  # 0 to 4
    print(f"Iteration {i}")

# Range with start, stop, step
print("\n2. Range with start, stop, step:")
for i in range(2, 10, 3):  # 2, 5, 8
    print(i, end=" ")
print()

# Looping through a string
print("\n3. Looping through a string:")
word = "Learning Python"
for letter in word:
    print(letter)

# Looping through a list
print("\n4. Looping through a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")


# Using enumerate() -> gives index + value
print("\n5. Using enumerate():")
colors = ["red", "green", "blue"] # item 1 colors[0] = "red", colors[1] = "green", colors[2] = "blue"
for i in colors:
    print(i)
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# Using zip() -> loop through multiple lists together
print("\n6. Using zip():")
names = ["Ali", "Ahmed", "Sara"]
marks = [85, 90, 78]

for name, mark in zip(names, marks):
    print(f"{name} got {mark} marks")

# Nested loops (Multiplication Table)
print("\n7. Multiplication Table (Nested Loops):")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:5}", end=" ") # :5 means 5 spaces for each number, right aligned
    print() # new line after each row

# ========== LOOP CONTROL STATEMENTS ==========
print("\n--- LOOP CONTROL STATEMENTS ---")

# BREAK
print("\n1. BREAK statement:")

for i in range(10):
    if i == 5:
        break

    print(i, end=" ")

print("\nLoop stopped at 5")

# CONTINUE
print("\n2. CONTINUE statement:")

for i in range(10):
    if i % 2 == 0:
        continue

    print(i, end=" ")

print("\n(Only odd numbers printed)")

# PASS statement
print("\n3. PASS statement:")

for i in range(5):
    if i == 3:
        pass  # Placeholder for future code

    print(i)

# ELSE with loops
print("\n4. ELSE with loops:")

for i in range(3):
    print(i)

else:
    print("Loop completed normally!")

# Else with break example
print("\n5. ELSE with BREAK example:")

for i in range(5):
    if i == 3:
        print("Loop stopped early!")
        break
else:
    print("Loop completed!")

# ========== LIST COMPREHENSION ==========
print("\n--- LIST COMPREHENSION ---")

# Traditional way
squares = []

for i in range(1, 6):
    squares.append(i * i)

print("Squares:", squares)

# List comprehension
squares2 = [i * i for i in range(1, 6)]

print("Squares using comprehension:", squares2)

# ========== COMMON LOOP PATTERNS ==========
print("\n--- COMMON LOOP PATTERNS ---")

# Sum of numbers
print("\n1. Sum of numbers:")

numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num

print("Total:", total)

# Finding maximum
print("\n2. Finding maximum number:")

numbers = [10, 25, 7, 99, 42]
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum:", maximum)

# Counting characters
print("\n3. Counting vowels:")

text = "programming"
count = 0

for ch in text:
    if ch in "aeiou":
        count += 1

print("Vowels:", count)


# # ========== WHILE LOOPS ==========
# print("\n--- WHILE LOOPS ---")

# # Basic while loop
# print("\n1. Countdown:")
# count = 5

# while count > 0:
#     print(f"Countdown: {count}")
#     count -= 1

# print("Blast off! 🚀")

# # Infinite loop example (commented for safety)
# print("\n2. Infinite Loop Example:")
# print("Example:")
# print("""
# # while True:
# #     print("This runs forever!")
# """)

# # While loop with user input
# print("\n3. Guess the Number Game:")

# secret_number = 7
# guess = 0
# attempts = 0

# while guess != secret_number:
#     guess = int(input("Guess the number (1-10): "))
#     attempts += 1

#     if guess < secret_number:
#         print("Too low!")

#     elif guess > secret_number:
#         print("Too high!")

#     else:
#         print(f"Correct! You got it in {attempts} attempts!")



# # ========== PRACTICE PROJECTS ==========
# print("\n" + "=" * 50)
# print("PRACTICE PROJECTS")
# print("=" * 50)

# # ==================================================
# # PROJECT 1: MULTIPLICATION TABLE
# # ==================================================
# print("\nPROJECT 1: MULTIPLICATION TABLE")

# number = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")

# # ==================================================
# # PROJECT 2: SUM OF FIRST N NUMBERS
# # ==================================================
# print("\nPROJECT 2: SUM OF FIRST N NUMBERS")

# n = int(input("Enter N: "))
# total = 0

# for i in range(1, n + 1):
#     total += i

# print(f"Sum = {total}")

# # ==================================================
# # PROJECT 3: FACTORIAL CALCULATOR
# # ==================================================
# print("\nPROJECT 3: FACTORIAL CALCULATOR")

# number = int(input("Enter a number: "))
# factorial = 1

# for i in range(1, number + 1):
#     factorial *= i

# print(f"Factorial of {number} = {factorial}")

# # ==================================================
# # PROJECT 4: FIBONACCI SEQUENCE
# # ==================================================
# print("\nPROJECT 4: FIBONACCI SEQUENCE")

# n = int(input("How many Fibonacci numbers? "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")

#     next_number = a + b
#     a = b
#     b = next_number

# print()

# # ==================================================
# # PROJECT 5: PASSWORD CHECKER
# # ==================================================
# print("\nPROJECT 5: PASSWORD CHECKER")

# correct_password = "python123"
# password = ""

# while password != correct_password:
#     password = input("Enter password: ")

#     if password != correct_password:
#         print("Wrong password!")

# print("Access Granted!")

# # ==================================================
# # PROJECT 6: SUM OF DIGITS
# # ==================================================
# print("\nPROJECT 6: SUM OF DIGITS")

# number = int(input("Enter a number: "))
# total = 0

# while number > 0:
#     digit = number % 10
#     total += digit
#     number //= 10

# print("Sum of digits =", total)

# # ==================================================
# # PROJECT 7: PALINDROME CHECKER
# # ==================================================
# print("\nPROJECT 7: PALINDROME CHECKER")

# word = input("Enter a word: ")

# reversed_word = word[::-1]

# if word == reversed_word:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# # ==================================================
# # PROJECT 8: PRIME NUMBER CHECKER
# # ==================================================
# print("\nPROJECT 8: PRIME NUMBER CHECKER")

# number = int(input("Enter a number: "))

# if number <= 1:
#     print("Not Prime")

# else:
#     is_prime = True

#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("Prime Number")
#     else:
#         print("Not Prime")

# # ==================================================
# # PROJECT 9: NUMBER GUESSING GAME
# # ==================================================
# print("\nPROJECT 9: NUMBER GUESSING GAME")

# secret = 5
# guess = 0

# while guess != secret:
#     guess = int(input("Guess the number: "))

#     if guess < secret:
#         print("Too Low")

#     elif guess > secret:
#         print("Too High")

# print("Correct!")

# # ==================================================
# # PROJECT 10: STAR PATTERN
# # ==================================================
# print("\nPROJECT 10: STAR PATTERN")

# rows = 5

# for i in range(1, rows + 1):
#     print("*" * i)