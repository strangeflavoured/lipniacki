import numpy as np
from scipy.integrate import solve_ivp as solve

from parameters import para
from model import model

def init(AB,AA,kv,nftot):

	##MODEL#############
	par=para(AB,AA,kv)
	f=model(par,0)

	##INITIAL VALUES####
	y0=np.zeros(14)
	y0[12]=nftot

	###INITIATION#######
	tspan=[0,60*60*101]

	sol=solve(f,tspan,y0,method='LSODA')

	return sol

def sim(AB,AA,kv,nftot,TR,y0,time):

	##MODEL#############
	par=para(AB,AA,kv)
	f=model(par,TR)

	###INITIATION#######
	tspan=[0,time]

	sol2=solve(f,tspan,y0,method='LSODA')

	return sol2