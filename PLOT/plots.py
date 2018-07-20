import numpy as np

import process as prc
import plotset as ps
import colours as c
import model as mod

def thresh(py,pt,string):
	t=[pt,pt]
	xlim=(-1,6)
	lstyle=['-','--']

	###PLOTTING#########	
	px=[py[6],ps.hline(mod.limit1(6),pt)]
	colour=['navy','gray']
	label=[string,'$\\vartheta$']
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [$\mu$M]',label=True,path='../../graphics/NF'+string+'thresh.png',DPI=500)

	###PLOTTING#########
	px=[py[7],ps.hline(mod.limit1(7),pt)]
	colour=[c.darkorange,'gray']
	label=[string,'$\\vartheta$']
	ps.figa(t,px,colour,label,xlim=xlim,title='A20',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [$\mu$M]',label=True,path='../../graphics/A20'+string+'thresh.png',DPI=500)

	###PLOTTING#########
	px=[py[12],ps.hline(mod.limit1(12),pt)]
	colour=[c.green,'gray']
	label=[string,'$\\vartheta$']
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B:I$\kappa$B',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [$\mu$M]',label=True,path='../../graphics/IkB'+string+'thresh.png',DPI=500)

	###PLOTTING#########
	t.append(pt)
	px=[py[1],ps.hline(mod.limit1(1),pt),ps.hline(mod.limitKO(1),pt)]
	colour=[c.maroon,'gray','gray']
	label=[string,'$\\vartheta_1$','$\\vartheta_2$']
	lstyle.append('-.')
	ps.figa(t,px,colour,label,xlim=xlim,title='IKKa',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [$\mu$M]',label=True,path='../../graphics/IKK'+string+'thresh.png',DPI=500)

def normplt(py,pt,*string):
	t=[pt,pt,pt,pt]
	px=[prc.norm(py[6]),prc.norm(py[1]),prc.norm(py[7]),prc.norm(py[12])]
	colour=['navy',c.maroon,c.darkorange,c.green]
	label=['NF$\kappa$B','IKKa','A20','NF$\kappa$B:I$\kappa$B']
	lstyle=['-','-','-','-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,xlim=xlim,title=string,linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [a.u.]',label=True,path='../../graphics/normalised.png',DPI=500)

def discreet(py,pt,*string):
	t=[pt,pt,pt,pt]
	px=[prc.discr(py[6],mod.limit1(6)),prc.discr(py[1],mod.limit1(1),mod.limitKO(1)),prc.discr(py[7],mod.limit1(7)),prc.discr(py[12],mod.limit1(12))]
	colour=['navy',c.maroon,c.darkorange,c.green]
	label=['NF$\kappa$B','IKKa','A20','NF$\kappa$B:I$\kappa$B']
	lstyle=['-','-','-','-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,xlim=xlim,title=string,linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [a.u.]',label=True,path='../../graphics/discreet.png',DPI=500)

def discrall(py,pt,*string):
	t=[pt]
	xlim=(-1,6)
	lstyle=['-']

	px=[prc.discr(py[6],mod.limit1(6))]
	colour=['navy']
	label=['NF$\kappa$B']
	ps.figa(t,px,colour,label,xlim=xlim,title=string,linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [a.u.]',label=True,path='../../graphics/NFdiscreet.png',DPI=500)	

	px=[prc.discr(py[1],mod.limit1(1),mod.limitKO(1))]
	colour=[c.maroon]
	label=['IKKa']
	ps.figa(t,px,colour,label,xlim=xlim,title=string,linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [a.u.]',label=True,path='../../graphics/IKKdiscreet.png',DPI=500)

	px=[prc.discr(py[7],mod.limit1(7))]
	colour=[c.darkorange]
	label=['A20']
	ps.figa(t,px,colour,label,xlim=xlim,title=string,linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [a.u.]',label=True,path='../../graphics/A20discreet.png',DPI=500)

	px=[prc.discr(py[12],mod.limit1(12))]
	colour=[c.green]
	label=['NF$\kappa$B:I$\kappa$B']
	ps.figa(t,px,colour,label,xlim=xlim,title=string,linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [a.u.]',label=True,path='../../graphics/IkBdiscreet.png',DPI=500)

def discreetmean(py,pt,*string):
	t=[pt,pt,pt,pt]
	px=[prc.discr(py[6],np.mean(py[6])),prc.discr(py[1],np.mean(py[1])),prc.discr(py[7],np.mean(py[7])),prc.discr(py[12],np.mean(py[12]))]
	colour=['navy',c.maroon,c.darkorange,c.green]
	label=['NF$\kappa$B','IKKa','A20','NF$\kappa$B:I$\kappa$B']
	lstyle=['-','-','-','-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,xlim=xlim,title=string,linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [a.u.]',label=True,path='../../graphics/discreetmean.png',DPI=500)	

def discreetmedian(py,pt,*string):
	t=[pt,pt,pt,pt]
	px=[prc.discr(py[6],np.median(py[6])),prc.discr(py[1],np.median(py[1])),prc.discr(py[7],np.median(py[7])),prc.discr(py[12],np.median(py[12]))]
	colour=['navy',c.maroon,c.darkorange,c.green]
	label=['NF$\kappa$B','IKKa','A20','NF$\kappa$B:I$\kappa$B']
	lstyle=['-','-','-','-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,xlim=xlim,title=string,linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [a.u.]',label=True,path='../../graphics/discreetmedian.png',DPI=500)	

def threshmean(py,pt,string):
	t=[pt,pt]
	xlim=(-1,6)
	lstyle=['-','--']
	label=[string,'$\\vartheta$']

	###PLOTTING#########
	px=[py[6],ps.hline(np.mean(py[6]),pt)]
	colour=['navy','gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [$\mu$M]',label=True,path='../../graphics/NF'+string+'threshmean.png',DPI=500)

	###PLOTTING#########
	px=[py[1],ps.hline(np.mean(py[1]),pt)]
	colour=[c.maroon,'gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='IKKa',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [$\mu$M]',label=True,path='../../graphics/IKK'+string+'threshmean.png',DPI=500)

	###PLOTTING#########
	px=[py[7],ps.hline(np.mean(py[7]),pt)]
	colour=[c.darkorange,'gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='A20',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [$\mu$M]',label=True,path='../../graphics/A20'+string+'threshmean.png',DPI=500)

	###PLOTTING#########
	px=[py[12],ps.hline(np.mean(py[12]),pt)]
	colour=[c.green,'gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B:I$\kappa$B',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [$\mu$M]',label=True,path='../../graphics/IkB'+string+'threshmean.png',DPI=500)

def threshmedian(py,pt,string):	
	t=[pt,pt]
	xlim=(-1,6)
	lstyle=['-','--']
	label=[string,'$\\vartheta$']
	
	###PLOTTING#########	
	px=[py[6],ps.hline(np.median(py[6]),pt)]
	colour=['navy','gray']	
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [$\mu$M]',label=True,path='../../graphics/NF'+string+'threshmedian.png',DPI=500)

	###PLOTTING#########
	px=[py[1],ps.hline(np.median(py[1]),pt)]
	colour=[c.maroon,'gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='IKKa',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [$\mu$M]',label=True,path='../../graphics/IKK'+string+'threshmedian.png',DPI=500)

	###PLOTTING#########
	px=[py[7],ps.hline(np.median(py[7]),pt)]
	colour=[c.darkorange,'gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='A20',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [$\mu$M]',label=True,path='../../graphics/A20'+string+'threshmedian.png',DPI=500)

	###PLOTTING#########
	px=[py[12],ps.hline(np.median(py[12]),pt)]
	colour=[c.green,'gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B:I$\kappa$B',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [$\mu$M]',label=True,path='../../graphics/IkB'+string+'threshmedian.png',DPI=500)	

def discrnor(py,pt):
	t=[pt,pt,pt]
	xlim=(-1,6)
	label=['Normalisation','Discretisation','$\\vartheta$']
	lstyle=['-','--','-.']

	m=mod.limit1(6)/np.amax(py[6])
	px=[prc.norm(py[6]),prc.discr(py[6],mod.limit1(6)),ps.hline(m,pt)]
	colour=['navy','b','gray']	
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [a.u.]',label=True,path='../../graphics/NFdiscrnor.png',DPI=500)	
	
	m=mod.limit1(7)/np.amax(py[7])	
	px=[prc.norm(py[7]),prc.discr(py[7],mod.limit1(7)),ps.hline(m,pt)]
	colour=[c.darkorange,c.gold,'gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='A20',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [a.u.]',label=True,path='../../graphics/A20discrnor.png',DPI=500)
	
	m=mod.limit1(12)/np.amax(py[12])
	px=[prc.norm(py[12]),prc.discr(py[12],mod.limit1(12)),ps.hline(m,pt)]
	colour=[c.green,c.limegreen,'gray']	
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B:I$\kappa$B',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [a.u.]',label=True,path='../../graphics/IkBdiscrnor.png',DPI=500)

	m=mod.limit1(1)/np.amax(py[1])
	n=mod.limitKO(1)/np.amax(py[1])
	lstyle.append(':')
	t.append(pt)
	label.append('$\\vartheta_2$')
	px=[prc.norm(py[1]),prc.discr(py[1],mod.limit1(1),mod.limitKO(1)),ps.hline(m,pt),ps.hline(n,pt)]
	colour=[c.maroon,'r','gray','gray']		
	ps.figa(t,px,colour,label,xlim=xlim,title='IKKa',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [a.u.]',label=True,path='../../graphics/IKKdiscrnor.png')