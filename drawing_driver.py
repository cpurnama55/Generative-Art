from acquire_frequency import acquire_frequency
import pyaudio
import numpy as np
import turtle as tt
from PIL import Image
from uuid import uuid4
import os

########### Frequency Analyzer Initialization ###########
# constants
# 11025 samples min offset 2HZ max offset 5 HZ
# 22050 samples min offset 1HZ max offset 2 HZ
# 11025 takes 250 ms per sample while 22050 takes 500 ms per sample

# Setting chunk sample size higher produces a more accurate frequency determination however it increases processing time
# I think a good middle ground is using 11025 sample size, using 22050 doubles time from 250 ms to 500 ms

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
# tt.Screen().setup(width = 1.0, height = 1.0)
tt.Screen().setup(width = 0.5, height = 0.5)

# Set up global variables to be used in drawing so that they are easily modifiable
size = 0.5          # Initial size of side that the turtle creates for shape
angle = 91          # Angle at which the turtle turns. Changing this value greatly changes what shapes the turtle creates
speed = 0           # Speed at which the turtle draws. 0: Fastest, 10: fast, normal: 6, slow: 3, slowest: 1
delay = 0           # Delay between canvas updates in ms. Lower value correlates to faster canvas updates
side_step = 0       # Value in which size will increase at. A smaller size_step creates a tighter spiral and vice versa. The initialization of this value does not matter
marker = 0          # Value that holds what the last frequency range we were in was. Helps indicate when the shape parameters should change or be held constant

# Set up frequency ranges for different shapes to draw depending on frequency
range_one = range(0, 100)
range_two = range(101,200)
range_three = range(201, 300)
range_four = range(301, 400)
range_five = range(401, 500)
range_six = range(501, 600)
range_seven = range(601, 700)
range_eight = range(701, 800)
range_nine = range(801, 900)
range_ten = range(901-1000)
range_eleven = range(1001, 1100)
range_tweleve = range(1101, 1200)
range_thirteen = range(1201, 1300)
range_fourteen = range(1301, 100000)

# Consider adding some holder/flag variable that indicates what the previous frequency range was? This could prove useful if you want
# to reset the size of the shape being created, because size can get big pretty fast. 
# IE if we remain in the same frequency range, continue incrementing size. Else reset it back to 1 or whatever
# Hide the turtle cursor
# tt.hideturtle()
# Make the turtle draw at the fastest speed
tt.speed(speed)
# Adjust time interval between canvas updates. 0 makes the turtle draw super fast
tt.delay(delay)

def update_shape(size_input, speed_input, side_step_input, angle_input):
    # Update the following global parameters to adjust the shape the turtle is drawing
    # This is a quick helper function we'll use to assign different shape drawings to different frequency ranges
    global size, speed, side_step, angle
    size, speed, side_step, angle = size_input, speed_input, side_step_input, angle_input

# Define functions that will be executed on a keypress
def start_drawing():
    # Main function that commands the turtle to actually draw
    # After this function is called the turtle will continue to draw unless the pause_drawing function is called
    global speed, delay, size, angle, side_step, marker
    global range_one, range_two, range_three, range_four, range_five, range_six, range_seven, range_eight, range_nine, range_ten, range_eleven, range_tweleve, range_thirteen 
    tt.speed(speed)
    tt.delay(delay)
    tt.pendown()
    while True:
        freq = acquire_frequency(stream = stream, xf_array = xf, CHUNK = CHUNK, RATE = RATE) 
        if freq in range_one:
            if marker != 1:
                update_shape(size_input = 10, speed_input = 4, side_step_input = 4, angle_input = 480)
                marker = 1
        elif freq in range_two:
            if marker != 2:
                update_shape(size_input = 20, speed_input = 4, side_step_input = 2.5, angle_input = 90)
                marker = 2
        elif freq in range_three:  
            if marker != 3:
                update_shape(size_input = 30, speed_input = 4, side_step_input = 1, angle_input = 60)
                marker = 3
        elif freq in range_four:
            if marker != 4:
                update_shape(size_input = 40, speed_input = 6, side_step_input = 0.8, angle_input = 56)
                marker = 4
        elif freq in range_five:
            if marker != 5:
                update_shape(size_input = 50, speed_input = 8, side_step_input = 0.4, angle_input = 63)
                marker = 5
        elif freq in range_six:
            if marker != 6:
                update_shape(size_input = 60, speed_input = 10, side_step_input = 0.6, angle_input = 91)
                marker = 6
        elif freq in range_seven:
            if marker != 7:
                update_shape(size_input = 70, speed_input = 0, side_step_input = 0.3, angle_input = 75)
                marker = 7
        elif freq in range_eight:
            if marker != 8:
                update_shape(size_input = 80, speed_input = 0, side_step_input = 0.2, angle_input = 85)
                marker = 8
        elif freq in range_nine:
            if marker != 9:
                update_shape(size_input = 90, speed_input = 0, side_step_input = 0.3, angle_input = 96)
                marker = 9
        elif freq in range_ten:
            if marker != 10:
                update_shape(size_input = 100, speed_input = 0, side_step_input = 0.4, angle_input = 106)
                marker = 10
        elif freq in range_eleven:
            if marker != 11:
                update_shape(size_input = 110, speed_input = 0, side_step_input = 0.4, angle_input = 121)
                marker = 11
        elif freq in range_tweleve:
            if marker != 12:
                update_shape(size_input = 120, speed_input = 0, side_step_input = 0.3, angle_input = 300)
                marker = 12
        elif freq in range_thirteen:
            if marker != 13:
                update_shape(size_input = 130, speed_input = 0, side_step_input = 0.5, angle_input = 131)
                marker = 13
        elif freq in range_fourteen:
            if marker != 14:
                update_shape(size_input = 140, speed_input = 10, side_step_input = 2, angle_input = 200)
                marker = 14
        tt.forward(size)
        tt.right(angle)
        # print(side_step)
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