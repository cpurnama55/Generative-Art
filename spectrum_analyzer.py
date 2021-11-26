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
CHUNK = 44100             # samples per frame
FORMAT = pyaudio.paInt16     # audio format (bytes per sample?)
CHANNELS = 1                 # single channel for microphone
# RATE = 44100                # samples per second
RATE = 44100

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

## Stuff for plotting ##
# variable for plotting
xf = np.linspace(0, RATE, CHUNK)     # frequencies (spectrum)

# create semilogx line for spectrum
line_fft, = ax.semilogx(xf, np.random.rand(CHUNK), '-', lw=2)

# format spectrum axes
ax.set_xlim(20, RATE / 2)
ax.set_xlabel('frequency (Hz)')
ax.set_ylabel('Percentage')
ax.set_title('Frequency spectrum')

# show the plot nonblocking so it can be updated as new data is being calculated
plt.show(block = False)
########################

print('stream started')

# for measuring frame rate
frame_count = 0
start_time = time.time()


while True:
    
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
    # max_index = np.argmax(buffer[20:int(RATE/2)])
    # print(xf[buffer.argmax])
    print(int(xf[buffer[1:].argmax()] + 1))
    # print(np.size(xf))
    # line_fft.set_ydata(buffer)
    
    # update figure canvas
    # try:
    #     fig.canvas.draw()
    #     fig.canvas.flush_events()
    #     frame_count += 1
        
    # except KeyboardInterrupt:
    #     # calculate average frame rate
    #     frame_rate = frame_count / (time.time() - start_time)
        
    #     print('stream stopped')
    #     print('average frame rate = {:.0f} FPS'.format(frame_rate))
    #     break