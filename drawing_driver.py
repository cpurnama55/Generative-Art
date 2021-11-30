from acquire_frequency import acquire_frequency
import pyaudio
import numpy as np
import turtle as tt
from PIL import Image
from uuid import uuid4

########### Frequency Analyzer Initialization ###########
# constants
# 11025 samples min offset 2HZ max offset 5 HZ
# 22050 samples min offset 1HZ max offset 2 HZ
# 11025 takes 250 ms per sample while 22050 takes 500 ms per sample
# Setting chunk sample size higher produces a more accurate frequency determination however it increases processing time
# I think a good middle ground is using 11025 sample size, using 22050 doubles time from 250 ms to 500 ms
# 1024 runs the drawing program at a sufficiently fast speed, though it's not the most accurate in the world

CHUNK = 1024 * 2             # Samples per frame
FORMAT = pyaudio.paInt16     # audio format of data
CHANNELS = 1                 # single channel for microphone
RATE = 44100                 # samples per second

# Pyaudio class instance to actually interface with sound input
p = pyaudio.PyAudio()

# Stream object to get data from microphone
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

# Array of frequencies
# Instead of using the full spectrum, there are CHUNK evenly spaced out frequencies to choose from
xf = np.linspace(0, RATE, CHUNK)     # frequencies (spectrum)
holder = 0
carrier = np.array([])

########### Spiral from squares ###########
# Maximize the screen size of the canvas
tt.Screen().setup(width = 1.0, height = 1.0)

# Set up global variables to be used in drawing so that they are easily modifiable
size = 0.5          # Initial size of side that the turtle creates for shape
angle = 91          # Angle at which the turtle turns. Changing this value greatly changes what shapes the turtle creates
speed = 0           # Speed at which the turtle draws. 0: Fastest, 10: fast, normal: 6, slow: 3, slowest: 1
delay = 0           # Delay between canvas updates in ms. Lower value correlates to faster canvas updates
side_step = 0       # Value in which size will increase at. A smaller size_step creates a tighter spiral and vice versa. The initialization of this value does not matter
marker = 0          # Value that holds what the last frequency range we were in was. Helps indicate when the shape parameters should change or be held constant

# Set up frequency ranges for different shapes to draw depending on frequency
range_one = range(101,200)
range_two = range(201, 300)
range_three = range(301, 400)
range_four = range(401, 500)
range_five = range(501, 600)
range_six = range(601, 700)
range_seven = range(701, 800)
range_eight = range(801, 900)
range_nine = range(901-1000)
range_ten = range(1001, 1100)
range_eleven = range(1101, 1200)
range_twelve = range(1201, 1300)
range_thirteen = range(1301, 1330)
range_fourteen = range(1331, 1500)
range_fifteen = range(1501, 1800)
range_sixteen = range(1801, 20000)

# Acquire the boundaries of the canvas that we'll use to make sure the turtle doesn't go off screen
left_bound = -(tt.screensize()[0] + 70)
right_bound = tt.screensize()[0] + 70
top_bound = tt.screensize()[1] + 30
bottom_bound = -(tt.screensize()[1] + 30)

# Hide the turtle cursor
tt.hideturtle()
# Make the turtle draw at the fastest speed
tt.speed(speed)
# Adjust time interval between canvas updates. 0 makes the turtle draw super fast
tt.delay(delay)

# Optionally we can set the background color to black. I like it more than white but that's just personal preference
# tt.bgcolor('black')

def update_shape(size_input, speed_input, side_step_input, angle_input):
    # Update the following global parameters to adjust the shape the turtle is drawing
    # This is a quick helper function we'll use to assign different shape drawings to different frequency ranges
    global size, speed, side_step, angle
    size, speed, side_step, angle = size_input, speed_input, side_step_input, angle_input

# Define functions that will be executed on a keypress
def start_drawing():
    # Main function that commands the turtle to actually draw
    # After this function is called the turtle will continue to draw unless the pause_drawing function is called

    # Initialize global variables
    global speed, delay, size, angle, side_step, marker
    global range_one, range_two, range_three, range_four, range_five, range_six, range_seven, range_eight, range_nine, range_ten, range_eleven, range_tweleve, range_thirteen 
    global left_bound, right_bound, top_bound, bottom_bound
    
    holder = 0      # Holder variable to makes frequency reading is not over 20000 Hz
    tt.delay(delay) # Set delay to global value
    tt.pendown()       
    while True:
        # Acquire frequency
        freq = acquire_frequency(stream = stream, xf_array = xf, CHUNK = CHUNK, RATE = RATE) 

        # Check if frequency is over 20000 Hz. This is usually an indication of a bad reading, so we'll jsut
        # set the frequency to be whatever the previous non-bad reading was
        if freq > 20000:
            freq = holder
        else:
            holder = freq

        # Check what range our acquired frequency is in
        # Adjust the shape it draws accordingly as well as the line color
        # Marker variable is used in the case that if we are in the same range as a previous iteration, 
        # we don't want to reset the size of object being drawn
        if freq in range_one:
            if marker != 1:
                update_shape(size_input = 20, speed_input = 0, side_step_input = 4, angle_input = 480)
                marker = 1
                tt.pencolor('red')    
        elif freq in range_two:
            if marker != 2:
                update_shape(size_input = 20, speed_input = 0, side_step_input = 2.5, angle_input = 90)
                marker = 2
                tt.pencolor('orange')            
        elif freq in range_three:  
            if marker != 3:
                update_shape(size_input = 30, speed_input = 0, side_step_input = 1, angle_input = 60)
                marker = 3
                tt.pencolor('yellow')
        elif freq in range_four:
            if marker != 4:
                update_shape(size_input = 40, speed_input = 0, side_step_input = 0.8, angle_input = 56)
                marker = 4
                tt.pencolor('lime')
        elif freq in range_five:
            if marker != 5:
                update_shape(size_input = 40, speed_input = 0, side_step_input = 0.4, angle_input = 63)
                marker = 5
                tt.pencolor('green')
        elif freq in range_six:
            if marker != 6:
                update_shape(size_input = 60, speed_input = 0, side_step_input = 0.6, angle_input = 91)
                marker = 6
                tt.pencolor('cyan')
        elif freq in range_seven:
            if marker != 7:
                update_shape(size_input = 60, speed_input = 0, side_step_input = 0.3, angle_input = 75)
                marker = 7
                tt.pencolor('light blue')
        elif freq in range_eight:
            if marker != 8:
                update_shape(size_input = 60, speed_input = 0, side_step_input = 0.2, angle_input = 85)
                marker = 8
                tt.pencolor('teal')
        elif freq in range_nine:
            if marker != 9:
                update_shape(size_input = 60, speed_input = 0, side_step_input = 0.3, angle_input = 96)
                marker = 9
                tt.pencolor('blue')
        elif freq in range_ten:
            if marker != 10:
                update_shape(size_input = 70, speed_input = 0, side_step_input = 0.4, angle_input = 106)
                marker = 10
                tt.pencolor('purple')
        elif freq in range_eleven:
            if marker != 11:
                update_shape(size_input = 70, speed_input = 0, side_step_input = 0.4, angle_input = 121)
                marker = 11
                tt.color('magenta')
        elif freq in range_twelve:
            if marker != 12:
                update_shape(size_input = 80, speed_input = 0, side_step_input = 2, angle_input = 200) #Swapped
                marker = 12
                tt.color('hot pink')
        elif freq in range_thirteen:
            if marker != 13:
                update_shape(size_input = 80, speed_input = 0, side_step_input = 0.5, angle_input = 131)
                marker = 13
                tt.color('deep pink')
        elif freq in range_fourteen:
            if marker != 14:
                update_shape(size_input = 80, speed_input = 0, side_step_input = 0.3, angle_input = 300) #Swapped
                marker = 14
                tt.color('indigo')
        elif freq in range_fifteen:
            if marker != 15:
                update_shape(size_input = 90, speed_input = 0, side_step_input = 0.6, angle_input = 91)
                marker = 15
                tt.color('maroon')
        elif freq in range_sixteen:
            if marker != 16:
                update_shape(size_input = 100, speed_input = 0, side_step_input = 2, angle_input = 200)
                marker = 16
                # tt.pencolor('white')        # Use this pen color if using black background
                tt.pencolor('black')        # Use this pen color if using white background

        # Actually draw the line
        tt.forward(size)
        tt.right(angle)

        # Check to see if the turtle ended out of bounds. If it is, reset is back to the center
        xcord = tt.xcor()
        ycord = tt.ycor()
        if xcord > right_bound or xcord < left_bound:
            tt.goto(0, 0)
        if ycord > top_bound or ycord < bottom_bound:
            tt.goto(0,0)
        
        # Increment step size
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
    uuid = str(uuid4()) 
    # Create the filepath (to specify we want pictures stored in pictures folder in current directory)
    filepath = 'pictures/' + uuid 
    # Save the current image on the screen to a postscript file
    tt.getscreen().getcanvas().postscript(file = filepath + '.ps')
    # Open the post script file and convert to png
    psimage=Image.open(filepath + '.ps')
    psimage.save(filepath + '.png')
    tt.write('Image saved', font = ('Arial', 16, 'normal'))
    tt.done()

# Map the functions to keyboard keys
tt.onkeypress(start_drawing, 'space')
tt.onkeypress(pause_drawing, 'p')
tt.onkeypress(reset_drawing, 'r')
tt.onkeypress(save_drawing, 's')

# Call listen to set focus on the turtle window. This allows the window to 'listen' for keystroke inputs
tt.listen()
# Need mainloop command to be able to interact with turtle
tt.mainloop()

########### LEFTOVER CODE ###########

## Acquire average of 10 samples ##
# Acquire the average frequency from 10 samples
# while True:
#     freq = acquire_frequency(stream = stream, xf_array = xf, CHUNK = CHUNK, RATE = RATE )
#     if freq > 20000:
#         continue
#     carrier = np.append(carrier, freq)
#     # print('Frequency:', freq, 'Hz')
#     if carrier.size >= 20:
#         # print(carrier)
#         print('Average frequency:', int(np.average(carrier)))
#         carrier = []
#     else:
#         pass
#####################################

# Just read sound input and determine sound frequency as fast as possible ##
# while True:
#     freq = acquire_frequency(stream = stream, xf_array = xf, CHUNK = CHUNK, RATE = RATE ) 
#     if freq > 20000:
#         print('Max Frequency:', holder, 'Hz')
#         pass
#     else: 
#         holder = freq
#         print('Max Frequency:', freq, 'Hz')
#############################################################################