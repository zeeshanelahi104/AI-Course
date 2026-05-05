# DRAWING WITH TURTLE GRAPHICS

import turtle
import random

print("=" * 50)
print("TURTLE GRAPHICS")
print("=" * 50)
print("\nClose the turtle window to continue to next section...")

# ========== SETUP ==========
# Create screen and turtle
screen = turtle.Screen()
screen.title("Turtle Graphics Demo")
screen.bgcolor("lightblue")
screen.setup(800, 600)  # Width, height

t = turtle.Turtle()
t.speed(5)  # Speed: 1(slowest) to 10(fastest), 0(fastest)
t.pensize(2)

# ========== BASIC MOVEMENT ==========
def basic_movement():
    t.penup()
    t.goto(-300, 200)
    t.pendown()
    t.write("Basic Movement", font=("Arial", 16, "bold"))
    
    t.penup()
    t.goto(-300, 150)
    t.pendown()
    
    # Forward, Backward, Left, Right
    t.forward(100)      # Move forward 100 pixels
    t.left(90)          # Turn left 90 degrees
    t.forward(50)
    t.right(90)         # Turn right 90 degrees
    t.forward(50)
    t.backward(100)     # Move backward

# ========== DRAWING SHAPES ==========
def draw_square(size):
    """Draw a square"""
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_rectangle(width, height):
    """Draw a rectangle"""
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

def draw_triangle(size):
    """Draw an equilateral triangle"""
    for _ in range(3):
        t.forward(size)
        t.left(120)

def draw_circle(radius):
    """Draw a circle"""
    t.circle(radius)

def draw_star(size):
    """Draw a 5-point star"""
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 180 - 36 = 144

# ========== COLOR AND STYLE ==========
def color_demo():
    t.penup()
    t.goto(-300, -50)
    t.pendown()
    t.write("Colors & Styles", font=("Arial", 16, "bold"))
    
    t.penup()
    t.goto(-300, -100)
    t.pendown()
    
    # Change colors
    t.color("red")
    t.fillcolor("yellow")
    
    t.begin_fill()
    draw_square(60)
    t.end_fill()
    
    t.penup()
    t.goto(-200, -100)
    t.pendown()
    
    t.color("blue")
    t.pensize(4)
    draw_circle(30)
    
    t.penup()
    t.goto(-100, -100)
    t.pendown()
    
    t.color("green")
    t.pensize(2)
    t.dot(40)  # Draw a dot

# ========== PATTERNS ==========
def draw_spiral():
    """Draw a colorful spiral"""
    t.penup()
    t.goto(100, 200)
    t.pendown()
    t.write("Spiral", font=("Arial", 16, "bold"))
    
    t.penup()
    t.goto(100, 150)
    t.pendown()
    
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for i in range(50):
        t.color(colors[i % len(colors)])
        t.forward(i * 2)
        t.right(59)

def draw_colorful_circles():
    """Draw a pattern of circles"""
    t.penup()
    t.goto(-100, 150)
    t.pendown()
    t.write("Circle Pattern", font=("Arial", 16, "bold"))
    
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
    for i in range(36):
        t.color(colors[i % len(colors)])
        t.circle(50)
        t.right(10)

def draw_flower():
    """Draw a flower shape"""
    t.penup()
    t.goto(100, -50)
    t.pendown()
    t.write("Flower", font=("Arial", 16, "bold"))
    
    t.penup()
    t.goto(100, -100)
    t.pendown()
    
    t.color("red")
    t.pensize(2)
    for _ in range(36):
        t.circle(50)
        t.right(10)

# ========== DRAW WITH USER INPUT ==========
def draw_polygon(sides, length):
    """Draw any regular polygon"""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.right(angle)

# ========== RANDOM ART ==========
def random_art():
    """Create random colorful art"""
    t.penup()
    t.goto(-300, -250)
    t.pendown()
    t.write("Random Art", font=("Arial", 16, "bold"))
    
    t.penup()
    t.goto(-300, -300)
    t.pendown()
    
    t.speed(10)
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    
    for _ in range(100):
        t.color(random.choice(colors))
        size = random.randint(10, 50)
        angle = random.randint(0, 360)
        x = random.randint(-350, 350)
        y = random.randint(-250, 250)
        
        t.penup()
        t.goto(x, y)
        t.pendown()
        
        shape = random.choice(["square", "circle", "triangle"])
        if shape == "square":
            for _ in range(4):
                t.forward(size)
                t.right(90)
        elif shape == "circle":
            t.circle(size // 2)
        else:
            for _ in range(3):
                t.forward(size)
                t.left(120)

# ========== RUN DEMOS ==========
def run_all_demos():
    # Comment/uncomment to run specific demos
    
    # Basic shapes
    t.clear()
    t.penup()
    t.goto(-300, 250)
    t.pendown()
    t.write("Shapes Demo", font=("Arial", 20, "bold"))
    
    t.penup()
    t.goto(-300, 200)
    t.pendown()
    draw_square(80)
    
    t.penup()
    t.goto(-150, 200)
    t.pendown()
    draw_rectangle(100, 60)
    
    t.penup()
    t.goto(0, 200)
    t.pendown()
    draw_triangle(80)
    
    t.penup()
    t.goto(150, 200)
    t.pendown()
    draw_circle(40)
    
    t.penup()
    t.goto(250, 200)
    t.pendown()
    draw_star(60)
    
    # Wait for click to continue
    screen.exitonclick()

# ========== PRACTICE PROJECTS ==========
print("\n" + "=" * 50)
print("PRACTICE PROJECTS")
print("=" * 50)

print("\nProject 1: Draw a House")
print("Draw a square for the base, triangle for roof, rectangle for door.")

print("\nProject 2: Draw a Smiley Face")
print("Draw a yellow circle, two eyes, and a smile arc.")

print("\nProject 3: Draw a Rainbow")
print("Draw multiple semi-circles in rainbow colors (ROYGBIV).")

print("\nProject 4: Draw a Snowflake")
print("Draw a symmetrical pattern using loops and rotations.")

print("\nProject 5: Spiral of Squares")
print("Draw squares that rotate and grow larger.")

print("\nProject 6: Draw Your Initials")
print("Use turtle movements to draw the first letter of your name.")

print("\nProject 7: Racing Turtles")
print("Create multiple turtles racing to the finish line.")

# Uncomment to run the demo
# run_all_demos()
# random_art()

# Keep window open
# screen.mainloop()