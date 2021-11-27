from numpy.core.fromnumeric import size
import pyaudio
import audioop
import os
import struct
import numpy as np
from scipy.fftpack import fft
import time

# Function for acquiring frequencies
def acquire_frequency(stream, xf_array, CHUNK = 11025, RATE = 44100):
    # Stream should be initialized before hand and passed in as an input
    # As part of stream intialization, a PyAudio class needs to be intialized beforehand
    # These steps aren't done here to reduce redundancy on every call to acquire a frequency

    # Array of frequencies
    # Instead of using the full spectrum, there are CHUNK evenly spaced out frequencies to choose from
    xf_array = np.linspace(0, RATE, CHUNK)     # frequencies (spectrum)

    data = stream.read(CHUNK)
    # convert data to integers
    data_int = struct.unpack(str(2 * CHUNK) + 'B', data)
    # create np array and offset by 128
    data_np = np.array(data_int, dtype='b')[::2] + 128
    # compute FFT 
    y_fourier = fft(data_int)
    # Find the absolute value of decibel level, and convert it to percentage
    buffer = np.abs(y_fourier[0:CHUNK])  / (128 * CHUNK)
    # Find the frequency at which the highest decibel occurs and return the value
    return int(xf_array[buffer[1:].argmax()])