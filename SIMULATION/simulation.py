import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from parameters import para
from model import model
import process as prc

def init(AA,AB,AC,kv,nftot):

	##MODEL#############
	par=para(AA,AB,AC,kv)
	f=model(par,0)

	##INITIAL VALUES####
	y0=np.zeros(14)
	y0[12]=nftot

	###INITIATION#######
	tspan=[0,60*60*101]

	sol=solve_ivp(f,tspan,y0,method='LSODA')

	return sol

def sim(AA,AB,AC,kv,TR,y0,time):

	##MODEL#############
	par=para(AA,AB,AC,kv)
	f=model(par,TR)

	###INITIATION#######
	tspan=[0,time]

	sol2=solve_ivp(f,tspan,y0,method='LSODA')

	return sol2

def varkv(AA,AB,AC,nftot,time,itr,pvar):
	SUM=[]
	colour=cm.autumn_r(np.linspace(0,1,len(itr)))
	plt.style.use('seaborn-dark')
	fig,ax=plt.subplots(nrows=1,ncols=1)
	for i,kv in enumerate(itr):
		###INITIATION#######
		TR=0
		sol=init(AA,AB,AC,kv,nftot)

		###SIMULATION#######
		TR=1
		y0=sol.y[:,-1]
		sol2=sim(AA,AB,AC,kv,TR,y0,time)

		###PROCESSING#######
		SOL=prc.fuse(sol.t,sol.y,sol2.t,sol2.y)
		SUM.append(SOL)
		pt=prc.hour(SOL[0])
		
		py=SOL[1:SOL.shape[0]]		
		ax.plot(pt-100,py[pvar],label='kv={}'.format(np.around(kv,1)),c=colour[i])
	ax.set_xlim(0,pt[-1]-100)
	ax.set_xlabel('t/h')
	ax.set_ylabel('NF$\kappa$B/$\mu$M')
	fig.suptitle('Variation of nuclear Volume')
	ax.legend()
	ax.grid()
	fig.tight_layout()
	plt.show()
	return SUM

def solve(AA,AB,AC,kv,nftot,**kwargs):
	tspan=kwargs.get('t',60*60*24)
	TR=kwargs.get('TR',1)
	###INITIATION#######
	sol=init(AA,AB,AC,kv,nftot)

	###SIMULATION#######
	y0=sol.y[:,-1]
	sol1=sim(AA,AB,AC,kv,TR,y0,tspan)

	###PROCESSING#######
	SOL=prc.fuse(sol.t,sol.y,sol1.t,sol1.y)
	pt=prc.hour(SOL[0])
	py=SOL[1:SOL.shape[0]]
	return np.vstack((pt,py))