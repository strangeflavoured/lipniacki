##########################################################################
##########################################################################
##                                                                       #
##   In this py-file one can introduce new parameters into the model,     #
##   also diffrent initial conditions and times characterictic for       #
##   simulation may be chosen.                                           #
##                                                                       #
##########################################################################
import numpy as np

############### Parametrisation for system of ODE's ####################
def para(AB,AA,nftot,kv): 
	#XXXXXXXXXXXXXXXXX A20 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                             
	c1=AB*0.00005/100     #AB*0.00005/100  inducible A20 mRNA synthesis, Assumption 
	c2=AB*0.000000        #AB*0.0  constitutive A20 mRNA synthesis, Assumption
	c3=0.0004             #0.0004  A20 mRNA degradation rate, Assumption 
	c4=0.005*100          #0.005*100  A20 translation rate, Assumption
	c5=0.0003             #0.0003  A20 degradation rate, IkBa *5
	 
	k1=0.0025             #0.0025 activation caused by TNF, FIT
	k2=0.1                #0.1  inactivation caused by A20, FIT
	k3=0.0015             #0.0015  spontanouous inactivation,  FIT
	kprod=0.000025        #0.000025  IKKn production rate
	kdeg1=0.000125        #0.000125  degradation of IKKa,IKKn and IKKi
	kdeg2=0.000125 
	kdeg3=0.000125 

	#XXXXXXXXXXXXXXXXXXX IkB alpha XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
	 
	a1=0.5                #0.5  IkBA*NFkB association  Hoff (short, correspond to i1) 
	a1n=0.5               #0.5  IkBA*NFkB association  Hoff (short, correspond to i1) 
	a2=0.2                #0.2  IKK*IkBa association  Fit
	a3=1.0                #1.0  IKK*(IkBa|NFkb) association  Fit
	t1=0.1                #0.1  degradation of (IKK|IkBa)  (any short)
	t2=0.1                #0.1  degradation of (IKK|IkBa|NFkB)  (any short)
	 
	c1a=AA*0.00005/100   #AA*0.00005/100  inducible (linear) IkBa mRNA synthesis FIT
	c2a=AA*0.000000      #AA*0.00000  constitutive mRNA IkBa synthesis  FIT 
	c3a=0.0004           #0.0004  mRNA IkBa degradation, FIT Blattner 22min i.e. 0.00075 
	c4a=0.005*100        #0.005*100   IkBa translation rate  FIT 
	c5a=0.0001           #0.0001  IkBa degradation rate, Pando
	c6a=0.00002          #0.00002 (IkBa|NFkB) degradation Hoff
	 
	i1=0.0025            #0.0025  NFkB nuclear import, Hoff blue (short correspond to a1)
	e2a=0.01             #0.01  (IkBa|NFkB) nuclear export, Hoff(any short) blue
	i1a=0.001            #0.001  IkBa nuclear import Hoff, FIT
	e1a=0.0005           #0.0005  IkBa nuclear export Hoff, FIT 

	par=np.array([kprod,kdeg1,k1,kdeg2,k3,kdeg3,a1,a1n,a2,a3,t1,t2,c6a,c5a,c1a,c3a,c4a,i1,e2a,i1a,e1a,c1,c3,c4,c5,k2,kv,c2,c2a])
	return par