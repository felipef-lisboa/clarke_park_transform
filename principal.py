#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import transforms as trs
# User configurable
freq = 1 / 60
end_time = 180
v_peak = 200
step_size = 0.01
# Creates the three-phase vectors abc
vector_a = []
vector_b = []
vector_c = []
wt = 2 * np.pi * freq * np.arange(0, end_time, step_size)
for ii, t in enumerate(wt):
  vector_a.append((v_peak) * np.sin(t))
  vector_b.append((v_peak) * np.sin(t - (2 / 3) * np.pi))
  vector_c.append((v_peak) * np.sin(t + (2 / 3) * np.pi))
  vector_a, vector_b, vector_c = np.array(vector_a), np.array(
    vector_b), np.array(vector_c)

# Calls the transformation functions
alpha, beta, zero1 = trs.abc_to_alphaBeta0(vector_a, vector_b, vector_c)
d, q, zero2 = trs.abc_to_dq0(vector_a, vector_b, vector_c, wt, 0)

# Plot the 3-phase system
plt.subplot(311)
plt.plot(vector_a, label="a")
plt.plot(vector_b, label="b")
plt.plot(vector_c, label="c")
plt.ylabel('Voltage')
plt.legend(ncol=3, loc=4)
# Plot the alphaBeta0 system
plt.subplot(312)
plt.plot(alpha, label="\u03B1")  # alpha letter in unicode
plt.plot(beta, label="\u03B2")  # beta letter in unicode
plt.plot(zero1, label="zero")
plt.ylabel('Voltage')
plt.legend(ncol=3, loc=4)
# Plot the dq0 system
plt.subplot(313)
plt.plot(d, label="d")
plt.plot(q, label="q")
plt.plot(zero2, label="zero")
plt.ylabel('Voltage')
plt.xlabel('Time')
plt.legend(ncol=3, loc=4)
#plt.show()
plt.savefig('plot.png')
print('Plot done')
