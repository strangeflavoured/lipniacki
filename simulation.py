import numpy as np
from scipy.integrate import solve_ivp as solve

from parameters import para
from model import model

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