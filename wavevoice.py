import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read('wavevoice.wav')
print(fs,len(data),data)
plt.subplot(211)
plt.plot(data)
t=np.arange(0,len(data)/fs,1.0/fs)
plt.subplot(212)
plt.plot(t,data)
wav.write('wavevoice-fast.wav',2*fs,data)
plt.show( )
