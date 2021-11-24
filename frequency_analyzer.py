import pyaudio
import struct
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import time

mic = pyaudio.PyAudio()
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 20000
CHUNK = int(RATE/20)
stream = mic.open(format=FORMAT, 
                 channels=CHANNELS, 
                 rate=RATE, 
                 input=True, 
                 output=True, 
                 frames_per_buffer=CHUNK)

plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')

try:
    while True:
        data = stream.read(CHUNK)
        data = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype='b')
        print(data.size)
        # print(data)
        # f, t, Sxx = signal.spectrogram(data, fs=CHUNK)
        # dBS = 10 * np.log10(Sxx)
        # print(dBS)
        time.sleep(1)
        # plt.pcolormesh(t, f, dBS)
        # plt.pause(0.005)
except KeyboardInterrupt:
    pass