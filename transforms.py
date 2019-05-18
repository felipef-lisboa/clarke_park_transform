#! /usr/bin/python3

# This file is a library for transformation functions

######
FUNÇÕES QUE FALTAM:
	- abc_to_alphaBeta0
	- alphaBeta0_to_dq0
	- dq0_to_alphaBeta0
	- alphaBeta0_to_abc 
######

def abc_to_dq0(a, b, c, delta):
	delta_b = delta - (2*np.pi/3)
	delta_c = delta + (2*np.pi/3)
	d = np.sqrt(2/3)*(a*np.cos(delta)+b*np.cos(delta_b)+c*np.cos(delta_c))
	q = np.sqrt(2/3)*(-a*np.sin(delta)-b*np.sin(delta_b)-c*np.sin(delta_c))
	z = np.sqrt(2/3)*np.sqrt(1/2)*(a+b+c)
	return d, q, z

def dq0_to_abc(d, q, z, delta):

	######
	# ESCREVER FUNÇÃO AQUI
	######

	return a, b, c