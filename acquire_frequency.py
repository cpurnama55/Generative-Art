from numpy.core.fromnumeric import size
import pyaudio
import audioop
import os
import struct
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import time

# constants
# 11025 samples min offset 2HZ max offset 5 HZ
# 22050 samples min offset 1HZ max offset 2 HZ
CHUNK = 11025                # samples per frame
# CHUNK = 22050
FORMAT = pyaudio.paInt16     # audio format (bytes per sample?)
CHANNELS = 1                 # single channel for microphone
RATE = 44100               # samples per second

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

# Array of frequencies
# Instead of using the full spectrum, there are CHUNK evenly spaced out frequencies to choose from
xf = np.linspace(0, RATE, CHUNK)     # frequencies (spectrum)

print('stream started')

while True:
    try:
        start_time = time.time()
        # binary data
        data = stream.read(CHUNK)  
        
        # # Take the RMS of the data
        # rms = audioop.rms(data, 2)
        # try:
        #     decibel = int(20 * np.log10(rms))
        #     line_fft.set_ydata(decibel)
        #     print(decibel)
        # except OverflowError:
        #     print('Still starting up...')
        #     pass
        
        # # convert data to integers
        data_int = struct.unpack(str(2 * CHUNK) + 'B', data)
        # create np array and offset by 128
        data_np = np.array(data_int, dtype='b')[::2] + 128
        # # compute FFT and update line
        y_fourier = fft(data_int)
        buffer = np.abs(y_fourier[0:CHUNK])  / (128 * CHUNK)

        freq = int(xf[buffer[1:].argmax()])
        if freq > 20000:
            print('Bad reading')
            pass
        else: 
            print('Max Frequency:', freq, 'Hz')
            print('Duration: {0:.2f}'.format(time.time() - start_time, 's'))
    except KeyboardInterrupt:
        print('stream stopped')