import numpy as np

def norm(x):
	m=np.amax(x)
	nx=x
	for i in range(0,len(x)):
		nx[i]=nx[i]/m
	return nx

def discr(x,*thresh):#thresh increasing
	l=len(thresh)
	lx=len(x)
	diy=np.zeros((lx,))
	for i in range(0,lx):
		for j,k in enumerate(thresh):
			if x[i]<k:
				diy[i]=j/l
				break
			elif x[i]==k:
				diy[i]=j/l+1/(2*l)
				break
			else:
				diy[i]=(j+1)/l
	return diy