import turtle as tt
from PIL import Image

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
     
# # tt.done()    # Stop window from closing
# tt.getscreen().getcanvas().postscript(file='turtle_image.ps')
# tt.done()
# ### Need ghostscript to do this. At the time of writing this code github is down so idk lol
# # psimage=Image.open('turtle_image.ps')
# # psimage.save('turtle_image.png')
# # tt.done()

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
size = 0.5
# Angle at which the turtle turns. Changing this value greatly changes what shapes the turtle creates
angle = 91
# Hide the turtle cursor
# tt.hideturtle()
# Make the turtle draw at the fastest speed
tt.speed(0)
# Adjust time interval between canvas updates. 0 makes the turtle draw super fast
tt.delay(0)

def start_drawing():
    tt.speed(0)
    tt.delay(0)
    tt.pendown()
    while True:
        # Call the global instances of size and angle and modify those
        global size
        global angle
        tt.forward(size)
        tt.right(angle)
        size = size + 0.5
def pause_drawing():
    tt.done()
def reset_drawing():
    global size
    global angle
    size = 0.5
    angle = 91
    tt.reset()
    tt.home()
    tt.speed(0)
    tt.delay(0)
def save_drawing():
    tt.getscreen().getcanvas().postscript(file='turtle_image.ps')
    tt.write('Image saved', font = ('Arial', 16, 'normal'))

tt.onkeypress(start_drawing, 'space')
tt.onkeypress(pause_drawing, 'p')
tt.onkeypress(reset_drawing, 'r')
tt.onkeypress(save_drawing, 's')
# Call listen to set focus on the turtle window. This allows the window to 'listen' for keystroke inputs
tt.listen()
# Need mainloop command to be able to interact with turtle
tt.mainloop()