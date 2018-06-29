import numpy as np

def fuse(sol,sol2):
	pt=np.hstack((sol.t,sol2.t+sol.t[-1]))
	py=np.hstack((sol.y,sol2.y))

	SOL=np.vstack((pt,py))
	return SOL

def min(pt):
	pt=pt/60
	return pt

def hour(pt):
	pt=pt/3600
	return pt