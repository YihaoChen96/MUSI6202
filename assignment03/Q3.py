import numpy as np
from Q1 import generateSinusoidal
from Q2 import generateSquare
import matplotlib.pyplot as plt

def computeSpectrum(x, sample_rate_Hz):

    spectrum = np.fft.fft(x) / x.shape[0]

    value = 1.0 / spectrum.shape[0] * sample_rate_Hz
    f = np.arange(0, (spectrum.shape[0]-1)//2, dtype = int)
    f = f * value

    half_spec = spectrum[:spectrum.shape[0]//2]
    XAbs = np.abs(half_spec)
    XPhase = np.angle(half_spec)
    XRe = half_spec.real
    XIm = half_spec.imag

    return f, XAbs, XPhase, XRe, XIm

if __name__ == "__main__":
    sine_amplitude = 1.0
    sine_sampling_rate_Hz = 44100
    sine_frequency_Hz = 400 
    sine_length_secs = 0.5
    sine_phase_radians = np.pi/2
    sine_t, sine_x = generateSinusoidal(sine_amplitude, sine_sampling_rate_Hz, sine_frequency_Hz, sine_length_secs, sine_phase_radians)

    square_amplitude = 1.0
    square_sampling_rate_Hz = 44100
    square_frequency_Hz = 400 
    square_length_secs = 0.5
    square_phase_radians = 0
    square_t, square_x = generateSquare(square_amplitude, square_sampling_rate_Hz, square_frequency_Hz, square_length_secs, square_phase_radians)

    sine_f, sine_XAbs, sine_XPhase, sine_XRe, sine_XIm = computeSpectrum(sine_x, sine_sampling_rate_Hz)
    square_f, square_XAbs, square_XPhase, square_XRe, square_XIm = computeSpectrum(square_x, square_sampling_rate_Hz)

    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10, 5))
    plt.subplots_adjust(wspace = 0.3, hspace = 0.2)
    ax1.plot(sine_f, sine_XAbs)
    ax1.set_title("Sinusodial's Magnitude Spectrum")
    ax1.set_xlabel("Frequency(Hz)")
    ax1.set_ylabel("Magnitude")
    ax2.plot(sine_f, sine_XPhase)
    ax2.set_title("Sinusodial's Phase Spectrum")
    ax2.set_xlabel("Frequency(Hz)")
    ax2.set_ylabel("Phase")
    plt.savefig("results/03-SinusodialSpectra.png", format = "png")

    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10, 5))
    plt.subplots_adjust(wspace = 0.3, hspace = 0.2)
    ax1.plot(square_f, square_XAbs)
    ax1.set_title("Square Wave's Magnitude Spectrum")
    ax1.set_xlabel("Frequency(Hz)")
    ax1.set_ylabel("Magnitude")
    ax2.plot(square_f, square_XPhase)
    ax2.set_title("Square Wave's Phase Spectrum")
    ax2.set_xlabel("Frequency(Hz)")
    ax2.set_ylabel("Phase")
    plt.savefig("results/03-SquareWaveSpectra.png", format = "png")


