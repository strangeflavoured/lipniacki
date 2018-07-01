import numpy as np
from scipy.integrate import solve_ivp as solve
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

	sol=solve(f,tspan,y0,method='LSODA')

	return sol

def sim(AA,AB,AC,kv,TR,y0,time):

	##MODEL#############
	par=para(AA,AB,AC,kv)
	f=model(par,TR)

	###INITIATION#######
	tspan=[0,time]

	sol2=solve(f,tspan,y0,method='LSODA')

	return sol2

def varkv(AA,AB,AC,kv,nftot,time,itr):
	SUM=[]
	#colour=cm.autumn(np.linspace(0,1,len(itr)))
	fig,ax=plt.subplots(nrows=1,ncols=1)
	plt.sytle.use('seaborn-dark')
	for kv in itr:
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
		ax.plot(pt-101,py[6])#,colour[kv])
	fig.tight_layout()
	plt.show()
	return SUM