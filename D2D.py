import numpy as np
from matplotlib import pyplot as plt
# UNIPOLER.................................
dec = input("Enter decimal data: ")
bin_data = bin(int(dec))[2:]
data = np.array([0, 0, 0, 0, 0, 0, 0, 0])
for i in range(len(bin_data)):
    data[8 - len(bin_data) + i] = int(bin_data[i])
time = np.arange(len(data))
plt.subplot(2, 3, 1)
plt.step(time, data, where='post')
plt.title('Unipolar')
plt.xlabel('Time')
plt.ylabel('Ammplitude')
plt.text(0, 2, data)
plt.grid(True)
plt.yticks([-2, -1, 0, 1, 2, 3])
plt.xticks(time)

# NRZ-L.......................................
signal = np.zeros(len(data), dtype=int)
for i in range(len(data)):
    if data[i] == 0:
        signal[i] = -1
    else:
        signal[i] = 1
plt.subplot(2, 3, 2)
plt.step(time, signal, where='post')
plt.title('NRZ-L')
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.text(0, 2, data)
plt.grid(True)
plt.yticks([-2, -1, 0, 1, 2, 3])
plt.xticks(time)

# NRZ-I.......................................
signal = np.zeros(len(data), dtype=int)
flg = True
for i in range(len(data)):
    if data[i] == 1:
        flg = not flg
    if flg:
        signal[i] = 1
    else:
        signal[i] = -1

plt.subplot(2, 3, 3)
plt.step(time, signal, where='post')
plt.title('NRZ-I')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.text(0, 2, data)
plt.grid(True)
plt.yticks([-2, -1, 0, 1, 2, 3])
plt.xticks(time)
# RZ.........
time = np.linspace(0, len(data), len(data) * 2)
signal = np.zeros (2 * len(data), dtype=int)
for i in range(0, 2 * len(data), 2):
    if data[i // 2] == 1:
        signal[i] = 1
    else:
        signal[i] = -1
    signal[i + 1] = 0

plt.subplot(2, 3, 4)
plt.step(time, signal, where='post')
plt.title('RZ')
plt.xlabel('Time')
plt.ylabel('Ammplitude')
plt.text(0, 2, data)
plt.grid(True)
plt.yticks([-2, -1, 0, 1, 2, 3])
plt.xticks(np.arange(len(data)))
# MANCHESTER.......
time_org = np.arange(len(data))
signal = np.zeros(len(data) * 2, dtype=int)
for i in range(0, len(data) * 2, 2):
    if data[i // 2] == 0:
        signal[i] = 1
        signal[i + 1] = -1
    else:
        signal[i] = -1
        signal[i + 1] = 1

print(signal)
time = np.arange(len(signal))
plt.subplot(2, 3, 5)
plt.step(time, signal, where='post')
plt.title('Manchestor')
plt.xlabel('Time')
plt.ylabel('Ammplitude')
plt.text(0, 2, data)

plt.grid(True)
plt.yticks([-2, -1, 0, 1, 2, 3])
plt.xticks(2* np.arange(len(data)))
# DIFFERENTIAL MANCHESTER....
time_org = np.arange(len(data))
signal = np.zeros(len(data) * 2, dtype=int)
start = False
for i in range(0, len(data) * 2, 2):
    if start:
        if data[i // 2] == 0:
            signal[i] = -1 * signal[i - 1]
            signal[i + 1] = signal[i - 1]
        else:
            signal[i] = signal[i - 1]
            signal[i + 1] = -1 * signal[i - 1]
    else:
        start = True
        if data[i // 2] == 0:
            signal[i] = -1
            signal[i + 1] = 1
        else:
            signal[i] = 1
            signal[i + 1] = -1
time = np.arange(len(signal))
plt.subplot(2, 3, 6)
plt.step(time, signal, where='post')
plt.title('Differential Manchestor')
plt.xlabel('Time')
plt.ylabel('Ammplitude')
plt.text(0, 2, data)

plt.grid(True)
plt.yticks([-2, -1, 0, 1, 2, 3])
plt.xticks(time_org * 2, time_org)
plt.show()