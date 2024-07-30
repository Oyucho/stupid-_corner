import turtle
import random

# Game configuration constants
WIDTH = 500  # Width of the game screen
HEIGHT = 500  # Height of the game screen
FOOD_SIZE = 10  # Size of the food
DELAY = 100  # Delay between each snake movement in milliseconds

# Dictionary to define movement offsets for each direction
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def reset():
    """Resets the game state, initializes snake, direction, and food position."""
    global snake, snake_direction, food_pos, pen
    snake = [[0, 0], [0, 20], [0, 40], [0, 50], [0, 60]]  # Initial snake body
    snake_direction = "up"  # Initial direction
    food_pos = get_random_food_pos()  # Random food position
    food.goto(food_pos)  # Place food at the new position
    move_snake()  # Start moving the snake

def move_snake():
    """Moves the snake based on the current direction and handles collisions."""
    global snake_direction

    # Determine the new head position of the snake
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_direction][0]
    new_head[1] = snake[-1][1] + offsets[snake_direction][1]

    # Check for self-collision
    if new_head in snake[:-1]:
        reset()  # Restart the game if the snake collides with itself
    else:
        snake.append(new_head)  # Add new head to the snake

        # Check if the snake has eaten food; otherwise, remove the tail segment
        if not food_collision():
            snake.pop(0)  # Remove the tail segment if no food is eaten

        # Implement screen wrapping logic
        if snake[-1][0] > WIDTH / 2:
            snake[-1][0] -= WIDTH
        elif snake[-1][0] < -WIDTH / 2:
            snake[-1][0] += WIDTH
        elif snake[-1][1] > HEIGHT / 2:
            snake[-1][1] -= HEIGHT
        elif snake[-1][1] < -HEIGHT / 2:
            snake[-1][1] += HEIGHT

        pen.clearstamps()  # Clear previous snake stamps

        # Draw the snake at the new positions
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        screen.update()  # Refresh the screen

        # Continue the game loop with a delay
        turtle.ontimer(move_snake, DELAY)

def food_collision():
    """Checks if the snake has collided with the food."""
    global food_pos
    if get_distance(snake[-1], food_pos) < 20:  # Check if snake head is close enough to food
        food_pos = get_random_food_pos()  # Generate a new food position
        food.goto(food_pos)  # Move food to the new position
        return True  # Indicate that the food was eaten
    return False

def get_random_food_pos():
    """Generates a random position for the food within the screen bounds."""
    x = random.randint(-WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(-HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)

def get_distance(pos1, pos2):
    """Calculates the Euclidean distance between two points."""
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

# Direction control functions
def go_up():
    """Changes the snake's direction to up, if not currently down."""
    global snake_direction
    if snake_direction != "down":  # Prevents reversing direction
        snake_direction = "up"

def go_right():
    """Changes the snake's direction to right, if not currently left."""
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_down():
    """Changes the snake's direction to down, if not currently up."""
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    """Changes the snake's direction to left, if not currently right."""
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

# Screen setup
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set screen size
screen.title("Snake Game")  # Set window title
screen.bgcolor("black")  # Set background color
screen.tracer(0)  # Disable automatic screen updates for smoother animation

# Pen setup for drawing the snake
pen = turtle.Turtle("square")
pen.penup()
pen.pencolor("yellow")

# Food setup
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)  # Adjust size based on FOOD_SIZE
food.penup()

# Event handlers for controlling the snake
screen.listen()
screen.onkey(go_up, "Up")  # Up arrow key for moving up
screen.onkey(go_right, "Right")  # Right arrow key for moving right
screen.onkey(go_down, "Down")  # Down arrow key for moving down
screen.onkey(go_left, "Left")  # Left arrow key for moving left

# Start the game
reset()  # Initialize the game state
turtle.done()  # Keep the window open
