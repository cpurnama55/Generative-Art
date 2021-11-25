import pyaudio                      # For actual audio input 
import struct                       # Let's us unpack audio data into integers as opposed to binary values
import numpy as np                  # To store data in arrays and perform operations
import matplotlib.pyplot as plt     # To help visualize data
import time
import sys
from tkinter import TclError

### IGNORE FOR NOW ###
#For the backend
# Using inline backend makes graph updating choppy, using
# this seperate one should speed things up
# %matplotlib tk
######################

CHUNK = 1024                        # How much audio samples that will be processed/displayed in a frame at a time
FORMAT = pyaudio.paInt16            # Number of bytes per channel
CHANNELS = 1                        # We're using just a microphone, so we'll just be accessing from one channel
RATE = 44100                        # Samples taken in per second, defined in frequency 

####################################################################################
# create matplotlib figure and axes
fig, ax = plt.subplots(1, figsize=(15, 7))

# pyaudio class instance
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

# variable for plotting
x = np.arange(0, 2 * CHUNK, 2)

# create a line object with random data
line, = ax.plot(x, np.random.rand(CHUNK), '-', lw=2)

# basic formatting for the axes
ax.set_title('AUDIO WAVEFORM')
ax.set_xlabel('samples')
ax.set_ylabel('volume')
ax.set_ylim(0, 255)
ax.set_xlim(0, 2 * CHUNK)
plt.setp(ax, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0, 128, 255])

# show the plot
plt.show(block = False)

print('stream started')

# for measuring frame rate
frame_count = 0
start_time = time.time()

# data = stream.read(CHUNK)       
# data_int = struct.unpack(str(2 * CHUNK) + 'B', data)
np.set_printoptions(threshold=sys.maxsize)
while True:
    
    # Read samples from the stream for the specified number of frames. This returns raw byte values, not integers
    data = stream.read(CHUNK)       
    
    # In order to get understandable values, we need to convert the read data into integers
    # Convert the data from raw bytes to integers. We specify a size of 2 * chunk because the data input is actually twice the size of CHUNK. Also pass in the data.
    data_int = struct.unpack(str(2 * CHUNK) + 'B', data)
   
    # We will also convert the struct data into a numpy array for easier presentation of the data
    # dtype b is an integer from 0 to 255   
    # Offset by 128 in order to loop values that exceed 255 back around
    # Adding half the range (255) will cause data values to wrap back around, eliminating the clipping issue
    data_np = np.array(data_int, dtype='b')[::2] + 128


    # Update data to be dispplayed
    line.set_ydata(data_np)
    
    # update figure canvas
    try:
        fig.canvas.draw()
        fig.canvas.flush_events()
        frame_count += 1
        
    except TclError:
        
        # calculate average frame rate
        frame_rate = frame_count / (time.time() - start_time)
        
        print('stream stopped')
        print('average frame rate = {:.0f} FPS'.format(frame_rate))
        break
####################################################################





####################################################################
# p = pyaudio.PyAudio()               # Class instance for PyAudio, main tool to interface to PortAudio (audio I/O library)
# stream = p.open(                    # Create a new data stream (which is a class) using our pre-defined parameters, store to a variable so we can modify later
#     format = FORMAT,
#     channels = CHANNELS,
#     rate = RATE,
#     input = True,
#     output = True,
#     frames_per_buffer = CHUNK
# )

# data = stream.read(CHUNK)           # Read samples from the stream for the specified number of frames. This returns raw byte values, not integers

# # In order to get understandable values, we need to convert the read data into integers
# # Convert the data from raw bytes to integers. We specify a size of 2 * chunk because the data input is actually twice the size of CHUNK. Also pass in the data.
# # We will also convert the struct data into a numpy array for easier presentation of the data
# # dtype b is an integer from 0 to 255   
# # Adding half the range (255) will cause data values to wrap back around, eliminating the clipping issue
# data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), 'b')[::2] + 127  

# # np.set_printoptions(threshold=sys.maxsize)
# # while True:
# #     print(data_int)
# #     time.sleep(1)

# # We can now plot the data
# fig, ax = plt.subplots()
# ax.plot(data_int, '-')
# plt.show()