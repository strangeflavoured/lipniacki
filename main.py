import matplotlib.pyplot as plt
import numpy as np 

import simulation as sim
import process as prc
import plot as p
##CONDITIONS########

AA=1                # AA=1 wt cell, AA=0 IkBa deficient cell
AB=1                # AB=1 wt cell, AB=0  A20 deficient cell
AC=1				# AC=1 wt cell, AC=0 IKKa KO
kv=5              	#ratio of cytoplasmic to nuclear volume kv=5
TR=0				#TNF signal
nftot=0.06			#total nfkb

###SIMULATION#######
sol=sim.init(AA,AB,AC,kv,nftot)

###SIMULATION#######
TR=1
y0=sol.y[:,-1]
sol2=sim.sim(AA,AB,AC,kv,TR,y0,60*60*2)

###SIMULATION#######
y0=sol2.y[:,-1]
y0[1]=0
print(y0)
sol3=sim.sim(AA,AB,0,kv,TR,y0,60*60*5)

SOL=prc.fuse(sol.t,sol.y,sol2.t,sol2.y)
pt=SOL[0]
py=SOL[1:SOL.shape[0]]

SOL2=prc.fuse(pt,py,sol3.t,sol3.y)
pt=prc.hour(SOL2[0])
py=SOL2[1:SOL2.shape[0]]

px=[py[6],py[1]]
colour=['r','g']
label=['NF$\kappa$B','IKK']
xlim=(-1,7)
p.figa(pt,px,colour,label,'seaborn-dark',101,xlim,'','h','$\mu$M',False)