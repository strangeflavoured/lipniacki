import numpy as np
import matplotlib.pyplot as plt

import process as prc
import plotset as ps
import colours as c
import model as mod

def plainall(pt,py,*string):
	if string:
		strg=string[0]
	else:
		strg=''
	###PLOTTING#########
	t=[pt,pt]
	px=[py[6],py[5]]
	colour=['navy','b']
	label=['nuclear','cytoplasmic']
	lstyle=['-','--']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../../graphics/NF'+strg+'.png',DPI=500)

	###PLOTTING#########
	t=[pt]
	px=[py[1]]
	colour=[c.blood]
	label=[strg]
	lstyle=['-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,xlim=xlim,title='IKKa',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=False,path='../../graphics/IKK'+strg+'.png',DPI=500)

	###PLOTTING#########
	t=[pt]
	px=[py[7]]
	colour=[c.darkorange]
	label=[strg]
	lstyle=['-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,xlim=xlim,title='A20',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=False,path='../../graphics/A20'+strg+'.png',DPI=500)

	###PLOTTING#########
	t=[pt,pt]
	px=[py[12],py[13]]
	colour=[c.green,c.lime]
	label=['cytoplasmic','nuclear']
	lstyle=['-','--']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B:I$\kappa$B',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../../graphics/IkB'+strg+'.png',DPI=500)

	###PLOTTING#########
	t=[pt,pt]
	px=[py[11],py[8]]
	colour=[c.maroon,c.steelblue]
	label=['I$\kappa$B','A20']
	lstyle=['--',':']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,xlim=xlim,title='Transcripts',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../../graphics/RNA'+strg+'.png',DPI=500)

def thresh(py,pt,string):	
	###PLOTTING#########
	t=[pt,pt]
	xlim=(-1,6)
	lstyle=['-','--']
	label=[string,'$\\vartheta$']

	###PLOTTING#########	
	px=[py[6],ps.hline(mod.limit1(6),pt)]
	colour=['navy','gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [$\mu$M]',label=True,path='../../graphics/NF'+string+'thresh.png',DPI=500)

	###PLOTTING#########
	px=[py[7],ps.hline(mod.limit1(7),pt)]
	colour=[c.darkorange,'gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='A20',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [$\mu$M]',label=True,path='../../graphics/A20'+string+'thresh.png',DPI=500)

	###PLOTTING#########
	px=[py[12],ps.hline(mod.limit1(12),pt)]
	colour=[c.green,'gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B:I$\kappa$B',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [$\mu$M]',label=True,path='../../graphics/IkB'+string+'thresh.png',DPI=500)

	###PLOTTING#########
	t.append(pt)
	label.append('$\\vartheta_2$')
	lstyle.append('-.')
	px=[py[1],ps.hline(mod.limit1(1),pt),ps.hline(mod.limitKO(1),pt)]
	colour=[c.blood,'gray','gray']	
	ps.figa(t,px,colour,label,xlim=xlim,title='IKKa',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [$\mu$M]',label=True,path='../../graphics/IKK'+string+'thresh.png',DPI=500)

def normplt(py,pt,*string):
	t=[pt,pt,pt,pt]
	px=[prc.norm(py[6]),prc.norm(py[1]),prc.norm(py[7]),prc.norm(py[12])]
	colour=['navy',c.blood,c.darkorange,c.green]
	label=['NF$\kappa$B','IKKa','A20','NF$\kappa$B:I$\kappa$B']
	lstyle=['-','-','-','-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,xlim=xlim,title=string,linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [a.u.]',label=True,path='../../graphics/normalised.png',DPI=500)

def discreet(py,pt,*string):
	t=[pt,pt,pt,pt]
	px=[prc.discr(py[6],mod.limit1(6)),prc.discr(py[1],mod.limit1(1),mod.limitKO(1)),prc.discr(py[7],mod.limit1(7)),prc.discr(py[12],mod.limit1(12))]
	colour=['navy',c.blood,c.darkorange,c.green]
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
	colour=[c.blood]
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
	colour=['navy',c.blood,c.darkorange,c.green]
	label=['NF$\kappa$B','IKKa','A20','NF$\kappa$B:I$\kappa$B']
	lstyle=['-','-','-','-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,xlim=xlim,title=string,linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [a.u.]',label=True,path='../../graphics/discreetmean.png',DPI=500)	

def discreetmedian(py,pt,*string):
	t=[pt,pt,pt,pt]
	px=[prc.discr(py[6],np.median(py[6])),prc.discr(py[1],np.median(py[1])),prc.discr(py[7],np.median(py[7])),prc.discr(py[12],np.median(py[12]))]
	colour=['navy',c.blood,c.darkorange,c.green]
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
	colour=[c.blood,'gray']
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
	colour=[c.blood,'gray']
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
	px=[prc.norm(py[6]),prc.discr(py[6],m),ps.hline(m,pt)]
	colour=['navy',c.dodgerblue,'gray']	
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [a.u.]',label=True,path='../../graphics/NFdiscrnor.png',DPI=500)	
	
	m=mod.limit1(7)/np.amax(py[7])	
	px=[prc.norm(py[7]),prc.discr(py[7],m),ps.hline(m,pt)]
	colour=[c.darkorange,c.yellow,'gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='A20',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [a.u.]',label=True,path='../../graphics/A20discrnor.png',DPI=500)
	
	m=mod.limit1(12)/np.amax(py[12])
	px=[prc.norm(py[12]),prc.discr(py[12],m),ps.hline(m,pt)]
	colour=[c.green,c.lime,'gray']	
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B:I$\kappa$B',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [a.u.]',label=True,path='../../graphics/IkBdiscrnor.png',DPI=500)

	m=mod.limit1(1)/np.amax(py[1])
	n=mod.limitKO(1)/np.amax(py[1])
	lstyle.append(':')
	t.append(pt)
	label.append('$\\vartheta_2$')
	px=[prc.norm(py[1]),prc.discr(py[1],m,n),ps.hline(m,pt),ps.hline(n,pt)]
	colour=[c.blood,'r','gray','gray']		
	ps.figa(t,px,colour,label,xlim=xlim,title='IKKa',linestyle=lstyle,xlabel='t$\\ /\\ $[h]',ylabel='c$\\ / \\ $ [a.u.]',label=True,path='../../graphics/IKKdiscrnor.png')

def evplt(dy,DY):
	dt=np.arange(dy.shape[1])
	DT=np.arange(DY.shape[1])

	plt.style.use('seaborn-darkgrid')
	plt.plot(dt,dy[1],'-',c=c.blood,label='IKKa')
	plt.plot(dt,dy[6],'--',c=c.navy,label='NF$\kappa$B')
	plt.plot(dt,dy[7],'-.',c=c.darkorange,label='A20')
	plt.plot(dt,dy[12],':',c=c.green,label='NF$\kappa$B:I$\kappa$B')
	plt.legend()
	plt.xlim(0,4000)
	plt.ylabel('change d')
	plt.xlabel('time steps')
	plt.tight_layout()
	plt.savefig('../../graphics/evplttimend.png',dpi=500)
	plt.close()

	plt.style.use('seaborn-darkgrid')
	plt.plot(DT,DY[1],'-',c=c.blood,label='IKKa')
	plt.plot(DT,DY[6],'--',c=c.navy,label='NF$\kappa$B')
	plt.plot(DT,DY[7],'-.',c=c.darkorange,label='A20')
	plt.plot(DT,DY[12],':',c=c.green,label='NF$\kappa$B:I$\kappa$B')
	plt.legend()
	plt.xlim(0,85)
	plt.ylabel('change d')
	plt.xlabel('time steps')
	plt.tight_layout()
	plt.savefig('../../graphics/evpltscale.png',dpi=500)
	plt.close()