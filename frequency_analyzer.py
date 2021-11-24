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