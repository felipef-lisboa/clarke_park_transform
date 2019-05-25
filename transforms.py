#! /usr/bin/python3
# This file is a library for transformation functions

import numpy as np

# Function to transform abc to alphaBeta0
def abc_to_alphaBeta0(a, b, c):
	alpha = np.sqrt(2/3)*(a - b/2 - c/2)
	beta = np.sqrt(2/3)*np.sqrt(3)*(b/2 - c/2)
	z = (np.sqrt(2/3)/np.sqrt(2))*(a+b+c)
	return alpha, beta, z

# Function to transform alphaBeta0 to dq0
def alphaBeta0_to_dq0(a, b, c, wt, delta):
  d = a*np.cos(wt+delta)+b*np.sin(wt+delta)
  q = b*np.cos(wt+delta)-a*np.sin(wt+delta)
  z = c
  return d, q, z

# Function to directly transform abc to dq0
def abc_to_dq0(a, b, c, wt, delta):
  d = np.sqrt(2/3)*(a*np.cos(wt+delta) + b*np.cos(wt+delta-(2*np.pi/3))+ c*np.cos(wt+delta+(2*np.pi/3)))
  q = np.sqrt(2/3)*(-a*np.sin(wt+delta) - b*np.sin(wt+delta-(2*np.pi/3)) - c*np.sin(wt+delta+(2*np.pi/3)))
  z = (np.sqrt(2/3)/np.sqrt(2))*(a+b+c)
  return d, q, z
