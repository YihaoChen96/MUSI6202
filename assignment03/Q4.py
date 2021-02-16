import numpy as np
from Q1 import generateSinusoidal
from Q2 import generateSquare
from Q3 import computeSpectrum
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

def generateBlocks(x, sample_rate_Hz, block_size, hop_size):
    block_num = int(np.ceil(x.shape[0]/hop_size))
    x = np.pad(x, (0,block_num*block_size - x.shape[0]), constant_values = 0)
    X = np.zeros((block_num, block_size))
    for i in range(block_num):
        X[i] = x[i*hop_size:i*hop_size+block_size]
    t = np.arange(block_num)*hop_size/sample_rate_Hz
    X = X.T
    return t, X

def mySpecgram(x,  block_size, hop_size, sampling_rate_Hz, window_type):

    
    fig, ax = plt.subplots(1,1) 
    if window_type == "rect":
        rect_window = np.ones(block_size)
        title = "Rect-Windowed Spectrogram"
        fname = "results/04-rect_specgram.png"
        magnitude_spectrogram, freq_vector, time_vector, im = ax.specgram(x, sides = "onesided", Fs = sampling_rate_Hz, NFFT = block_size, noverlap = block_size - hop_size, window = rect_window)
    elif window_type == "hann":
        hann_window = np.hanning(block_size)
        title = "Hann-Windowed Spectrogram"
        fname = "results/04-hann_specgram.png"
        magnitude_spectrogram, freq_vector, time_vector, im = ax.specgram(x, sides = "onesided", Fs = sampling_rate_Hz, NFFT = block_size, noverlap = block_size - hop_size, window = hann_window)
    else:
        raise NotImplementedError("Window type not supported")
    
    ax.set_xlabel("Time(second)")
    ax.set_ylabel("Frequency(Hz)")
    ax.set_title(title)
    plt.savefig(fname)

    return freq_vector[1:], time_vector, magnitude_spectrogram[1:]

if __name__ == "__main__":
    square_amplitude = 1.0
    square_sampling_rate_Hz = 44100
    square_frequency_Hz = 400 
    square_length_secs = 0.5
    square_phase_radians = 0
    square_t, square_x = generateSquare(square_amplitude, square_sampling_rate_Hz, square_frequency_Hz, square_length_secs, square_phase_radians)

    block_size = 2048
    hop_size = 1024

    rect_freq_vector, rect_time_vector, rect_magnitude_spectrogram = mySpecgram(square_x , block_size, hop_size, square_sampling_rate_Hz, 'rect')
    hann_freq_vector, hann_time_vector, hann_magnitude_spectrogram = mySpecgram(square_x , block_size, hop_size, square_sampling_rate_Hz, 'hann')