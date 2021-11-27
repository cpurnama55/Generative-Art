from acquire_frequency import acquire_frequency
import pyaudio
import numpy as np

# constants
# 11025 samples min offset 2HZ max offset 5 HZ
# 22050 samples min offset 1HZ max offset 2 HZ

# Setting chunk sample size higher produces a more accurate frequency determination however it increases processing time
# I think a good middle ground is using 11025 sample size, using 22050 doubles time from 250 ms to 500 ms
CHUNK = 11025                # samples per frame
FORMAT = pyaudio.paInt16     # audio format of data
CHANNELS = 1                 # single channel for microphone
RATE = 44100                 # samples per second
CHUNK = 11025                # samples per frame
FORMAT = pyaudio.paInt16     # audio format of data
CHANNELS = 1                 # single channel for microphone
RATE = 44100                 # samples per second

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
holder = 0
carrier = np.array([])

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
    
while True:
    freq = acquire_frequency(stream = stream, xf_array = xf, CHUNK = CHUNK, RATE = RATE )
    if freq > 20000:
        print('Max Frequency:', holder, 'Hz')
        pass
    else: 
        holder = freq
        print('Max Frequency:', freq, 'Hz')