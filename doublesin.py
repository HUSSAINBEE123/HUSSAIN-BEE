importmatplotlib.pyplot as mp
import numpy as np
fs=int(input("enter a sampling frequency"))
f1 = int(input("enter a first frequency"))
f2=int(input("enter a second frequency"))
time=int(input("enter a time"))
x = np.arange(time)
y1 = np.sin(2 *np. pi * f1 * x/ fs)
mp.subplot(121)
mp.plot(x, y1)
mp.xlabel('time(samples)')
mp.ylabel('amplitude')
y2=np.sin(2 *np.pi * f2* x/ fs)
mp.subplot(122)
mp.plot(x,y2)
mp.xlabel('time(samples)')
mp.ylabel('amplitude')
mp.show()