#! /usr/bin/python3

# This program says hello 
print('Hello world!')

import numpy as np
import matplotlib.pyplot as plt

# Function to transform abc to dq0
def dq0_transform(a, b, c, delta):
	delta_b = delta - (2*np.pi/3)
	delta_c = delta + (2*np.pi/3)
	d = np.sqrt(2/3)*(a*np.cos(delta)+b*np.cos(delta_b)+c*np.cos(delta_c))
	q = np.sqrt(2/3)*(-a*np.sin(delta)-b*np.sin(delta_b)-c*np.sin(delta_c))
	z = np.sqrt(2/3)*np.sqrt(1/2)*(a+b+c)
	return d, q, z
#     d=(np.sqrt(2/3)*v_a-(1/(np.sqrt(6)))*v_b-(1/(np.sqrt(6)))*v_c)
#     q=((1/(np.sqrt(2)))*v_b-(1/(np.sqrt(2)))*v_c)
#     return d, q

# User configurable
freq = 1/60
end_time = 180
v_peak = 220
step_size = 0.01
# Find the three-phase voltages
Va = []
Vb = []
Vc = []
thetas = 2 * np.pi * freq * np.arange(0,end_time,step_size)
for ii, t in enumerate(thetas):
    Va.append(v_peak * np.sin(t))
    Vb.append(v_peak * np.sin(t - (2/3)*np.pi))
    Vc.append(v_peak * np.sin(t - (4/3)*np.pi))
Va, Vb, Vc = np.array(Va), np.array(Vb), np.array(Vc)

# Calculate the dq0 system
d, q, z= dq0_transform(Va, Vb, Vc, 0)

# Plot the 3-phase system
plt.subplot(211)
plt.plot(Va, label="Va")
plt.plot(Vb, label="Vb")
plt.plot(Vc, label="Vc")
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.legend(ncol=3,loc=4)
# Plot the dq0 system
plt.subplot(212)
plt.plot(d, label="d")
plt.plot(q, label="q")
plt.plot(z, label="z")
plt.show()