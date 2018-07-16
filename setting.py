import numpy as np

import simulation as sim
import process as prc
import plot as p
import results as res
import colours as c
import model as mod

def solve(AA,AB,AC,kv,nftot):
	###INITIATION#######
	TR=0
	sol=sim.init(AA,AB,AC,kv,nftot)

	###SIMULATION#######
	TR=1
	y0=sol.y[:,-1]
	sol1=sim.sim(AA,AB,AC,kv,TR,y0,60*60*24)

	###PROCESSING#######
	SOL=prc.fuse(sol.t,sol.y,sol1.t,sol1.y)
	pt=prc.hour(SOL[0])
	py=SOL[1:SOL.shape[0]]
	return np.vstack((pt,py))

def thresh(py,t,string):	
	###PLOTTING#########
	pt=[t,t]
	px=[py[6],p.hline(mod.limit1(6),t)]
	colour=['navy','gray']
	label=[string,'$\delta$']
	lstyle=['-','--']
	xlim=(-1,6)
	p.figa(pt,px,colour,label,101,xlim=xlim,title='NF$\kappa$B',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../NF'+string+'thresh.png',DPI=500)

	###PLOTTING#########
	pt=[t,t,t]
	px=[py[1],p.hline(mod.limit1(1),t),p.hline(mod.limitKO(1),t)]
	colour=[c.maroon,'gray','gray']
	label=[string,'$\delta_1$','$\delta_2$']
	lstyle=['-','--','-.']
	xlim=(-1,6)
	p.figa(pt,px,colour,label,101,xlim=xlim,title='IKKa',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../IKK'+string+'thresh.png',DPI=500)

	###PLOTTING#########
	pt=[t,t]
	px=[py[7],p.hline(mod.limit1(7),t)]
	colour=[c.darkorange,'gray']
	label=[string,'$\delta$']
	lstyle=['-','--']
	xlim=(-1,6)
	p.figa(pt,px,colour,label,101,xlim=xlim,title='A20',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../A20'+string+'thresh.png',DPI=500)

	###PLOTTING#########
	pt=[t,t]
	px=[py[12],p.hline(mod.limit1(12),t)]
	colour=[c.green,'gray']
	label=[string,'$\delta$']
	lstyle=['-','--']
	xlim=(-1,6)
	p.figa(pt,px,colour,label,101,xlim=xlim,title='NF$\kappa$B:I$\kappa$B',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../IkB'+string+'thresh.png',DPI=500)

def normplt(py,pt,*string):
	t=[pt,pt,pt,pt]
	px=[prc.norm(py[6]),prc.norm(py[1]),prc.norm(py[7]),prc.norm(py[12])]
	colour=['navy',c.maroon,c.darkorange,c.green]
	label=['NF$\kappa$B','IKKa','A20','NF$\kappa$B:I$\kappa$B']
	lstyle=['-','-','-','-']
	xlim=(-1,6)
	p.figa(t,px,colour,label,101,xlim=xlim,title=string,linestyle=lstyle,xlabel='h',ylabel='a.u.',label=True,path='../normalised.png',DPI=500)

def discreet(py,pt,*string):
	t=[pt,pt,pt,pt]
	px=[prc.discr(py[6],mod.limit1(6)),prc.discr(py[1],mod.limit1(1)),prc.discr(py[7],mod.limit1(7)),prc.discr(py[12],mod.limit1(12))]
	colour=['navy',c.maroon,c.darkorange,c.green]
	label=['NF$\kappa$B','IKKa','A20','NF$\kappa$B:I$\kappa$B']
	lstyle=['-','-','-','-']
	xlim=(-1,6)
	p.figa(t,px,colour,label,101,xlim=xlim,title=string,linestyle=lstyle,xlabel='h',ylabel='a.u.',label=True,path='../discreet.png',DPI=500)