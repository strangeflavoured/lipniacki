import numpy as np
import model as mod
import process as prc
import results as res

def discrprogr(py):
	y=[]
	dy=[]
	for i in range(0,len(py)):
		if i==1:
			y.append(np.array(prc.discr(py[i],mod.limit1(i),mod.limitKO(i))))
		else:
			y.append(np.array(prc.discr(py[i],mod.limit1(i))))
	y=np.stack(y)

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

def analyse(path):
	restore=res.load(path)
	##print(restore.files)
	##pt=restore['pt']
	##if 'ptsim' in restore.keys():
	##	ptsim=restore['ptsim']

	py=restore['py']
	x,X=discrprogr(py)

	y=[]
	Y=[]
	if 'pysim' in restore.keys():
		pysim=restore['pysim']
		y,Y=discrprogr(pysim)	

	res.save('../../anres/results',x=x,X=X,y=y,Y=Y)
	res.dump('../../anres/results',x=x,X=X,y=y,Y=Y)

def show(path):
	rest=res.load(path)

	#X=rest['X']	
	#for i in range(0,len(X)):
	#	print(X[i])

	if 'Y' in rest.keys():
		Y=rest['Y']

		for i in range(0,len(Y)):
			print(Y[i])