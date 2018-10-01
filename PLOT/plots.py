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
	px=[py[6]]
	colour=['navy']
	label=[strg]
	lstyle=['-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B',linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ $\mu$M',label=False,path='../../graphics/NF'+strg+'.png',DPI=500)

	###PLOTTING#########
	t=[pt]
	px=[py[1]]
	colour=[c.blood]
	label=[strg]
	lstyle=['-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,xlim=xlim,title='IKKa',linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ $\mu$M',label=False,path='../../graphics/IKK'+strg+'.png',DPI=500)

	###PLOTTING#########
	t=[pt]
	px=[py[7]]
	colour=[c.darkorange]
	label=[strg]
	lstyle=['-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,xlim=xlim,title='A20',linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ $\mu$M',label=False,path='../../graphics/A20'+strg+'.png',DPI=500)

	###PLOTTING#########
	t=[pt,pt]
	px=[py[12]]
	colour=[c.green]
	label=[strg]
	lstyle=['-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B:I$\kappa$B',linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ $\mu$M',label=False,path='../../graphics/IkB'+strg+'.png',DPI=500)

	###PLOTTING#########
	#t=[pt,pt]
	#px=[py[11],py[8]]
	#colour=[c.maroon,c.steelblue]
	#label=['I$\kappa$B','A20']
	#lstyle=['--',':']
	#xlim=(-1,6)
	#ps.figa(t,px,colour,label,xlim=xlim,title='Transcripts',linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ $\mu$M',label=True,path='../../graphics/RNA'+strg+'.png',DPI=500)

def thresh(py,pt,string):	
	###PLOTTING#########
	t=[pt,pt]
	xlim=(-1,6)
	lstyle=['-','--']
	label=[string,'$\\vartheta$']

	###PLOTTING#########	
	px=[py[6],ps.hline(mod.limit1(6),pt)]
	colour=['navy','gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B',linestyle=lstyle,xlabel='t$\\ \/\\ $h',ylabel='c$\\ /\\$ $\\mu$M',label=True,path='../../graphics/NF'+string+'thresh.png',DPI=500)

	###PLOTTING#########
	px=[py[7],ps.hline(mod.limit1(7),pt)]
	colour=[c.darkorange,'gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='A20',linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ $\mu$M',label=True,path='../../graphics/A20'+string+'thresh.png',DPI=500)

	###PLOTTING#########
	px=[py[12],ps.hline(mod.limit1(12),pt)]
	colour=[c.green,'gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B:I$\kappa$B',linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ $\mu$M',label=True,path='../../graphics/IkB'+string+'thresh.png',DPI=500)

	###PLOTTING#########
	t.append(pt)
	label.append('$\\vartheta_2$')
	lstyle.append('-.')
	px=[py[1],ps.hline(mod.limit1(1),pt),ps.hline(mod.limitKO(1),pt)]
	colour=[c.blood,'gray','gray']	
	ps.figa(t,px,colour,label,xlim=xlim,title='IKKa',linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ $\mu$M',label=True,path='../../graphics/IKK'+string+'thresh.png',DPI=500)

def normplt(py,pt,*string):
	t=[pt,pt,pt,pt]
	px=[prc.norm(py[6]),prc.norm(py[1]),prc.norm(py[7]),prc.norm(py[12])]
	colour=['navy',c.blood,c.darkorange,c.green]
	label=['NF$\kappa$B','IKKa','A20','NF$\kappa$B:I$\kappa$B']
	lstyle=['-','-','-','-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,xlim=xlim,title=string,linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ a.u.',label=True,path='../../graphics/normalised.png',DPI=500)

def discreet(py,pt,*string,**kwargs):
	mode=kwargs.get('mode','limit')
	(m6,m7,m12,m1,n1)=prc.evmode(mode,py)
	t=[pt,pt,pt,pt]
	px=[prc.discr(py[1],m1,n1),prc.discr(py[6],m6),prc.discr(py[7],m7),prc.discr(py[12],m12)]
	colour=[c.blood,'navy',c.darkorange,c.green]
	label=['IKKa','NF$\kappa$B','A20','NF$\kappa$B:I$\kappa$B']
	lstyle=['-','--','-.',':']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,xlim=xlim,title=string,linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ a.u.',label=True,path='../../graphics/discreet{}.png'.format(kwargs.get('mode','')),DPI=500)

def discrall(py,pt,*string,**kwargs):	
	mode=kwargs.get('mode','limit')
	(m6,m7,m12,m1,n1)=prc.evmode(mode,py)
	t=[pt]
	xlim=(-1,6)
	lstyle=['-']

	px=[prc.discr(py[6],m6)]
	colour=['navy']
	label=['NF$\kappa$B']
	ps.figa(t,px,colour,label,xlim=xlim,title=string,linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ a.u.',label=True,path='../../graphics/NFdiscreet{}.png'.format(kwargs.get('mode','')),DPI=500)	

	px=[prc.discr(py[1],m1,n1)]
	colour=[c.blood]
	label=['IKKa']
	ps.figa(t,px,colour,label,xlim=xlim,title=string,linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ a.u.',label=True,path='../../graphics/IKKdiscreet{}.png'.format(kwargs.get('mode','')),DPI=500)

	px=[prc.discr(py[7],m7)]
	colour=[c.darkorange]
	label=['A20']
	ps.figa(t,px,colour,label,xlim=xlim,title=string,linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ a.u.',label=True,path='../../graphics/A20discreet{}.png'.format(kwargs.get('mode','')),DPI=500)

	px=[prc.discr(py[12],m12)]
	colour=[c.green]
	label=['NF$\kappa$B:I$\kappa$B']
	ps.figa(t,px,colour,label,xlim=xlim,title=string,linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ a.u.',label=True,path='../../graphics/IkBdiscreet{}.png'.format(kwargs.get('mode','')),DPI=500)

def discreetmean(py,pt,*string):
	t=[pt,pt,pt,pt]
	px=[prc.discr(py[6],np.mean(py[6])),prc.discr(py[1],np.mean(py[1])),prc.discr(py[7],np.mean(py[7])),prc.discr(py[12],np.mean(py[12]))]
	colour=['navy',c.blood,c.darkorange,c.green]
	label=['NF$\kappa$B','IKKa','A20','NF$\kappa$B:I$\kappa$B']
	lstyle=['-','-','-','-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,xlim=xlim,title=string,linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ a.u.',label=True,path='../../graphics/discreetmean.png',DPI=500)	

def discreetmedian(py,pt,*string):
	t=[pt,pt,pt,pt]
	px=[prc.discr(py[6],np.median(py[6])),prc.discr(py[1],np.median(py[1])),prc.discr(py[7],np.median(py[7])),prc.discr(py[12],np.median(py[12]))]
	colour=['navy',c.blood,c.darkorange,c.green]
	label=['NF$\kappa$B','IKKa','A20','NF$\kappa$B:I$\kappa$B']
	lstyle=['-','-','-','-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,xlim=xlim,title=string,linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ a.u.',label=True,path='../../graphics/discreetmedian.png',DPI=500)	

def threshmean(py,pt,string):
	t=[pt,pt]
	xlim=(-1,6)
	lstyle=['-','--']
	label=[string,'$\\vartheta$']

	###PLOTTING#########
	px=[py[6],ps.hline(np.mean(py[6]),pt)]
	colour=['navy','gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B',linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ $\mu$M',label=True,path='../../graphics/NF'+string+'threshmean.png',DPI=500)

	###PLOTTING#########
	px=[py[1],ps.hline(np.mean(py[1]),pt)]
	colour=[c.blood,'gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='IKKa',linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ $\mu$M',label=True,path='../../graphics/IKK'+string+'threshmean.png',DPI=500)

	###PLOTTING#########
	px=[py[7],ps.hline(np.mean(py[7]),pt)]
	colour=[c.darkorange,'gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='A20',linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ $\mu$M',label=True,path='../../graphics/A20'+string+'threshmean.png',DPI=500)

	###PLOTTING#########
	px=[py[12],ps.hline(np.mean(py[12]),pt)]
	colour=[c.green,'gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B:I$\kappa$B',linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ $\mu$M',label=True,path='../../graphics/IkB'+string+'threshmean.png',DPI=500)

def threshmedian(py,pt,string):	
	t=[pt,pt]
	xlim=(-1,6)
	lstyle=['-','--']
	label=[string,'$\\vartheta$']
	
	###PLOTTING#########	
	px=[py[6],ps.hline(np.median(py[6]),pt)]
	colour=['navy','gray']	
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B',linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ $\mu$M',label=True,path='../../graphics/NF'+string+'threshmedian.png',DPI=500)

	###PLOTTING#########
	px=[py[1],ps.hline(np.median(py[1]),pt)]
	colour=[c.blood,'gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='IKKa',linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ $\mu$M',label=True,path='../../graphics/IKK'+string+'threshmedian.png',DPI=500)

	###PLOTTING#########
	px=[py[7],ps.hline(np.median(py[7]),pt)]
	colour=[c.darkorange,'gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='A20',linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ $\mu$M',label=True,path='../../graphics/A20'+string+'threshmedian.png',DPI=500)

	###PLOTTING#########
	px=[py[12],ps.hline(np.median(py[12]),pt)]
	colour=[c.green,'gray']
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B:I$\kappa$B',linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ $\mu$M',label=True,path='../../graphics/IkB'+string+'threshmedian.png',DPI=500)	

def discrnor(py,pt,**kwargs):
	mode=kwargs.get('mode','limit')
	(m6,m7,m12,m1,n1)=prc.evmode(mode,py)
	t=[pt,pt,pt]
	xlim=(-1,6)
	label=['Normalisation','Discretisation','$\\vartheta$']
	lstyle=['-','--','-.']
	tick=(0,0.25,0.5,.75,1)

	px=[prc.norm(py[6]),prc.discr(py[6],m6),ps.hline(m6,pt)]
	colour=['navy',c.dodgerblue,c.plum]	
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B',yticks=tick,linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ a.u.',label=True,path='../../graphics/NFdiscrnor{}{}.png'.format(kwargs.get('name',''),kwargs.get('mode','mean')),DPI=500)	
		
	px=[prc.norm(py[12]),prc.discr(py[12],m12),ps.hline(m12,pt)]
	colour=[c.green,c.lime,c.plum]	
	ps.figa(t,px,colour,label,xlim=xlim,title='NF$\kappa$B:I$\kappa$B',yticks=tick,linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ a.u.',label=True,path='../../graphics/IkBdiscrnor{}{}.png'.format(kwargs.get('name',''),kwargs.get('mode','mean')),DPI=500)
	
	lstyle[2]=':'
	px=[prc.norm(py[7]),prc.discr(py[7],m7),ps.hline(m7,pt)]
	colour=[c.darkorange,c.gold,c.deeppink]
	ps.figa(t,px,colour,label,xlim=xlim,title='A20',yticks=tick,linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ a.u.',label=True,path='../../graphics/A20discrnor{}{}.png'.format(kwargs.get('name',''),kwargs.get('mode','mean')),DPI=500)
	
	lstyle.append('-.')
	t.append(pt)
	label.append('$\\vartheta_2$')
	px=[prc.norm(py[1]),prc.discr(py[1],m1,n1),ps.hline(m1,pt),ps.hline(n1,pt)]
	colour=[c.blood,'r',c.deeppink,c.plum]		
	ps.figa(t,px,colour,label,xlim=xlim,title='IKKa',yticks=tick,linestyle=lstyle,xlabel='t$\\ /\\ $h',ylabel='c$\\ / \\ $ a.u.',label=True,path='../../graphics/IKKdiscrnor{}{}.png'.format(kwargs.get('name',''),kwargs.get('mode','mean')))

def evplt(dy,DY,**kwargs):
	dt=np.arange(dy.shape[1])	

	plt.style.use('seaborn-darkgrid')
	plt.plot(dt,dy[1],'-',c=c.blood,label='IKKa')
	plt.plot(dt,dy[6],'--',c=c.navy,label='NF$\kappa$B')
	plt.plot(dt,dy[7],'-.',c=c.darkorange,label='A20')
	plt.plot(dt,dy[12],':',c=c.green,label='NF$\kappa$B:I$\kappa$B')
	plt.legend()
	plt.yticks([-1,0,1])
	plt.xlim(0,4000)
	plt.ylabel('change')
	plt.xlabel('time steps')
	plt.tight_layout()
	plt.savefig('../../graphics/evplttimend{}.png'.format(kwargs.get('strg','')),dpi=500)
	plt.close()

	plt.style.use('seaborn-darkgrid')

	D=prc.insee(prc.ceem(np.array([DY[1],DY[6],DY[7],DY[12]])))
	DT=np.arange(D.shape[1])

	plt.plot(DT,D[0],'-',c=c.blood,label='IKKa')
	plt.plot(DT,D[1],'--',c=c.navy,label='NF$\kappa$B')
	plt.plot(DT,D[2],'-.',c=c.darkorange,label='A20')
	plt.plot(DT,D[3],':',c=c.green,label='NF$\kappa$B:I$\kappa$B')
	plt.legend()
	plt.yticks([-1,0,1])
	if np.amax(DT)>85:
		plt.xlim(0,85)
	plt.ylabel('change')
	plt.xlabel('time steps')
	plt.tight_layout()
	plt.savefig('../../graphics/evpltscale{}.png'.format(kwargs.get('strg','')),dpi=500)
	plt.close()