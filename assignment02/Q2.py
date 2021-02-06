from Q1 import myTimeConv

from scipy import signal
from scipy.io.wavfile import read as readwav

import numpy as np 
import time


def loadSoundFile(filename):
    rate, data = readwav(filename)

    # Get left channel
    origin = data
    if len(data.shape) > 1:
        data = data[:,0]
        
    # Normalize
    if data.dtype != 'float32':
        if data.dtype == 'uint8':
            bits = 8
        elif data.dtype == 'int16':
            bits = 16
        elif data.dtype == 'int32':
            bits = 32

        data = data / float(2**(bits - 1))

    if data.dtype == 'uint8':
        data = data - 1.

    return rate, data

def CompareConv(x, h):
    
    time_arr = np.zeros(2)
    
    # Custom method
    start = time.time()
    my_conv = myTimeConv(x, h)
    end = time.time()
    time_arr[0] = end-start


    # Scipy method
    start = time.time()
    scipy_conv= signal.convolve(x, h)
    end = time.time()
    time_arr[1] = end-start
    
    m = np.mean(my_conv - scipy_conv)
    mabs = np.mean(np.abs(my_conv - scipy_conv))
    stdev = np.std(my_conv-scipy_conv)

    return m, mabs, stdev, time_arr

def main():
    sr_x, x = loadSoundFile("piano.wav")
    sr_h, h = loadSoundFile("impulse-response.wav")

    m, mabs, stdev, time_arr = CompareConv(x, h)

    with open("results/02-report.txt","w") as f:
        f.write("Mean Diff: %s\n" % m)
        f.write("Abs Mean Diff: %s\n" % mabs)
        f.write("Stdev: %s\n" % stdev)
        f.write("MyConv Time Used: %f sec, Scipy Time Used: %f sec\n" % (time_arr[0], time_arr[1]))

if __name__ == "__main__":
    main()
