from turtle import *

# Initialize the screen and set up the drawing window
s = Screen()
s.screensize(700, 1000)  # Set the screen size to 700x1000 pixels
speed(5)  # Set the drawing speed of the turtle

def my_goto(x, y):
    """
    Move the turtle to a specific coordinate (x, y) without drawing.
    """
    penup()  # Lift the pen to move without drawing
    goto(x, y)  # Move to the new position
    pendown()  # Lower the pen to start drawing

pensize(2)  # Set the pen width to 2 units

def short():
    """
    Draws the shorts of the character.
    """
    fillcolor('#ffec40')  # Set the fill color for the shorts
    begin_fill()  # Start filling the shape with the fill color
    right(25)
    forward(20)
    right(45)
    forward(20)
    left(70)
    forward(90)
    left(95)
    forward(75)
    left(85)
    forward(175)
    left(85)
    forward(75)
    left(95)
    forward(90)
    left(85)
    forward(18)
    end_fill()  # End filling the shape

def lleg():
    """
    Draws the left leg of the character.
    """
    my_goto(-39, -25)  # Move to the starting position for the left leg
    fillcolor("#ffd699")  # Set the fill color for the left leg
    begin_fill()
    right(89)
    forward(25)
    right(90)
    forward(50)
    right(90)
    forward(20)
    right(85)
    forward(50)
    end_fill()

def lsock():
    """
    Draws the left sock of the character.
    """
    my_goto(-36, -78)  # Move to the starting position for the left sock
    fillcolor("#ffffff")  # Set the fill color for the sock
    begin_fill()
    right(90)
    circle(80, 13)
    right(110)
    forward(22)
    right(85)
    forward(19)
    right(90)
    forward(21)
    end_fill()

def lshoe():
    """
    Draws the left shoe of the character.
    """
    my_goto(-69, -112)  # Move to the starting position for the left shoe
    fillcolor("#b5ae60")  # Set the fill color for the shoe
    begin_fill()
    right(90)
    left(5)
    forward(56)
    left(105)
    forward(13)
    left(75)
    forward(20)
    right(90)
    forward(15)
    circle(10, 15)
    left(80)
    forward(4)
    circle(10, 15)
    left(40)
    circle(20, 15)
    forward(10)
    right(45)
    forward(15)
    circle(25, 25)
    end_fill()

def rleg():
    """
    Draws the right leg of the character.
    """
    my_goto(60, -28)  # Move to the starting position for the right leg
    fillcolor("#ffd699")  # Set the fill color for the right leg
    begin_fill()
    left(128)
    forward(25)
    right(95)
    forward(55)
    right(90)
    forward(20)
    right(85)
    forward(55)
    end_fill()

def rsock():
    """
    Draws the right sock of the character.
    """
    my_goto(64, -79)  # Move to the starting position for the right sock
    fillcolor("#ffffff")  # Set the fill color for the sock
    begin_fill()
    right(90)
    circle(90, 14)
    right(110)
    forward(23)
    right(90)
    forward(15)
    right(80)
    forward(21)
    end_fill()

def rshoe():
    """
    Draws the right shoe of the character.
    """
    my_goto(64, -108)  # Move to the starting position for the right shoe
    fillcolor("#b5ae60")  # Set the fill color for the shoe
    begin_fill()
    right(100)
    forward(56)
    left(160)
    forward(25)
    right(68)
    forward(17)
    left(90)
    circle(18, 15)
    forward(5)
    left(75)
    forward(11)
    right(85)
    forward(20)
    left(45)
    circle(10, 30)
    left(25)
    forward(5)
    end_fill()

def shirt():
    """
    Draws the shirt of the character.
    """
    my_goto(-75, 48)  # Move to the starting position for the shirt
    fillcolor("red")  # Set the fill color for the shirt
    begin_fill()
    left(72)
    forward(185)
    left(87)
    forward(75)
    right(68)
    circle(20, 8)
    circle(300, 23)
    left(90)
    circle(35, 17)
    right(38)
    circle(35, 17)
    left(58)
    forward(75)
    right(12)
    forward(140)
    right(40)
    forward(93)
    left(120)
    circle(-20, 65)
    left(75)
    forward(10)
    left(23)
    forward(88)
    right(31)
    forward(87)
    right(180)
    forward(108)
    right(180)
    forward(104)
    circle(10, 70)
    end_fill()

def head():
    """
    Draws the head and face of the character.
    """
    my_goto(-20, 295)  # Move to the starting position for the head
    left(20)
    pensize(2)
    fillcolor('#fcc6a0')  # Set the fill color for the face
    begin_fill()
    right(90)
    forward(40)
    right(90)
    circle(50, 80)
    left(10)
    circle(50, 80)
    left(2)
    circle(200, 50)
    left(48)
    forward(60)
    circle(45, 60)
    right(5)
    circle(100, 85)
    end_fill()
    
    # Draw the hair or hat (if any)
    fillcolor('black')
    begin_fill()
    pensize(2)
    right(170)
    circle(-100, 165)
    right(78)
    forward(26)
    right(87)
    forward(55)
    circle(45, 60)
    right(5)
    circle(100, 85)
    end_fill()
    
    # Draw the neck and additional face details
    fillcolor('#fcc6a0')
    begin_fill()
    right(180)
    circle(-100, 105)
    right(37)
    forward(49)
    pensize(2)
    left(130)
    forward(30)
    right(50)
    forward(36)
    right(80)
    forward(50)
    pencolor('#fcc6a0')
    right(90)
    forward(30)
    end_fill()

def rhand():
    """
    Draws the right hand of the character.
    """
    my_goto(197, 209)  # Move to the starting position for the right hand
    pencolor('black')
    fillcolor('#fcc6a0')  # Set the fill color for the hand
    begin_fill()
    right(45)
    forward(6)
    left(55)
    forward(20)
    circle(-5, 70)
    right(100)
    forward(18)
    left(105)
    forward(18)
    circle(-5, 70)
    right(100)
    forward(18)
    left(145)
    forward(15)
    circle(-5, 70)
    right(100)
    forward(18)
    left(150)
    forward(13)
    circle(-5, 70)
    right(100)
    forward(15)
    left(150)
    forward(10)
    circle(-5, 70)
    right(100)
    forward(12)
    circle(60, 10)
    left(45)
    forward(6)
    right(90)
    forward(10)
    end_fill()

def lhand():
    """
    Draws the left hand of the character.
    """
    my_goto(-94, 242)  # Move to the starting position for the left hand
    fillcolor('#fcc6a0')  # Set the fill color for the hand
    begin_fill()
    right(10)
    forward(6)
    left(90)
    penup()
    forward(12)
    pendown()
    left(90)
    forward(8)
    left(90)
    forward(12)
    end_fill()

def chocochips():
    """
    Draws decorative elements (chocolate chips or buttons) on the shirt.
    """
    my_goto(-103, 291)  # Move to the starting position for the decorative elements
    right(90)
    fillcolor('#02d302')  # Set the fill color for the main decorative element
    begin_fill()
    right(90)
    forward(55)
    left(80)
    forward(12)
    left(10)
    forward(17)
    left(10)
    forward(12)
    left(80)
    forward(55)
    left(80)
    forward(12)
    left(10)
    forward(17)
    left(10)
    forward(12)
    left(80)
    left(80)
    forward(12)
    left(10)
    forward(17)
    left(10)
    forward(12)
    end_fill()
    
    # Draw small chocolate chips/buttons
    penup()
    right(100)
    forward(20)
    right(90)
    forward(14)
    pendown()
    pencolor('#9c5e4a')  # Set the color for small chocolate chips
    fillcolor('#9c5e4a')
    begin_fill()
    for i in range(5):
        forward(15)
        right(144)
    end_fill()
    
    # Position for next chip
    penup()
    forward(27)
    left(90)
    forward(16)
    left(90)
    forward(7)
    pendown()
    fillcolor('#9c5e4a')
    begin_fill()
    for i in range(5):
        forward(10)
        right(144)
    end_fill()
    
    # Position for next chip
    penup()
    forward(20)
    right(90)
    forward(5)
    pendown()
    fillcolor('#9c5e4a')
    begin_fill()
    for i in range(5):
        forward(10)
        right(144)
    end_fill()
    
    # Position for last chip
    penup()
    right(180)
    forward(6)
    pendown()
    fillcolor('#9c5e4a')
    begin_fill()
    for i in range(5):
        forward(10)
        right(144)
    end_fill()

def lhand2():
    """
    Adds additional detail to the left hand.
    """
    my_goto(-112, 284)  # Move to the starting position for additional hand detail
    pencolor('black')
    fillcolor('#fcc6a0')  # Set the fill color for the hand detail
    begin_fill()
    right(180)
    forward(31)
    left(90)
    for i in range(2): 
        circle(4, 90) 
    for i in range(3):
        right(180)
        for i in range(2): 
            circle(4, 90)
    end_fill()

def mouth():
    """
    Draws the mouth of the character.
    """
    my_goto(-25, 200)  # Move to the starting position for the mouth
    left(65)
    fillcolor('#77332e')  # Set the fill color for the mouth
    begin_fill()
    for i in range(2): 
        circle(25, 90) 
        circle(25 // 2, 90)
    end_fill()

def eyebrow(x, y):
    """
    Draws an eyebrow at the specified position (x, y).
    """
    my_goto(x, y)  # Move to the position for the eyebrow
    pensize(18)  # Set the pen width for the eyebrow
    right(150)
    forward(25)
    right(90)
    for i in range(1):
        right(45)
        dot(15)  # Draw a dot as part of the eyebrow
    left(55)
    forward(25)
    for i in range(1):
        right(45)
        dot(15)  # Draw another dot for the second part of the eyebrow

def eyelid(x, y):
    """
    Draws an eyelid at the specified position (x, y).
    """
    my_goto(x, y)  # Move to the position for the eyelid
    pensize(2)  # Set the pen width for the eyelid
    left(170)
    circle(-23, 180)  # Draw a semi-circle to represent the eyelid

def eyes1(x, y):
    """
    Draws the first eye at the specified position (x, y).
    """
    my_goto(x, y)  # Move to the position for the first eye
    right(90)
    fillcolor('#000000')  # Set the fill color for the eye
    begin_fill()
    circle(18)  # Draw the outer part of the eye
    end_fill()
    left(90)
    penup()
    forward(19)
    right(90)
    forward(7)
    pendown()
    fillcolor('#ffffff')  # Set the fill color for the eye's white part
    begin_fill()
    left(90)
    circle(9)  # Draw the white part of the eye
    end_fill()

def eyes2(x, y):
    """
    Draws the second eye at the specified position (x, y).
    """
    my_goto(x, y)  # Move to the position for the second eye
    right(90)
    fillcolor('#000000')  # Set the fill color for the eye
    begin_fill()
    circle(18)  # Draw the outer part of the eye
    end_fill()
    left(90)
    penup()
    forward(19)
    right(90)
    forward(8)
    pendown()
    fillcolor('#ffffff')  # Set the fill color for the eye's white part
    begin_fill()
    left(90)
    circle(9)  # Draw the white part of the eye
    end_fill()

def robo():
    """
    Draws a red robot or a similar shape.
    """
    my_goto(155, -105)  # Move to the starting position for the robot
    left(93)
    color('red')
    pensize(7)
    begin_fill()
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    end_fill()

    # Draw eyes or buttons for the robot
    color('white')
    penup()
    left(90)
    forward(30)
    right(90)
    forward(12)
    pendown()
    pensize(3)
    circle(5)  # Draw the first eye/button
    penup()
    forward(25)
    pendown()
    circle(5)  # Draw the second eye/button

    # Draw a rectangular part for the robot's body
    penup()
    right(90)
    forward(20)
    right(90)
    pendown()
    begin_fill()
    forward(23)
    right(90)
    forward(7)
    right(90)
    forward(23)
    right(90)
    forward(7)
    right(90)
    end_fill()

    # Draw a red circle for the robot's additional detail
    penup()
    forward(25)
    right(90)
    forward(35)
    pendown()
    color('red')
    forward(30)
    penup()
    right(90)
    pendown()
    begin_fill()
    circle(5)  # Draw a red circle
    end_fill()

def legs():
    """
    Draws both the legs of the character.
    """
    lleg()  # Draw the left leg and its parts
    lsock()  # Draw the left sock
    lshoe()  # Draw the left shoe
    rleg()  # Draw the right leg and its parts
    rsock()  # Draw the right sock
    rshoe()  # Draw the right shoe

def hands():
    """
    Draws both the hands of the character along with additional details.
    """
    rhand()  # Draw the right hand and its details
    lhand()  # Draw the left hand
    chocochips()  # Draw decorative elements on the shirt
    lhand2()  # Add additional detail to the left hand

def eyebrows():
    """
    Draws the eyebrows and eyelids of the character.
    """
    eyebrow(-8, 300)  # Draw the first eyebrow
    right(90)
    eyebrow(72, 300)  # Draw the second eyebrow
    eyelid(-9, 270)  # Draw the first eyelid
    left(15)
    eyelid(68, 265)  # Draw the second eyelid

def eyes():
    """
    Draws both eyes of the character.
    """
    eyes1(17, 275)  # Draw the first eye
    eyes2(95, 270)  # Draw the second eye

# The main function to draw the complete character
def main():
    """
    Draw the entire character by calling all the functions.
    """
    shirt()  # Draw the shirt
    head()  # Draw the head
    legs()  # Draw the legs
    hands()  # Draw the hands
    eyebrows()  # Draw the eyebrows and eyelids
    eyes()  # Draw the eyes
    robo()  # Draw the robot

if __name__ == "__main__":
    main()  # Execute the main function to draw the character
    done()  # Finish the drawing and display the result
