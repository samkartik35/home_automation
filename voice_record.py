import pyaudio
import wave
import time as t
from datetime import datetime
from pytz import timezone


import matplotlib.pyplot as plt
import numpy as np
import wave, sys

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
RECORD_SECONDS = 2
WAVE_OUTPUT_FILENAME = "output.wav"



# shows the sound waves
def visualize(path: str):
	
	# reading the audio file
	raw = wave.open(path)
	
	# reads all the frames
	# -1 indicates all or max frames
	signal = raw.readframes(-1)
	signal = np.frombuffer(signal, dtype ="int16")
	
	# gets the frame rate
	f_rate = raw.getframerate()

	# to Plot the x-axis in seconds
	# you need get the frame rate
	# and divide by size of your signal
	# to create a Time Vector
	# spaced linearly with the size
	# of the audio file
	time = np.linspace(
		0, # start
		len(signal) / f_rate,
		num = len(signal)
	)

	# using matlplotlib to plot
	# creates a new figure
	plt.figure(1)
	
	# title of the plot
	plt.title("Sound Wave")
	
	# label of x-axis
	plt.xlabel("Time")
	
	# actual ploting
	plt.plot(time, signal)
	
	# shows the plot
	# in new window
	plt.show()

	# you can also save
	# the plot using
	# plt.savefig('filename')

def get_time_stamp():
    fmt = "%Y-%m-%d %H:%M:%S"

    now_time = datetime.now(timezone('ASIA/Calcutta'))
    time = now_time.strftime(fmt)
    return(time)

def init_recording():

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
    return(stream,p)
    
def record_samples(stream,p):
    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()
    time_stamp = get_time_stamp()
    dt = time_stamp.split(' ')
    
    tm = dt[1].split(':')

    print(dt[0])
    print(dt[1])
    tm = tm[0] + '_' + tm[1] +'_' + tm[2]
    output_file = 'samples/audio_sample_' + dt[0]+'_' + tm  +'.wav'
    print(output_file)

    wf = wave.open(output_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return(output_file)

stream,p = init_recording()
file = record_samples(stream,p)
print("file name:",file)
visualize(file)
