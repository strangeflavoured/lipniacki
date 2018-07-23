import matplotlib.pyplot as plt
import numpy as np 

import simulation as sim
import results as res

##CONDITIONS########
AA=1                # AA=1 wt cell, AA=0 IkBa deficient cell
AB=1                # AB=1 wt cell, AB=0  A20 deficient cell
AC=1				# AC=1 wt cell, AC=0 IKKa KO
kv=5              	#ratio of cytoplasmic to nuclear volume kv=5
#TR=0				#TNF signal
nftot=0.06		   	#total nfkb

sol=sim.solve(AA,AB,AC,kv,nftot)#kwargs: TR, t
pt=sol[0]
py=sol[1]
sol1=sol[2]

###VARY kv##########
#itr=np.linspace(1,10,20)
#SUM=sim.varkv(AA,AB,AC,nftot,time=60*60*24,itr=itr,pvar=6)

###SAVING###########
res.dump('../../simres/results',pt=pt,py=py)#,ptsim=sol1.t,pysim=sol1.y)
#res.save('../../simres/steadystate', mode='wt',tend=pt[-1]-101, yend=py[:,-1])
