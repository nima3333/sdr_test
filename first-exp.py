from rtlsdr import RtlSdr
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["figure.figsize"] = (25,10)

sdr = RtlSdr()

freq = [67.978, 69.967]
#sdr.freq_correction = 60   # PPM
sdr.sample_rate = 2.048e6//8  # Hz

for i in range(len(freq)):
    f = freq[i]
    # configure device
    sdr.center_freq = f*1e6     # Hz
    sdr.gain = 'auto'

    samples = np.array(sdr.read_samples(2.048e6//2))
    plt.subplot(1, len(freq), i+1)
    plt.plot(range(len(samples)), np.abs(samples))
    plt.title(f"Frequency f={f} MHz")
plt.show()