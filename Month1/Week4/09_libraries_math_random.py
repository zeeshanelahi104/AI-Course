# IMPORTING & USING LIBRARIES (math, random)

print("=" * 50)
print("IMPORTING & USING LIBRARIES")
print("=" * 50)

# ========== IMPORTING MODULES ==========
print("\n--- IMPORTING MODULES ---")

# Method 1: Import entire module
import math
print(f"math.pi = {math.pi}")
print(f"math.e = {math.e}")

# Method 2: Import specific functions
from math import sqrt, pow, factorial
print(f"sqrt(16) = {sqrt(16)}")
print(f"pow(2, 3) = {pow(2, 3)}")
print(f"factorial(5) = {factorial(5)}")

# Method 3: Import with alias
import random as rd
print(f"random number (0-1): {rd.random()}")

# Method 4: Import everything (not recommended)
from math import *
print(f"sin(90°) = {sin(radians(90))}")

# ========== MATH LIBRARY ==========
print("\n" + "=" * 40)
print("MATH LIBRARY")
print("=" * 40)

print("\n--- BASIC MATH FUNCTIONS ---")
num = 16
print(f"sqrt({num}) = {math.sqrt(num)}")
print(f"ceil(3.14) = {math.ceil(3.14)}")    # Round up
print(f"floor(3.14) = {math.floor(3.14)}")  # Round down
print(f"trunc(3.99) = {math.trunc(3.99)}")  # Remove decimal
print(f"fabs(-10) = {math.fabs(-10)}")      # Absolute value

print("\n--- POWER & LOGARITHMS ---")
print(f"pow(2, 8) = {math.pow(2, 8)}")      # 2^8
print(f"exp(2) = {math.exp(2)}")            # e^2
print(f"log(100) = {math.log(100)}")        # Natural log
print(f"log10(100) = {math.log10(100)}")    # Base 10 log

print("\n--- TRIGONOMETRY ---")
angle_deg = 30
angle_rad = math.radians(angle_deg)
print(f"sin({angle_deg}°) = {math.sin(angle_rad):.4f}")
print(f"cos({angle_deg}°) = {math.cos(angle_rad):.4f}")
print(f"tan({angle_deg}°) = {math.tan(angle_rad):.4f}")

print("\n--- CONSTANTS ---")
print(f"π (pi) = {math.pi}")
print(f"e = {math.e}")
print(f"τ (tau) = {math.tau}")
print(f"infinity = {math.inf}")

# ========== RANDOM LIBRARY ==========
print("\n" + "=" * 40)
print("RANDOM LIBRARY")
print("=" * 40)

import random

print("\n--- BASIC RANDOM FUNCTIONS ---")
print(f"random() - 0 to 1: {random.random()}")
print(f"uniform(1, 10) - float: {random.uniform(1, 10):.2f}")
print(f"randint(1, 10) - integer: {random.randint(1, 10)}")
print(f"randrange(0, 100, 5): {random.randrange(0, 100, 5)}")

print("\n--- WORKING WITH SEQUENCES ---")
colors = ["red", "green", "blue", "yellow", "purple"]
print(f"Original list: {colors}")
print(f"choice() - random item: {random.choice(colors)}")
print(f"sample(3 items): {random.sample(colors, 3)}")

random.shuffle(colors)
print(f"After shuffle(): {colors}")

print("\n--- SEEDING RANDOM ---")
random.seed(42)  # Same seed = same random numbers
print(f"With seed 42: {random.randint(1, 100)}")
print(f"With seed 42: {random.randint(1, 100)}")
random.seed(42)
print(f"Reset seed 42: {random.randint(1, 100)}")

# ========== PRACTICE PROJECTS ==========
print("\n" + "=" * 50)
print("PRACTICE PROJECTS")
print("=" * 50)

print("\nProject 1: Dice Roller")
print("Create a function roll_dice(sides=6) that returns random number.")
print("Roll two dice and display result.")

print("\nProject 2: Circle Calculator")
print("Use math library to calculate:")
print("- Area of circle: πr²")
print("- Circumference: 2πr")
print("- Volume of sphere: (4/3)πr³")

print("\nProject 3: Password Generator")
print("Generate random password with:")
print("- Uppercase, lowercase, digits, special chars")
print("- Length specified by user")

print("\nProject 4: Math Quiz Game")
print("Generate random math questions (addition, subtraction, multiplication)")
print("Keep score and give feedback.")

print("\nProject 5: Lottery Number Generator")
print("Generate 6 unique random numbers between 1 and 49.")

print("\nProject 6: Rock Paper Scissors")
print("Play against computer using random choice.")

print("\nProject 7: Quadratic Equation Solver")
print("Use math.sqrt() to solve: ax² + bx + c = 0")