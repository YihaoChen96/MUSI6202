import numpy as np
import matplotlib.pyplot as plt

def generateSinusoidal(amplitude, sampling_rate_Hz, frequency_Hz, length_secs, phase_radians):
    sample_num = int(sampling_rate_Hz * length_secs)
    t = np.arange(0, (sample_num+1)/sampling_rate_Hz, 1/sampling_rate_Hz)
    x = amplitude * np.sin(2*np.pi*frequency_Hz*t + phase_radians)

    assert len(t) == len(x)
    return np.array(t), np.array(x)





if __name__ == "__main__":
    amplitude = 1.0
    sampling_rate_Hz = 44100
    frequency_Hz = 400 
    length_secs = 0.5
    phase_radians = np.pi/2
    t, x = generateSinusoidal(amplitude, sampling_rate_Hz, frequency_Hz, length_secs, phase_radians)

    idx = int(sampling_rate_Hz * 0.005)
    fig, ax = plt.subplots(1,1)
    ax.set_xlabel("Time(second)")
    ax.set_ylabel("Amplitude")
    ax.set_title("Sinusoidal")
    ax.plot(t[:idx], x[:idx])
    plt.savefig("results/01-sinusoidal.png", format = "png")


