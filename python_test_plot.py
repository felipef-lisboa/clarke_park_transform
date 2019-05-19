#! /usr/bin/python3

# This program says hello 
print('Hello world!')

import numpy as np
import matplotlib.pyplot as plt

# Function to transform abc to dq0
def abc_to_alphaBeta0(a, b, c):
	alpha = np.sqrt(2/3)*(a - b/2 - c/2)
	beta = np.sqrt(2/3)*np.sqrt(3)*(b/2 - c/2)
	z = (np.sqrt(2/3)/np.sqrt(2))*(a+b+c)
	return alpha, beta, z

def alphaBeta0_to_dq0(a, b, c, delta):
  d = a*np.cos(thetas+delta)+b*np.sin(thetas+delta)
  q = b*np.cos(thetas+delta)-a*np.sin(thetas+delta)
  z = c
  return d, q, z

def abc_to_dq0(a, b, c, delta):
  d = np.sqrt(2/3)*(a*np.cos(thetas+delta) + b*np.cos(thetas+delta-(2*np.pi/3))+ c*np.cos(thetas+delta+(2*np.pi/3)))
  q = np.sqrt(2/3)*(-a*np.sin(thetas+delta) - b*np.sin(thetas+delta-(2*np.pi/3)) - c*np.sin(thetas+delta+(2*np.pi/3)))
  z = (np.sqrt(2/3)/np.sqrt(2))*(a+b+c)
  return d, q, z

# User configurable
freq = 1/60
end_time = 180
v_peak = 100
step_size = 0.01
# Find the three-phase voltages
Va = []
Vb = []
Vc = []
thetas = 2 * np.pi * freq * np.arange(0,end_time,step_size)
for ii, t in enumerate(thetas):
  Va.append((v_peak+50) * np.sin(t))
  Vb.append((v_peak) * np.sin(t - (2/3)*np.pi))
  Vc.append((v_peak) * np.sin(t + (2/3)*np.pi))
Va, Vb, Vc = np.array(Va), np.array(Vb), np.array(Vc)

# Calculate the dq0 system
alpha, beta, zero1= abc_to_alphaBeta0(Va, Vb, Vc)
d, q, zero2 = abc_to_dq0(Va,Vb,Vc, 0)

# Plot the 3-phase system
plt.subplot(311)
plt.plot(Va, label="Va")
plt.plot(Vb, label="Vb")
plt.plot(Vc, label="Vc")
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.legend(ncol=3,loc=4)
# Plot the alphaBeta0 system
plt.subplot(312)
plt.plot(alpha, label="alpha")
plt.plot(beta, label="beta")
plt.plot(zero1, label="zero")
plt.legend(ncol=3,loc=4)
# Plot the dq0 system
plt.subplot(313)
plt.plot(d, label="d")
plt.plot(q, label="q")
plt.plot(zero2, label="zero")
plt.legend(ncol=3,loc=4)
plt.show()
#plt.savefig('plot.png')
print('Plot done')
