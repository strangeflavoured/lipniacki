import matplotlib.pyplot as plt
import numpy as np 
from scipy.integrate import RK45 as solve

from parameters import para
from model import model

AB=1                # AB=1 wt cell, AB=0  A20 deficient cell
AA=1                 # AA=1 wt cell, AA=0 IkBa deficient cell
nftot=0.06			#total nfkb
kv=5              #ratio of cytoplasmic to nuclear volume kv=5
TR=0				#TNF signal

par=para(AB,AA,nftot,kv)

f=model(par,TR)

t0=0
tend=10
y0=np.zeros(14)

sol=solve(f,t0,y0,tend)

##OUTPUT###
#Traceback (most recent call last):
#  File "main.py", line 22, in <module>
#    sol=solve(f,t0,y0,tend)
#  File "/.local/lib/python3.6/site-packages/scipy/integrate/_ivp/rk.py", line 99, in __init__
#    self.f = self.fun(self.t, self.y)
#  File "/.local/lib/python3.6/site-packages/scipy/integrate/_ivp/base.py", line 139, in fun
#    return self.fun_single(t, y)
#  File "/.local/lib/python3.6/site-packages/scipy/integrate/_ivp/base.py", line 21, in fun_wrapped
#    return np.asarray(fun(t, y), dtype=dtype)
#  File "model.py", line 65, in mod
#    dy[0]= kprod - kdeg1*y[0] - TR*k1*y[0]              
#TypeError: 'int' object is not subscriptable

plt.plot(sol.t,sol.y[6])
plt.show()