import matplotlib.pyplot as plt
import numpy as np 

import simulation as sim
import process as prc
import plot as p
##CONDITIONS########

AB=1                # AB=1 wt cell, AB=0  A20 deficient cell
AA=1                # AA=1 wt cell, AA=0 IkBa deficient cell
kv=5              	#ratio of cytoplasmic to nuclear volume kv=5
TR=0				#TNF signal
nftot=0.06			#total nfkb

###SIMULATION#######
sol=sim.init(AB,AA,kv,nftot)

###SIMULATION#######
y0=sol.y[:,-1]
sol2=sim.sim(AB,AA,kv,nftot,1,y0,60*60*24)

SOL=prc.fuse(sol,sol2)
pt=prc.hour(SOL[0])
py=SOL[1:-1]

p.figa(pt,py[6],'r','seaborn-dark',100,(0,24),'free nuclear NFkB','h','$\mu$M',False)