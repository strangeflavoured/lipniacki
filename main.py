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

###INITIATION#######
tspan=[0,60*60*101]

sol=solve(f,tspan,y0,method='LSODA')

###SIMULATION#######
TR=1
f=model(par,TR)

y0=sol.y[:,-1]
tspan=[0,60*60*24]

sol2=solve(f,tspan,y0,method='LSODA')

plt.style.use('seaborn-dark')
plt.plot(sol.t/3600-100,sol.y[6],'r')
plt.plot(sol2.t/3600+1,sol2.y[6],'r')
plt.xlim((0,6))

plt.tight_layout()
plt.show()