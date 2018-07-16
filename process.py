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

def norm(x):
	m=np.amax(x)
	for i in range(0,len(x)):
		x[i]=x[i]/m
	return x

def discr(x,*thresh):
	l=len(thresh)
	lx=len(x)
	y=np.zeros((lx,))
	for i in range(0,len(x)):
		for j,k in enumerate(thresh):
			if x[i]<k:
				y[i]=j/l
				break
			elif x[i]==k:
				y[i]=j/l+1/(2*l)
				break
			else:
				y[i]=(j+1)/l
	return y