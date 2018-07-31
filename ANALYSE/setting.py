import numpy as np
import model as mod
import process as prc
import results as res

def discr(py,**kwargs):
	mode=kwargs.get('mode','limit')
	y=[]
	for i in range(0,len(py)):
		if mode=='limit':
			if i==1:
				y.append(np.array(prc.discr(py[i],mod.limit1(i),mod.limitKO(i))))
			else:
				y.append(np.array(prc.discr(py[i],mod.limit1(i))))
		elif mode=='mean':
			if i==1:
				y.append(np.array(prc.discr(py[i],mod.meanpy(i)/2,mod.meanpy(i))))
			else:
				y.append(np.array(prc.discr(py[i],mod.meanpy(i))))
		elif mode =='half':
			if i==1:
				y.append(np.array(prc.discr(py[i],mod.meanpy(i)/2,(mod.limit0(i)+mod.limit1(i))/2)))
			else:
				y.append(np.array(prc.discr(py[i],(mod.limit0(i)+mod.limit1(i))/2)))
		elif mode=='hmean':
			if i==1:
				y.append(np.array(prc.discr(py[i],mod.meanpy(i)/2,(mod.limit0(i)+mod.meanpy(i))/2)))
			else:
				y.append(np.array(prc.discr(py[i],(mod.limit0(i)+mod.meanpy(i))/2)))
	y=np.stack(y)
	return y

def discrprogr(py,**kwargs):
	y=discr(py,**kwargs)

	dy=[]
	for i in range(0,len(y)):
		a=[]
		for j,k in enumerate(y[i]):
			if k<y[i,j-1]:
				a.append(-j)
			elif k>y[i,j-1]:
				a.append(j)
			else:
				a.append(0)
		dy.append(np.array(a))
	dy=np.stack(dy)

	x=[]
	X=[]
	for i in range(1,dy.shape[1]):
		ii=[]
		II=[]
		app=False
		for j in range(0,dy.shape[0]):
			if i==np.absolute(dy[j,i]):
				app=True
				if np.sign(dy[j,i])<0:
					strg='-'
					stg=-1
				elif np.sign(dy[j,i])>0:
					strg='+'
					stg=1
				ii.append('{}{}'.format(strg,j))
				II.append(int(stg*j))
		if app==True:
			x.append(ii)
			X.append(np.array(II))
	return(x,np.array(X))

def evaldiscr(py,**kwargs):
	y=discr(py,**kwargs)

	dy=[]
	for i in range(0,y.shape[0]):
		a=[]
		for j,k in enumerate(y[i]):
			if j==0:
				a.append(0)
			elif j!=0:
				if k<y[i,j-1]:
					a.append(-1)
				elif k>y[i,j-1]:
					a.append(1)
				else:
					a.append(0)
		dy.append(np.array(a))
	dy=np.stack(dy)

	DY=[np.zeros(dy.shape[0])]
	for i in range(0,dy.shape[1]):
		if np.any(dy[:,i]):
			DY.append(dy[:,i])
	DY=np.transpose(DY)
	return (dy,DY)

def analyse(path,**kwargs):
	restore=res.load(path)
	##print(restore.files)
	##pt=restore['pt']
	##if 'ptsim' in restore.keys():
	##	ptsim=restore['ptsim']

	py=restore['py']
	x,X=discrprogr(py,**kwargs)

	y=[]
	Y=[]
	if 'pysim' in restore.keys():
		pysim=restore['pysim']
		y,Y=discrprogr(pysim,**kwargs)	

	res.save('../../anres/anresults{}'.format(kwargs.get('mode','')),x=x,X=X,y=y,Y=Y)
	res.dump('../../anres/anresults{}'.format(kwargs.get('mode','')),x=x,X=X,y=y,Y=Y)

def evaluate(path,**kwargs):
	restore=res.load(path)
	##print(restore.files)
	##pt=restore['pt']
	##if 'ptsim' in restore.keys():
	##	ptsim=restore['ptsim']

	py=restore['py']
	dy,DY=evaldiscr(py,**kwargs)

	y=[]
	Y=[]
	if 'pysim' in restore.keys():
		pysim=restore['pysim']
		y,Y=evaldiscr(pysim,**kwargs)	

	res.save('../../anres/evresults{}'.format(kwargs.get('mode','')),dy=dy,DY=DY,y=y,Y=Y)
	res.dump('../../anres/evresults{}'.format(kwargs.get('mode','')),dy=dy,DY=DY,y=y,Y=Y)

def show(path):
	rest=res.load(path)

	#X=rest['X']	
	#for i in range(0,len(X)):
	#	print(X[i])

	if 'Y' in rest.keys():
		Y=rest['Y']

		for i in range(0,len(Y)):
			print(Y[i])