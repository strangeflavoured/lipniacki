import matplotlib.pyplot as plt
import numpy as np 
from scipy.integrate import solve_ivp as solve

from parameters import para
from model import model

##CONDITIONS########

AB=1                # AB=1 wt cell, AB=0  A20 deficient cell
AA=1                # AA=1 wt cell, AA=0 IkBa deficient cell
kv=5              	#ratio of cytoplasmic to nuclear volume kv=5
TR=0				#TNF signal
nftot=0.06			#total nfkb

##MODEL#############

par=para(AB,AA,kv)
f=model(par,TR)

##INITIAL VALUES####

y0=np.zeros(14)
y0[12]=nftot

###SIMULATION#######
tspan=[0,60*60*24]

sol=solve(f,tspan,y0,method='LSODA')

plt.plot(sol.t,sol.y[6])
plt.show()