import numpy as np

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