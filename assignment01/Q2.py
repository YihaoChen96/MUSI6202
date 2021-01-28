from Q1 import crossCorr, loadSoundFile
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

def findSnarePosition(snareFilename, drumloopFilename):
    snare_rate, snare_data = loadSoundFile(snareFilename)
    drum_rate, drum_loop = loadSoundFile(drumloopFilename)
    corr = crossCorr(snare_data, drum_loop)
    peaks, properties = find_peaks(corr, height = 0.75)
    return list(peaks)

if __name__ == "__main__":
    peaks = findSnarePosition("snare.wav", "drum_loop.wav")
    with open("results/02-snareLocation.txt", "w") as f:
        f.writelines("%s\n" % p for p in peaks)
