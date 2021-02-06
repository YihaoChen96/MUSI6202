from scipy.signal import correlate, correlation_lags
from scipy.io.wavfile import read as readwav
import matplotlib.pyplot as plt
import numpy as np


def crossCorr(x, y):
    corr = correlate(x,y)
    corr /= np.max(corr)
    return corr

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


def main():
    snare_rate, snare_data = loadSoundFile("snare.wav")
    drum_rate, drum_loop = loadSoundFile("drum_loop.wav")
    corr = crossCorr(drum_loop, snare_data)

    # Plot figure
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(corr)
    ax.set_title("Cross-Correlated Signal")
    ax.set_xlabel("Sample Position")
    plt.savefig("results/01-correlation.png", format = "png")
    