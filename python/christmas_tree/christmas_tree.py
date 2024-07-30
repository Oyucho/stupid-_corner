from turtle import *
from PIL import Image, ImageDraw, ImageFont
import os

# Screen setup
s = Screen()
s.screensize(700, 1000)
s.bgcolor("lightblue")

# Initialize turtle
t = Turtle()
t.speed(5)
t.hideturtle()

# Function to move turtle to a specific position
def my_goto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Draw the Christmas tree
def draw_tree():
    # Tree trunk
    my_goto(0, -150)
    t.color("brown")
    t.begin_fill()
    t.forward(20)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.end_fill()

    # Tree layers
    t.color("green")
    my_goto(-50, -90)
    t.begin_fill()
    t.right(90)
    t.forward(120)
    t.left(120)
    t.forward(70)
    t.left(120)
    t.forward(70)
    t.left(120)
    t.forward(120)
    t.end_fill()

    my_goto(-40, -30)
    t.begin_fill()
    t.forward(100)
    t.left(120)
    t.forward(60)
    t.left(120)
    t.forward(60)
    t.left(120)
    t.forward(100)
    t.end_fill()

    my_goto(-30, 20)
    t.begin_fill()
    t.forward(80)
    t.left(120)
    t.forward(50)
    t.left(120)
    t.forward(50)
    t.left(120)
    t.forward(80)
    t.end_fill()

# Draw decorations
def draw_decorations():
    # Ornaments
    t.color("red")
    my_goto(-20, 40)
    t.dot(20)
    my_goto(10, 10)
    t.dot(20)
    my_goto(-30, -20)
    t.dot(20)
    my_goto(20, -50)
    t.dot(20)

    # Star on top
    t.color("yellow")
    my_goto(-10, 90)
    t.begin_fill()
    t.left(72)
    for _ in range(5):
        t.forward(20)
        t.right(144)
    t.end_fill()

# Draw the tree
draw_tree()
draw_decorations()

# Save turtle screen to an image
file_name = "christmas_tree.png"
ts = t.getscreen()
ts.getcanvas().postscript(file=file_name)

# Load the image and add text using Pillow
image = Image.open(file_name)
draw = ImageDraw.Draw(image)

# Load Montserrat font (replace with your actual path if needed)
font_path = "Montserrat-Regular.ttf"  # Adjust path as needed

font_size = 40

# Print the font path for verification (optional)
print(f"Using font path: {font_path}")

try:
  font = ImageFont.truetype(font_path, font_size)
except OSError as e:
  print(f"Error loading font: {e}")
  # Use a default font (e.g., Arial)
  font = ImageFont.load_default()
  font_size = 20  # Adjust size if needed

# Define text and color
text = "Merry Christmas from Zone01 Kisumu"
text_color = "#0033cc"  # --blue-201

# Calculate text size
text_width = draw.textlength(text, font=font)
text_bbox = draw.textbbox(text, font=font)
text_height = text_bbox[3] - text_bbox[1]

# Calculate text position
image_width, image_height = image.size
text_x = (image_width - text_width) / 2
text_y = image_height - text_height - 50

# Draw text on image
draw.text((text_x, text_y), text, font=font, fill=text_color)

# Save the final image
final_file_name = "christmas_tree_with_text.png"
image.save(final_file_name)

# Clean up
os.remove(file_name)
print(f"Image saved as {final_file_name}")

# Done
done()


