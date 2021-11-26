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

CHUNK = 1024*2                # samples per frame
FORMAT = pyaudio.paInt16      # audio format (bytes per sample?)
CHANNELS = 1                  # single channel for microphone
RATE = 44100                  # samples per second

# create matplotlib figure and axes
fig, ax = plt.subplots(1)

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

## Stuff for plotting ##

# create semilogx line for spectrum
line_fft, = ax.semilogx(xf, np.random.rand(CHUNK), '-', lw=2)
# format spectrum axes
ax.set_xlim(20, RATE / 2)
ax.set_xlabel('frequency (Hz)')
ax.set_ylabel('Percentage')
ax.set_title('Frequency spectrum')

# # show the plot nonblocking so it can be updated as new data is being calculated
plt.show(block = False)
########################

print('stream started')

while True:
    # binary data
    data = stream.read(CHUNK)  
    
    
    # # To find sound level of input
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
    line_fft.set_ydata(np.abs(y_fourier[0:CHUNK])  / (128 * CHUNK))
    # update figure canvas
    try:
        fig.canvas.draw()
        fig.canvas.flush_events()
        
    except KeyboardInterrupt:
        print('stream stopped')
        break