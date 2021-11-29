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
# CHUNK = 11025                # samples per frame
CHUNK = 1024 * 2
FORMAT = pyaudio.paInt16     # audio format of data
CHANNELS = 1                 # single channel for microphone
RATE = 44100                 # samples per second

# Pyaudio class instance to actually interface with sound input
p = pyaudio.PyAudio()

# stream object to get data from microphone
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

# Consider adding some holder/flag variable that indicates what the previous frequency range was? This could prove useful if you want
# to reset the size of the shape being created, because size can get big pretty fast. 
# IE if we remain in the same frequency range, continue incrementing size. Else reset it back to 1 or whatever


# Hide the turtle cursor
# tt.hideturtle()
# Make the turtle draw at the fastest speed
tt.speed(speed)
# Adjust time interval between canvas updates. 0 makes the turtle draw super fast
tt.delay(delay)

# Define functions that will be executed on a keypress
def start_drawing():
    # Main function that commands the turtle to actually draw
    # After this function is called the turtle will continue to draw unless the pause_drawing function is called
    global speed
    global delay
    global size
    global angle
    global side_step
    tt.speed(speed)
    tt.delay(delay)
    tt.pendown()
    while True:
        freq = acquire_frequency(stream = stream, xf_array = xf, CHUNK = CHUNK, RATE = RATE) 

        # My (Caelan voice range)
        if freq in range(100, 400):
            speed = 0
            side_step = 0.8
            angle = 56
        # Little higher range
        elif freq in range(401, 800):
            speed = 0
            side_step = 0.6
            angle = 91
        elif freq in range(801, 20000):
            speed = 0
            side_step = 0.5
            angle = 131

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

# # Just read sound input and determine sound frequency as fast as possible ##
# while True:
#     freq = acquire_frequency(stream = stream, xf_array = xf, CHUNK = CHUNK, RATE = RATE ) 
#     if freq > 20000:
#         print('Max Frequency:', holder, 'Hz')
#         pass
#     else: 
#         holder = freq
#         print('Max Frequency:', freq, 'Hz')
#############################################################################