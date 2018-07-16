import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np 

import simulation as sim
import process as prc
import plot as p
import results as res
import colours as c
import model as mod
import setting as s

##CONDITIONS########
AA=1                # AA=1 wt cell, AA=0 IkBa deficient cell
AB=1                # AB=1 wt cell, AB=0  A20 deficient cell
AC=1				# AC=1 wt cell, AC=0 IKKa KO
kv=5              	#ratio of cytoplasmic to nuclear volume kv=5
TR=0				#TNF signal
nftot=0.06		   	#total nfkb

sol=s.solve(AA,AB,AC,kv,nftot)
pt=sol[0]
py=sol[1:sol.shape[0]]

#s.thresh(py,pt,'wt')
#s.normplt(py,pt)
#s.discreet(py,pt)

#px=[py[6]]
#py=[py[9]]
#colour=['r']
#colourmap=[cm.autumn]
#lab=['wt']
#p.phaseplt(px,py,colour,colourmap,lab,xlabel='NF$\kappa$B',ylabel='I$\kappa$B')

###SAVING###########
#res.dump('../results.npz',pt=pt,py=py)
#res.save('../steadystate.txt', tend=pt[-1], yend=py[:,-1])

#restore=res.load('../results.npz')
#print(restore.files)
#pt=restore['pt']
#py=restore['py']

###VARY kv##########
#itr=np.linspace(1,10,20)
#SUM=sim.varkv(AA,AB,AC,nftot,time=60*60*24,itr=itr,pvar=6)