import numpy as np

def fuse(t1,y1,t2,y2):
	pt=np.hstack((t1,t2+t1[-1]))
	py=np.hstack((y1,y2))

	SOL=np.vstack((pt,py))
	return SOL

def min(pt):
	pt=pt/60
	return pt

def hour(pt):
	pt=pt/3600
	return pt