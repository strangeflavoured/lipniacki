import numpy as np

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
	ps.figa(t,px,colour,label,101,xlim=xlim,title='NF$\kappa$B',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../../graphics/NF'+strg+'.png',DPI=500)

	###PLOTTING#########
	t=[pt]
	px=[py[1]]
	colour=[c.blood]
	label=[strg]
	lstyle=['-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title='IKKa',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=False,path='../../graphics/IKK'+strg+'.png',DPI=500)

	###PLOTTING#########
	t=[pt]
	px=[py[7]]
	colour=[c.darkorange]
	label=[strg]
	lstyle=['-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title='A20',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=False,path='../../graphics/A20'+strg+'.png',DPI=500)

	###PLOTTING#########
	t=[pt,pt]
	px=[py[12],py[13]]
	colour=[c.green,c.lime]
	label=['cytoplasmic','nuclear']
	lstyle=['-','--']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title='NF$\kappa$B:I$\kappa$B',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../../graphics/IkB'+strg+'.png',DPI=500)

	###PLOTTING#########
	t=[pt,pt]
	px=[py[11],py[8]]
	colour=[c.slategrey,c.steelblue]
	label=['I$\kappa$B','A20']
	lstyle=['-','--']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title='Transcripts',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../../graphics/RNA'+strg+'.png',DPI=500)

def thresh(py,pt,string):	
	###PLOTTING#########
	t=[pt,pt]
	px=[py[6],ps.hline(mod.limit1(6),pt)]
	colour=['navy','gray']
	label=[string,'$\delta$']
	lstyle=['-','--']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title='NF$\kappa$B',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../../graphics/NF'+string+'thresh.png',DPI=500)

	###PLOTTING#########
	t=[pt,pt,pt]
	px=[py[1],ps.hline(mod.limit1(1),pt),ps.hline(mod.limitKO(1),pt)]
	colour=[c.maroon,'gray','gray']
	label=[string,'$\delta_1$','$\delta_2$']
	lstyle=['-','--','-.']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title='IKKa',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../../graphics/IKK'+string+'thresh.png',DPI=500)

	###PLOTTING#########
	t=[pt,pt]
	px=[py[7],ps.hline(mod.limit1(7),pt)]
	colour=[c.darkorange,'gray']
	label=[string,'$\delta$']
	lstyle=['-','--']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title='A20',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../../graphics/A20'+string+'thresh.png',DPI=500)

	###PLOTTING#########
	t=[pt,pt]
	px=[py[12],ps.hline(mod.limit1(12),pt)]
	colour=[c.green,'gray']
	label=[string,'$\delta$']
	lstyle=['-','--']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title='NF$\kappa$B:I$\kappa$B',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../../graphics/IkB'+string+'thresh.png',DPI=500)

def normplt(py,pt,*string):
	t=[pt,pt,pt,pt]
	px=[prc.norm(py[6]),prc.norm(py[1]),prc.norm(py[7]),prc.norm(py[12])]
	colour=['navy',c.maroon,c.darkorange,c.green]
	label=['NF$\kappa$B','IKKa','A20','NF$\kappa$B:I$\kappa$B']
	lstyle=['-','-','-','-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title=string,linestyle=lstyle,xlabel='h',ylabel='a.u.',label=True,path='../../graphics/normalised.png',DPI=500)

def discreet(py,pt,*string):
	t=[pt,pt,pt,pt]
	px=[prc.discr(py[6],mod.limit1(6)),prc.discr(py[1],mod.limit1(1)),prc.discr(py[7],mod.limit1(7)),prc.discr(py[12],mod.limit1(12))]
	colour=['navy',c.maroon,c.darkorange,c.green]
	label=['NF$\kappa$B','IKKa','A20','NF$\kappa$B:I$\kappa$B']
	lstyle=['-','-','-','-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title=string,linestyle=lstyle,xlabel='h',ylabel='a.u.',label=True,path='../../graphics/discreet.png',DPI=500)

def discreetmean(py,pt,*string):
	t=[pt,pt,pt,pt]
	px=[prc.discr(py[6],np.mean(py[6])),prc.discr(py[1],np.mean(py[1])),prc.discr(py[7],np.mean(py[7])),prc.discr(py[12],np.mean(py[12]))]
	colour=['navy',c.maroon,c.darkorange,c.green]
	label=['NF$\kappa$B','IKKa','A20','NF$\kappa$B:I$\kappa$B']
	lstyle=['-','-','-','-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title=string,linestyle=lstyle,xlabel='h',ylabel='a.u.',label=True,path='../../graphics/discreetmean.png',DPI=500)	

def discreetmedian(py,pt,*string):
	t=[pt,pt,pt,pt]
	px=[prc.discr(py[6],np.median(py[6])),prc.discr(py[1],np.median(py[1])),prc.discr(py[7],np.median(py[7])),prc.discr(py[12],np.median(py[12]))]
	colour=['navy',c.maroon,c.darkorange,c.green]
	label=['NF$\kappa$B','IKKa','A20','NF$\kappa$B:I$\kappa$B']
	lstyle=['-','-','-','-']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title=string,linestyle=lstyle,xlabel='h',ylabel='a.u.',label=True,path='../../graphics/discreetmedian.png',DPI=500)	

def threshmean(py,pt,string):	
	###PLOTTING#########
	t=[pt,pt]
	px=[py[6],ps.hline(np.mean(py[6]),pt)]
	colour=['navy','gray']
	label=[string,'$\delta$']
	lstyle=['-','--']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title='NF$\kappa$B',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../../graphics/NF'+string+'threshmean.png',DPI=500)

	###PLOTTING#########
	t=[pt,pt]
	px=[py[1],ps.hline(np.mean(py[1]),pt)]
	colour=[c.maroon,'gray']
	label=[string,'$\delta$']
	lstyle=['-','--']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title='IKKa',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../../graphics/IKK'+string+'threshmean.png',DPI=500)

	###PLOTTING#########
	t=[pt,pt]
	px=[py[7],ps.hline(np.mean(py[7]),pt)]
	colour=[c.darkorange,'gray']
	label=[string,'$\delta$']
	lstyle=['-','--']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title='A20',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../../graphics/A20'+string+'threshmean.png',DPI=500)

	###PLOTTING#########
	t=[pt,pt]
	px=[py[12],ps.hline(np.mean(py[12]),pt)]
	colour=[c.green,'gray']
	label=[string,'$\delta$']
	lstyle=['-','--']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title='NF$\kappa$B:I$\kappa$B',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../../graphics/IkB'+string+'threshmean.png',DPI=500)

def threshmedian(py,pt,string):	
	###PLOTTING#########
	t=[pt,pt]
	px=[py[6],ps.hline(np.median(py[6]),pt)]
	colour=['navy','gray']
	label=[string,'$\delta$']
	lstyle=['-','--']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title='NF$\kappa$B',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../../graphics/NF'+string+'threshmedian.png',DPI=500)

	###PLOTTING#########
	t=[pt,pt]
	px=[py[1],ps.hline(np.median(py[1]),pt)]
	colour=[c.maroon,'gray']
	label=[string,'$\delta$']
	lstyle=['-','--']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title='IKKa',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../../graphics/IKK'+string+'threshmedian.png',DPI=500)

	###PLOTTING#########
	t=[pt,pt]
	px=[py[7],ps.hline(np.median(py[7]),pt)]
	colour=[c.darkorange,'gray']
	label=[string,'$\delta$']
	lstyle=['-','--']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title='A20',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../../graphics/A20'+string+'threshmedian.png',DPI=500)

	###PLOTTING#########
	t=[pt,pt]
	px=[py[12],ps.hline(np.median(py[12]),pt)]
	colour=[c.green,'gray']
	label=[string,'$\delta$']
	lstyle=['-','--']
	xlim=(-1,6)
	ps.figa(t,px,colour,label,101,xlim=xlim,title='NF$\kappa$B:I$\kappa$B',linestyle=lstyle,xlabel='h',ylabel='$\mu$M',label=True,path='../../graphics/IkB'+string+'threshmedian.png',DPI=500)	