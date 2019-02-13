import matplotlib.pyplot as plt;
import numpy as np;
fs=int(input("enter a sampling frequency"))
f1=int(input("enter frequency"))
f2=int(input("enter frequency"))
n=int(input("enter a samples"))
q=int(input("enter phase for first wave:"));
x=np.arange(n);
a=np.sin((2*np.pi*f1/fs*x)+q);
plt.subplot(311);
plt.plot(x,a);
plt.xlabel("samples(n)");
plt.ylabel("amplitude(v)");
p=int(input("enter phase for second wave:"));
b=np.sin((2*np.pi*f2/fs*x)+p);
plt.subplot(312);
plt.plot(x,b);
plt.xlabel("samples(n)");
plt.ylabel("amplitude(v)");
plt.show()
