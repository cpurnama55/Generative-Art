import turtle as tt
from PIL import Image
from uuid import uuid4
import os

##### To draw a spirograph #####
# # Set the background color as black,
# # pensize as 2 and speed of drawing
# # curve as 10(relative)
# tt.bgcolor('black')
# tt.pensize(2)
# tt.speed(0)
# tt.delay(0)
# # Hide the cursor(or turtle) which drew the circle
# tt.hideturtle()
 
# # Iterate six times in total
# for i in range(6):
   
#       # Choose your color combination
#     for color in ('red', 'magenta', 'blue',
#                   'cyan', 'green', 'white',
#                   'yellow'):
#         tt.color(color)
         
#         # Draw a circle of chosen size, 100 here
#         tt.circle(100)
         
#         # Move 10 pixels left to draw another circle
#         tt.left(10)
     
# # After done creating the image, create a UUID for the file name
# uuid = str(uuid.uuid4()) 
# # Create the filepath (to specify we want pictures stored in pictures folder in current directory)
# filepath = 'pictures/' + uuid 
# # Save the current image on the screen to a postscript file
# tt.getscreen().getcanvas().postscript(file = filepath + '.ps')
# # Open the post script file and convert to png
# psimage=Image.open(filepath + '.ps')
# psimage.save(filepath + '.png')
# # Remove the old post script file
# try:
#   os.remove(filepath + '.ps')
# except:
#   print("Cannot remove  specified file:", filepath + '.ps')
# tt.done()
################################




###### To draw a star #####
# tt.color('red', 'yellow')
# tt.begin_fill()
# tt.speed(0)
# # delay(20)
# while True:
#     tt.forward(200)
#     tt.left(170)
#     if abs(tt.pos()) < 1:
#         break
# tt.end_fill()
# tt.done()
###########################
 
##### Spiral from squares #####
# Maximize the screen size of the canvas
tt.Screen().setup(width = 1.0, height = 1.0)
# Initial size of side that the turtle creates for shape
size = 1            # Initial size of side that the turtle creates for shape
size_init = size    # Store initial value of size
side_step = 2       # Value in which size will increase at. A smaller size_step creates a tighter spiral and vice versa. The initialization of this value does not matter
angle = 200         # Angle at which the turtle turns. Changing this value greatly changes what shapes the turtle creates 
speed = 10           # Speed at which the turtle draws. 0: Fastest, 10: fast, normal: 6, slow: 3, slowest: 1
delay = 0           # Delay between canvas updates in ms. Lower value correlates to faster canvas updates
# Hide the turtle cursor
tt.hideturtle()
# Make the turtle draw at the fastest speed
tt.speed(speed)
# Adjust time interval between canvas updates. 0 makes the turtle draw super fast
tt.delay(speed)
tt.color('hot pink') 

def start_drawing():
    global speed
    global delay
    global size 
    global angle
    global side_step
    tt.speed(speed)
    tt.delay(delay)
    tt.pendown()
    while True:
        # Call the global instances of size and angle and modify those
        tt.forward(size)
        tt.right(angle)
        size = size + side_step
def pause_drawing():
    tt.done()
def reset_drawing():
    global size
    global angle
    global speed
    global delay
    size = 0.5
    angle = 91
    tt.reset()
    tt.home()
    tt.speed(speed)
    tt.delay(delay)
def save_drawing():
  # After done creating the image, create a UUID for the file name
    # uuid = str(uuid4()) 
    uuid = 'size' + str(size_init) + '_sidestep' + str(side_step) + '_angle' + str(angle) + '_speed' + str(speed) + '_delay' + str(delay)
    # Create the filepath (to specify we want pictures stored in pictures folder in current directory)
    filepath = 'pictures/' + uuid 
    # Save the current image on the screen to a postscript file
    tt.getscreen().getcanvas().postscript(file = filepath + '.ps')
    # Open the post script file and convert to png
    psimage=Image.open(filepath + '.ps')
    psimage.save(filepath + '.png')
    tt.write('Image saved', font = ('Arial', 16, 'normal'))
    tt.done()

tt.onkeypress(start_drawing, 'space')
tt.onkeypress(pause_drawing, 'p')
tt.onkeypress(reset_drawing, 'r')
tt.onkeypress(save_drawing, 's')
# Call listen to set focus on the turtle window. This allows the window to 'listen' for keystroke inputs
tt.listen()
# Need mainloop command to be able to interact with turtle
tt.mainloop()