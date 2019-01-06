import matplotlib.pyplot as plt
import numpy as np 

import simulation as sim
import results as res

def timevar(stop):
	sol=sim.solve(AA,AB,AC,kv,nftot,t=60*60*stop)

	RET=[[],[],[]]	
	for i,j in enumerate(sol[2].t):
		RET[0].append([j/3600,np.mean(sol[2].y[1,:i+1]),np.mean(sol[2].y[6,:i+1]),np.mean(sol[2].y[7,:i+1]),np.mean(sol[2].y[12,:i+1])])
		RET[1].append([j/3600,np.median(sol[2].y[1,:i+1]),np.median(sol[2].y[6,:i+1]),np.median(sol[2].y[7,:i+1]),np.median(sol[2].y[12,:i+1])])
		RET[2].append([j/3600,np.amax(sol[2].y[1,:i+1]),np.amax(sol[2].y[6,:i+1]),np.amax(sol[2].y[7,:i+1]),np.amin(sol[2].y[12,:i+1])])
	RET[0]=np.transpose(RET[0])
	RET[1]=np.transpose(RET[1])
	RET[2]=np.transpose(RET[2])
	return RET

##CONDITIONS########
AA=1                # AA=1 wt cell, AA=0 IkBa deficient cell
AB=1                # AB=1 wt cell, AB=0  A20 deficient cell
AC=1				# AC=1 wt cell, AC=0 IKKa KO
kv=5              	#ratio of cytoplasmic to nuclear volume kv=5
#TR=0				#TNF signal
nftot=0.06		   	#total nfkb

#VAR=timevar(24)#np.logspace(0,np.log2(24),20,base=2))
#res.dump('../../simres/VARthreshwt',mean=VAR[0],median=VAR[1],max=VAR[2])

'''sol=sim.solve(AA,AB,AC,kv,nftot,t=60*60*24,TR=1)
for i,j in enumerate(sol[2].y):
	if i==12:
		print(np.amax(j[100:]))
	else:
		print(np.amax(j))'''
		
sol=sim.solve(AA,AB,AC,kv,nftot,t=60*60*24)#kwargs: TR, t
pt=sol[0]
py=sol[1]
sol1=sol[2]
t0=sol[3]

###VARY kv##########
#itr=np.linspace(1,10,20)
#SUM=sim.varkv(AA,AB,AC,nftot,time=60*60*24,itr=itr,pvar=6)

###SAVING###########
res.dump('../../simres/resultswt',pt=pt,py=py,ptsim=sol1.t,pysim=sol1.y,t0=t0)
res.save('../../simres/steadystatewt', mode='wt',tend=pt[-1]-101, yend=py[:,-1],t0=t0)
#print(np.median(sol[2].y[1,:]),np.median(sol[2].y[6,:]),np.median(sol[2].y[7,:]),np.median(sol[2].y[12,:]))#KNAI