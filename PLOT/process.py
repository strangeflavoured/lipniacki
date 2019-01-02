import numpy as np
import model as mod

def norm(x):
	m=np.amax(x)	
	nx=x
	if m!=0:
		for i in range(0,len(x)):
			nx[i]=nx[i]/m
	else:
		nx=np.zeros(len(x))
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

def evmode(mode):
	if mode=='limit':
		m6=mod.limit1(6)/mod.pymax(6)
		m7=mod.limit1(7)/mod.pymax(7)
		m12=mod.limit1(12)/mod.pymax(12)
		m1=mod.limit1(1)/mod.pymax(1)
		n1=mod.limitKO(1)/mod.pymax(1)
	elif mode=='mean6':
		m6=mod.meanpy(6)/mod.pymax(6)
		m7=mod.meanpy(7)/mod.pymax(7)
		m12=mod.meanpy(12)/mod.pymax(12)
		n1=mod.meanKO(1)/mod.pymax(1)
		m1=mod.meanpy(1)/mod.pymax(1)
	elif mode=='mean24':
		m6=mod.mean24(6)/mod.pymax(6)
		m7=mod.mean24(7)/mod.pymax(7)
		m12=mod.mean24(12)/mod.pymax(12)
		n1=mod.mean24KO(1)/mod.pymax(1)
		m1=mod.mean24(1)/mod.pymax(1)
	elif mode=='median':
		m6=mod.median(6)/mod.pymax(6)
		m7=mod.median(7)/mod.pymax(7)
		m12=mod.median(12)/mod.pymax(12)
		n1=mod.medianKO(1)/mod.pymax(1)
		m1=mod.median(1)/mod.pymax(1)
	elif mode=='hlim':
		m6=(mod.limit0(6)+mod.limit1(6))/(2*mod.pymax(6))
		m7=(mod.limit0(7)+mod.limit1(7))/(2*mod.pymax(7))
		m12=(mod.limit0(12)+mod.limit1(12))/(2*mod.pymax(12))
		m1=(mod.limit0(1)+mod.limit1(1))/(2*mod.pymax(1))
		n1=(mod.limit0(1)+mod.limitKO(1))/(2*mod.pymax(1))
	elif mode=='hmean6':
		m6=(mod.limit0(6)+mod.meanpy(6))/(2*mod.pymax(6))
		m7=(mod.limit0(7)+mod.meanpy(7))/(2*mod.pymax(7))
		m12=(mod.limit0(12)+mod.meanpy(12))/(2*mod.pymax(12))
		m1=(mod.limit0(1)+mod.meanpy(1))/(2*mod.pymax(1))
		n1=(mod.limit0(1)+mod.meanKO(1))/(2*mod.pymax(1))
	elif mode=='hmean24':
		m6=(mod.limit0(6)+mod.mean24(6))/(2*mod.pymax(6))
		m7=(mod.limit0(7)+mod.mean24(7))/(2*mod.pymax(7))
		m12=(mod.limit0(12)+mod.mean24(12))/(2*mod.pymax(12))
		m1=(mod.limit0(1)+mod.mean24(1))/(2*mod.pymax(1))
		n1=(mod.limit0(1)+mod.mean24KO(1))/(2*mod.pymax(1))
	elif mode=='hmax':
		m6=(mod.limit0(6)+mod.pymax(6))/(2*mod.pymax(6))
		m7=(mod.limit0(7)+mod.pymax(7))/(2*mod.pymax(7))
		m12=(mod.limit0(12)+mod.pymax(12))/(2*mod.pymax(12))
		m1=(mod.limit0(1)+mod.pymax(1))/(4*mod.pymax(1))
		n1=(mod.limit0(1)+mod.pymax(1))/(2*mod.pymax(1))
	elif mode=='custom':
		m6=mod.mean24(6)/mod.pymax(6)
		m7=(mod.limit0(7)/(2*mod.pymax(7))+0.5)
		m12=mod.mean24(12)/mod.pymax(12)
		m1=(mod.limit0(1)+mod.limit1(1))/(2*mod.pymax(1))
		n1=(mod.limit0(1)+mod.limitKO(1))/(2*mod.pymax(1))
	elif mode=='custom2':
		m6=mod.mean24(6)/mod.pymax(6)
		m7=(mod.limit0(7)+mod.limit1(7))/(2*mod.pymax(7))
		m12=mod.mean24(12)/mod.pymax(12)
		m1=(mod.limit0(1)+mod.limit1(1))/(2*mod.pymax(1))
		n1=mod.mean24(1)/mod.pymax(1)
	return (m6,m7,m12,m1,n1)

def ceem(arr):
	#removes empty element indices
	d=arr.copy()
	i=0
	while i<d.shape[1]:
		if not d[:,i].any():
			d=np.delete(d,i,1)
			i-=1
		i+=1
	return d

def insee(arr):
	#inserts empty element index after every index
	v=arr.copy()
	i=0
	while i<=v.shape[1]:
		v=np.insert(v,i,0,axis=1)
		i+=2
	return v