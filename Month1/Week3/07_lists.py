# LISTS in Python

print("=" * 50)
print("LISTS")
print("=" * 50)

# ========== CREATING LISTS ==========
print("\n--- CREATING LISTS ---")

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with numbers
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# List with mixed data types
mixed = [10, "hello", 3.14, True]
print(f"Mixed list: {mixed}")

# List constructor
list_from_range = list(range(5))
print(f"List from range: {list_from_range}")

# ========== ACCESSING LIST ELEMENTS ==========
print("\n--- ACCESSING LIST ELEMENTS ---")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(f"Fruits: {fruits}")
print(f"First fruit (index 0): {fruits[0]}")
print(f"Second fruit (index 1): {fruits[1]}")
print(f"Last fruit (index -1): {fruits[-1]}")
print(f"Second last (index -2): {fruits[-2]}")

# Slicing lists [start:end:step]
print(f"\nSlicing examples:")
print(f"fruits[1:4]: {fruits[1:4]}")      # Index 1 to 3
print(f"fruits[:3]: {fruits[:3]}")        # First 3 elements
print(f"fruits[2:]: {fruits[2:]}")        # From index 2 to end
print(f"fruits[::2]: {fruits[::2]}")      # Every second element
print(f"fruits[::-1]: {fruits[::-1]}")    # Reverse list

# ========== MODIFYING LISTS ==========
print("\n--- MODIFYING LISTS ---")

# Changing an element
colors = ["red", "green", "blue"]
print(f"Original: {colors}")
colors[1] = "yellow"
print(f"After colors[1] = 'yellow': {colors}")

# Adding elements
colors.append("purple")     # Add to end
print(f"After append: {colors}")

colors.insert(1, "orange")  # Insert at position
print(f"After insert at index 1: {colors}")

# Removing elements
colors.remove("yellow")     # Remove by value
print(f"After remove('yellow'): {colors}")

popped = colors.pop()       # Remove and return last
print(f"After pop(): {colors}, popped value: {popped}")

popped_index = colors.pop(1)  # Remove at index
print(f"After pop(1): {colors}, popped: {popped_index}")

# ========== LIST METHODS ==========
print("\n--- LIST METHODS ---")
nums = [3, 1, 4, 1, 5, 9, 2]
print(f"Original: {nums}")

nums.sort()                 # Sort ascending
print(f"After sort(): {nums}")

nums.reverse()              # Reverse order
print(f"After reverse(): {nums}")

print(f"Count of 1's: {nums.count(1)}")
print(f"Index of 5: {nums.index(5)}")

nums_copy = nums.copy()     # Create a copy
nums.clear()                # Empty the list
print(f"After clear(): {nums}")
print(f"Copy remains: {nums_copy}")

# ========== LIST OPERATIONS ==========
print("\n--- LIST OPERATIONS ---")
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(f"Concatenation: {list1} + {list2} = {combined}")

# Repetition
repeated = list1 * 3
print(f"Repetition: {list1} * 3 = {repeated}")

# Membership testing
print(f"Is 2 in list1? {2 in list1}")
print(f"Is 10 in list1? {10 in list1}")

# List length
print(f"Length of combined list: {len(combined)}")

# ========== LOOPING THROUGH LISTS ==========
print("\n--- LOOPING THROUGH LISTS ---")

# Basic for loop
print("Basic loop:")
for fruit in fruits:
    print(f"  {fruit}")

# Loop with index
print("\nLoop with index:")
for i in range(len(fruits)):
    print(f"  Index {i}: {fruits[i]}")

# enumerate() - get index and value
print("\nUsing enumerate():")
for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")

# ========== LIST COMPREHENSIONS ==========
print("\n--- LIST COMPREHENSIONS ---")

# Traditional way
squares = []
for x in range(5):
    squares.append(x ** 2)
print(f"Squares (traditional): {squares}")

# List comprehension
squares_comp = [x ** 2 for x in range(5)]
print(f"Squares (comprehension): {squares_comp}")

# With condition
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# ========== PRACTICE TASKS ==========
print("\n" + "=" * 50)
print("PRACTICE TASKS")
print("=" * 50)

print("\nTask 1: Create a list of 5 favorite movies.")
print("Then print the first, last, and middle movie.")

print("\nTask 2: List Operations")
print("Create a list of numbers. Find: sum, maximum, minimum, average.")

print("\nTask 3: Remove Duplicates")
print("Given [1, 2, 2, 3, 4, 4, 5], create a new list with unique elements.")

print("\nTask 4: Even Number Filter")
print("Create a list of numbers 1-20. Use list comprehension to get even numbers.")

print("\nTask 5: To-Do List Manager")
print("Create a program that allows user to:")
print("- Add tasks")
print("- Remove tasks")
print("- View all tasks")
print("- Exit")

print("\nTask 6: Matrix (2D List)")
print("Create a 3x3 matrix (list of lists) and print it nicely.")