import numpy as np
import matplotlib.pyplot as plt

from Q1 import generateSinusoidal

def generateSquare(amplitude, sampling_rate_Hz, frequency_Hz, length_secs, phase_radians):


    harmonics = [(2*k - 1) for k in range(1,11)]
    ts = []
    xs = []
    for harm in harmonics:

        t_sine, x_sine = generateSinusoidal(amplitude/harm, sampling_rate_Hz, harm*frequency_Hz, length_secs, phase_radians)
        ts.append(t_sine)
        xs.append(x_sine)
    t = ts[0]
    x = 4/np.pi * np.sum(xs, axis = 0)
    assert len(t) == len(x)
    return np.array(t), np.array(x)

if __name__ == "__main__":
    amplitude = 1.0
    sampling_rate_Hz = 44100
    frequency_Hz = 400 
    length_secs = 0.5
    phase_radians = 0
    t, x = generateSquare(amplitude, sampling_rate_Hz, frequency_Hz, length_secs, phase_radians)
    
    idx = int(sampling_rate_Hz * 0.005)
    fig, ax = plt.subplots(1,1)
    ax.set_xlabel("Time(second)")
    ax.set_ylabel("Amplitude")
    ax.set_title("Square Wave")
    ax.plot(t[:idx], x[:idx])
    plt.savefig("results/02-squarewave.png", format = "png")