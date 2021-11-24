import pyaudio                      # For actual audio input 
import struct                       # Let's us unpack audio data into integers as opposed to binary values
import numpy as np                  # To store data in arrays and perform operations
import matplotlib.pyplot as plt     # To help visualize data

### IGNORE FOR NOW ###
#For the backend
# Using inline backend makes graph updating choppy, using
# this seperate one should speed things up
# %matplotlib tk
######################

CHUNK = 1024 * 4                    # How much audio samples that will be processed/displayed in a frame at a time
FORMAT = pyaudio.paInt16            # Number of bytes per channel
CHANNELS = 1                        # We're using just a microphone, so we'll just be accessing from one channel
RATE = 44100                        # Samples taken in per second, defined in frequency 

p = pyaudio.PyAudio()               # Class instance for PyAudio, main tool to interface to PortAudio (audio I/O library)
stream = p.open(                    # Create a new data stream (which is a class) using our pre-defined parameters, store to a variable so we can modify later
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = CHUNK
)

data = stream.read(CHUNK)           # Read samples from the stream for the specified number of frames. This returns raw byte values, not integers

# In order to get understandable values, we need to convert the read data into integers
# Convert the data from raw bytes to integers. We specify a size of 2 * chunk because the data input is actually twice the size of CHUNK. Also pass in the data.
# We will also convert the struct data into a numpy array for easier presentation of the data
# dtype b is an integer from 0 to 255   
# Adding half the range (255) will cause data values to wrap back around, eliminating the clipping issue
data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), 'b') + 127  


# We can now plot the data
fig, ax = plt.subplots()
ax.plot(data_int, '-')
plt.show()
# One thing to take note of is that the displayed data will be somewhat clipped/cutoff
# We can fix this by shifting the data to look like a proper waveform