#! /usr/bin/python3

# This program says hello 
print('Hello world!')

import numpy as np
import matplotlib.pyplot as plt
import transforms as trs

# User configurable
freq = 1/60
end_time = 180
v_peak = 200
step_size = 0.01
# Find the three-phase voltages
Va = []
Vb = []
Vc = []
wt = 2 * np.pi * freq * np.arange(0,end_time,step_size)
for ii, t in enumerate(wt):
  Va.append((v_peak) * np.sin(t))
  Vb.append((v_peak) * np.sin(t - (2/3)*np.pi))
  Vc.append((v_peak) * np.sin(t + (2/3)*np.pi))
Va, Vb, Vc = np.array(Va), np.array(Vb), np.array(Vc)

# Calculate the dq0 system
alpha, beta, zero1= trs.abc_to_alphaBeta0(Va, Vb, Vc)
d, q, zero2 = trs.abc_to_dq0(Va,Vb,Vc, wt, 0)

# Plot the 3-phase system
plt.subplot(311)
plt.plot(Va, label="Va")
plt.plot(Vb, label="Vb")
plt.plot(Vc, label="Vc")
plt.ylabel('Voltage')
plt.legend(ncol=3,loc=4)
# Plot the alphaBeta0 system
plt.subplot(312)
plt.plot(alpha, label="\u03B1")
plt.plot(beta, label="\u03B2")
plt.plot(zero1, label="zero")
plt.ylabel('Voltage')
plt.legend(ncol=3,loc=4)
# Plot the dq0 system
plt.subplot(313)
plt.plot(d, label="d")
plt.plot(q, label="q")
plt.plot(zero2, label="zero")
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.legend(ncol=3,loc=4)
plt.show()
#plt.savefig('plot.png')
print('Plot done')
