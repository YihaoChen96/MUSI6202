import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

"""
Answer to the Question 1, subquestion 2: the length of y is 299 (200 + 100 - 1).
"""

def myTimeConv(x, h):
    K, M = len(x), len(h)
    if K == 0:
        raise ValueError('x cannot be empty')
    if M == 0:
        raise ValueError('h cannot be empty')
    x = np.array(x)
    h = np.array(h)
    
    x_freq = np.fft.fft(x, K+M-1)
    h_freq = np.fft.fft(h, K+M-1)
    y_freq = np.multiply(x_freq, h_freq)
    y = np.fft.ifft(y_freq).real

    return y

def main():
    x = np.ones(200)
    h = signal.triang(51)
    h = h - h[-1] 
    h /= np.max(h)

    y_time = myTimeConv(x, h)

    plt.plot(y_time)
    plt.title("DC vs. Triangular Convolution")
    plt.ylabel("Amplitude")
    plt.xlabel("Sample")
    plt.savefig("results/01-TimeDomainConv.png", format = "png")

if __name__ == "__main__":
    main()


