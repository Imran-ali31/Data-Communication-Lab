import numpy as np
import matplotlib.pyplot as plt
A_c = 3 #float(input('Enter carrier amplitude: '))
f_c = 40 #float(input('Enter carrier frquency: '))
A_m = 2 #float(input('Enter message amplitude: '))
f_m = 4 #float(input('Enter message frquency: '))
t = np.linspace(0, 1, 1000)
carrier = A_c*np.cos(2*np.pi*f_c*t)
modulator = A_m*np.cos(2*np.pi*f_m*t)
product = A_c*(1+np.cos(2*np.pi*f_m*t))*np.cos(2*np.pi*f_c*t)
plt.subplot(3,3,1)
plt.title('Amplitude Modulation')
plt.plot(modulator)
plt.ylabel('Amplitude')
plt.xlabel('Message signal')

plt.subplot(3,3,4)
plt.plot(carrier)
plt.ylabel('Amplitude')
plt.xlabel('Carrier signal')

plt.subplot(3,3,7)
plt.plot(product)
plt.ylabel('Amplitude')
plt.xlabel('AM signal')
#Frequency Modulation..............
modulator = np.sin(2 * np.pi * f_m * t)
carrier = np.sin(2 * np.pi * f_c * t)
product = np.zeros_like(modulator)

for i, t in enumerate(t):
    product[i] = np.sin(2 * np.pi * (f_c * t + modulator[i]))

plt.subplot(3, 3, 2)
plt.title('Frequency Modulation')
plt.plot(t,modulator)
plt.ylabel('Amplitude')
plt.xlabel('Message signal')

plt.subplot(3, 3, 5)
plt.plot(t,carrier)
plt.ylabel('Amplitude')
plt.xlabel('Carrier signal')

plt.subplot(3, 3, 8)
plt.plot(t,product)
plt.ylabel('Amplitude')
plt.xlabel('FM signal')
plt.tight_layout()
#Phase Modulation.............................
carrier = 200.0
modulator = 800.0
beta = 1.0
x1 = np.linspace(0.0, 0.03, num=2000)
y1 = np.sin(carrier * np.pi * x1)
y2 = np.cos(modulator * np.pi * x1)
y3 = np.sin(carrier * np.pi * x1 + beta * y2)
plt.subplot(3, 3, 3)
plt.plot(x1, y1)
plt.title('Phase Modulation')
plt.ylabel('Amplitude')
plt.xlabel('Message Signal')
plt.grid(True)

plt.subplot(3, 3, 6)
plt.plot(x1, y2)
plt.ylabel('Amplitude')
plt.xlabel('Carrier Signal')
plt.grid(True)

plt.subplot(3, 3, 9)
plt.plot(x1, y3)
plt.ylabel('Amplitude')
plt.xlabel('PM Signal')
plt.grid(True)
plt.yticks([-2, -1, 0, 1, 2, 3])
plt.tight_layout()
plt.show()