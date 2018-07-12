import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np 

import simulation as sim
import process as prc
import plot as p
import results as res
import colours as c

##CONDITIONS########
AA=1                # AA=1 wt cell, AA=0 IkBa deficient cell
AB=1                # AB=1 wt cell, AB=0  A20 deficient cell
AC=1				# AC=1 wt cell, AC=0 IKKa KO
kv=5              	#ratio of cytoplasmic to nuclear volume kv=5
TR=0				#TNF signal
nftot=0.06		   	#total nfkb

###INITIATION#######
sol=sim.init(AA,AB,AC,kv,nftot)

###SIMULATION#######
TR=1
y0=sol.y[:,-1]
sol1=sim.sim(AA,AB,AC,kv,TR,y0,60*60*10000)

###PROCESSING#######
SOL=prc.fuse(sol.t,sol.y,sol1.t,sol1.y)
pt=prc.hour(SOL[0])
py=SOL[1:SOL.shape[0]]

###PLOTTING#########
#px=[py1[6],py2[6]]
#pt=[pt1,pt2]
#colour=[c.deepskyblue,'navy']
#label=['TNF=0','TNF=1']
#lstyle=['--','-']
#xlim=(-1,6)
#p.figa(pt,px,colour,label,101,xlim=xlim,title='NF$\kappa$B',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../resultsNF.png',DPI=500)

#px=[py[6]]
#py=[py[9]]
#colour=['r']
#colourmap=[cm.autumn]
#lab=['wt']
#p.phaseplt(px,py,colour,colourmap,lab,xlabel='NF$\kappa$B',ylabel='I$\kappa$B')

###SAVING###########
res.dump('../results.npz',pt=pt,py=py)
res.save('../steadystate.txt', tend=pt[-1], yend=py[:,-1])

#restore=res.load('../results.npz')
#print(restore.files)
#pt=restore['pt']
#py=restore['py']

###VARY kv##########
#itr=np.linspace(1,10,20)
#SUM=sim.varkv(AA,AB,AC,nftot,time=60*60*24,itr=itr,pvar=6)