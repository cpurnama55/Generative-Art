# Turtle is included in Python3 standard library! No need to install
import turtle                   
# For turtle documentation, visit the following link:
# https://docs.python.org/3/library/turtle.html#turtle.mainloop


# Set up the turtle environment 
turtle.setup(0.75, 0.75)            # Create a screen that occupies 75% in width and height                     
turtle.title("Turtle Keys")         # String to display in title bar of window
cursor = turtle.Turtle()            # Assign turtle class to a variable

# Variables that specify turtle's rotational angle and movement speed
rot_angle = 5                   
movement_speed = 10             

# Create functions that activate on a key press. We will map these functions to a key later
def move_forward():
    cursor.forward(movement_speed)

def rotate_left():
    cursor.left(rot_angle)

def rotate_right():
    cursor.right(rot_angle)

def move_backward():
    cursor.back(movement_speed)

def reset_canvas():
    cursor.reset()

# Map the previously created functions to a key specified by a string. 
# onkeypress makes the function happen when you press and while you hold the key
# onkey makes the function happen when you press the key, and it only occurs once even if you hold the key
# onkeyrelease makes the function happen when you release the key
turtle.onkeypress(move_forward, "Up")
turtle.onkeypress(rotate_left, "Left")
turtle.onkeypress(rotate_right, "Right")
turtle.onkeypress(move_backward, "Down")
turtle.onkeypress(reset_canvas, "r")

# Call listen to set focus on the turtle window. This allows the window to 'listen' for keystroke inputs
turtle.listen()

# Start the actual turtle up! Should be called last in script. 
# You only need to use this function if you want to interact with the turtle 
turtle.mainloop()