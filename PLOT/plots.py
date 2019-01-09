import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.lines import Line2D
from matplotlib.ticker import FormatStrFormatter, NullFormatter

import process as prc
import plotset as ps
import colours as c
import model as mod

def append(LIST,obj):
	appendix=LIST
	appendix.append(obj)
	return appendix

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
	(m6,m7,m12,m1,n1)=prc.evmode(mode)
	t=[pt,pt,pt,pt]
	xlim=(-1,6)
	label=['Normalisation','Discretisation','$\\vartheta$']
	lstyle=['-','--','-.','-.']
	tick=[0,0.5,1]
	mtick=[0.25,0.75]
	xlab='t$\\ /\\ $h'
	ylab='c / nM'
	ylab2='Activity'
	c1=c.plum
	c2=c.deeppink
	MAX6=np.amax(py[6])
	TH6=m6/MAX6
	MAX12=np.amax(py[12])
	TH12=m12/MAX12
	MAX7=np.amax(py[7])
	TH7=m7/MAX7
	MAX1=np.amax(py[1])
	TH1_1=m1/MAX1
	TH1_2=n1/MAX1
	thresh1 = Line2D([0], [0], color=c1, lw=1,linestyle='-.')
	thresh2 = Line2D([0], [0], color=c2, lw=1,linestyle=':')
	l1 = Line2D([0], [0], color='black', lw=1,linestyle='-')
	l2 = Line2D([0], [0], color='black', lw=1,linestyle='--')

	
	plt.style.use('seaborn-paper')
	fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(2,2)

	px1=[prc.norm(py[6]),prc.discr(py[6],m6),ps.hline(TH6,pt)]
	colour1=['navy',c.dodgerblue,c1]	
	for i,j in enumerate(px1):
		ax1.plot(t[i]-101,j,c=colour1[i],linestyle=lstyle[i])
	ax1.set_title('NF$\kappa$B')
	ax1.set_xlim(xlim)	
	ax1.set_yticks(tick)
	ax1.set_yticks(TH6,minor=True)
	ax1.set_yticklabels([0,np.around(MAX6*500,decimals=1),np.around(MAX6*1000,decimals=1)])
	ax1.set_yticklabels([np.around(MAX6*TH6[0]*1000,decimals=1)],minor=True)
	ax1.set_xlabel(xlab)
	ax1.set_ylabel(ylab)
	ax12=ax1.twinx()
	ax12.yaxis.tick_right()	
	NUL=ax12.transData.inverted().transform(ax1.transData.transform((0,0)))[1]
	HALF=ax12.transData.inverted().transform(ax1.transData.transform((0,0.5)))[1]
	ONE=ax12.transData.inverted().transform(ax1.transData.transform((1,1)))[1]
	ax12.set_yticks([NUL,HALF,ONE])	
	ax12.set_yticklabels([0,0.5,1])
	ax12.set_ylabel(ylab2)

	px2=[prc.norm(py[12]),prc.discr(py[12],m12),ps.hline(TH12,pt)]
	colour2=[c.green,c.lime,c1]
	for i,j in enumerate(px2):
		ax2.plot(t[i]-101,j,c=colour2[i],linestyle=lstyle[i])
	ax2.set_title('I$\kappa$B')
	ax2.set_xlim(xlim)	
	ax2.set_yticks(tick)
	ax2.set_yticks(TH12,minor=True)
	ax2.set_yticklabels([0,np.around(MAX12*500,decimals=1),np.around(MAX12*1000,decimals=1)])
	ax2.set_yticklabels([np.around(MAX12*TH12[0]*1000,decimals=1)],minor=True)
	ax2.set_xlabel(xlab)
	ax2.set_ylabel(ylab)
	ax22=ax2.twinx()
	ax22.yaxis.tick_right()	
	NUL=ax22.transData.inverted().transform(ax2.transData.transform((0,0)))[1]
	HALF=ax22.transData.inverted().transform(ax2.transData.transform((0,0.5)))[1]
	ONE=ax22.transData.inverted().transform(ax2.transData.transform((1,1)))[1]
	ax22.set_yticks([NUL,HALF,ONE])
	ax22.set_yticklabels([0,0.5,1])
	ax22.set_ylabel(ylab2)
	
	lstyle[-2]=':'
	px3=[prc.norm(py[7]),prc.discr(py[7],m7),ps.hline(TH7,pt)]
	colour3=[c.darkorange,c.gold,c2]
	for i,j in enumerate(px3):
		ax3.plot(t[i]-101,j,c=colour3[i],linestyle=lstyle[i])
	ax3.set_title('A20')
	ax3.set_xlim(xlim)	
	ax3.set_yticks(tick)
	ax3.set_yticks(TH7,minor=True)
	ax3.set_yticklabels([0,np.around(MAX7*500,decimals=1),np.around(MAX7*1000,decimals=1)])
	ax3.set_yticklabels([np.around(MAX7*TH7[0]*1000,decimals=1)],minor=True)
	ax3.yaxis.get_ticklabels(minor=True)[0].set_verticalalignment('top')
	ax3.yaxis.get_ticklabels()[1].set_verticalalignment('baseline')
	ax3.set_xlabel(xlab)
	ax3.set_ylabel(ylab)
	ax32=ax3.twinx()
	ax32.yaxis.tick_right()	
	NUL=ax32.transData.inverted().transform(ax3.transData.transform((0,0)))[1]
	HALF=ax32.transData.inverted().transform(ax3.transData.transform((0,0.5)))[1]
	ONE=ax32.transData.inverted().transform(ax3.transData.transform((1,1)))[1]
	ax32.set_yticks([NUL,HALF,ONE])
	ax32.set_yticklabels([0,0.5,1])
	ax32.set_ylabel(ylab2)
	
	px4=[prc.norm(py[1]),prc.discr(py[1],m1,n1),ps.hline(TH1_1,pt),ps.hline(TH1_2,pt)]
	colour4=[c.blood,'r',c2,c1]
	for i,j in enumerate(px4):
		ax4.plot(t[i]-101,j,c=colour4[i],linestyle=lstyle[i])
	ax4.set_title('IKK')
	ax4.set_xlim(xlim)	
	ax4.set_yticks(tick[1:])
	ax4.set_yticks(np.append(TH1_1,TH1_2),minor=True)
	ax4.set_yticklabels([np.around(MAX1*500,decimals=1),np.around(MAX1*1000,decimals=1)])
	ax4.set_yticklabels([np.around(MAX1*TH1_1[0]*1000,decimals=1),np.around(MAX1*TH1_2[0]*1000,decimals=1)],minor=True)
	ax4.set_xlabel(xlab)
	ax4.set_ylabel(ylab)
	ax4.yaxis.get_ticklabels(minor=True)[0].set_verticalalignment('top')
	ax4.yaxis.get_ticklabels(minor=True)[1].set_verticalalignment('baseline')
	ax42=ax4.twinx()
	ax42.yaxis.tick_right()	
	NUL=ax42.transData.inverted().transform(ax4.transData.transform((0,0)))[1]
	HALF=ax42.transData.inverted().transform(ax4.transData.transform((0,0.5)))[1]
	ONE=ax42.transData.inverted().transform(ax4.transData.transform((1,1)))[1]
	ax42.set_yticks([NUL,HALF,ONE])
	'''turn off minor ticks:
	for tic in ax42.yaxis.get_minor_ticks():
		tic.tick1On = tic.tick2On = False'''
	ax42.set_yticklabels([0,0.5,1])
	ax42.set_ylabel(ylab2)	

	handles=[l1,l2,thresh1,thresh2]
	labels=['Simulation','Discretised','$\\vartheta_\mathrm{mean}$','$\\vartheta_\mathrm{half}$']

	for ax in fig.axes:
		plt.setp(ax.get_yticklabels(which='both'), fontsize=7)
		plt.setp(ax.get_xticklabels(which='both'), fontsize=7)
		ax.tick_params(direction='in')

	fig.legend(handles, labels, 'center',fontsize=6,framealpha=0,prop={'size': 7},edgecolor=None)

	fig.tight_layout()
	plt.savefig('../../graphics/discrnor{}{}.png'.format(kwargs.get('strg',''),mode),dpi=500)
	plt.close()
	
def evplt(dy,DY,dy2,DY2,**kwargs):

	plt.style.use('seaborn-paper')

	D=prc.insee(prc.ceem(np.array([DY[1],DY[6],DY[7],DY[12]])))

	D2=prc.insee(prc.ceem(np.array([DY2[1],DY2[6],DY2[7],DY2[12]])))
	
	if 'start' in kwargs:
		start=kwargs.get('start')
		D=np.append([[start[0]],[start[1]],[start[2]],[start[3]]],D,axis=1)
		D2=np.append([[start[0]],[start[1]],[start[2]],[start[3]]],D2,axis=1)

		for i,j in enumerate(D):
			for k,l in enumerate(j):
				D[i][k]=j[k-1]+l
		for i,j in enumerate(D2):
			for k,l in enumerate(j):
				D2[i][k]=j[k-1]+l
		for m in range(3):
			app=[]
			for i in range(len(D)):
				app.append([D[i][-1]])
			D=np.append(D,app,axis=1)
			app2=[]
			for i in range(len(D2)):
				app2.append([D2[i][-1]])
			D2=np.append(D2,app2,axis=1)

	DT=np.arange(D.shape[1])
	DT2=np.arange(D2.shape[1])

	xticks=[]
	for i in range(0,D.shape[1]-2,2):
		xticks.append(i+0.5)

	fig=plt.figure()
	gs=GridSpec(2,2)
	ax1 = fig.add_subplot(gs[0, :])
	ax2=fig.add_subplot(gs[-1,:-1])

	ax1.plot(DT,D[0],'-',c=c.blood,label='IKKa')
	ax1.plot(DT,D[1],'--',c=c.navy,label='NF$\kappa$B')
	ax1.plot(DT,D[2],'-.',c=c.darkorange,label='A20')
	ax1.plot(DT,D[3],':',c=c.green,label='NF$\kappa$B:I$\kappa$B')
	
	#ax1.grid(linewidth=.25,color=c.lightslategrey)
	ax1.set_yticks([0,1,2])
	ax1.set_xticks(xticks)
	ax1.set_xlim(0,len(DT)-2)
	ax1.set_ylabel('Level')	
	ax1.set_xticklabels([])
	ax1.set_xlabel('Time (Steps)',x=0.91)
	xtitle=ax1.set_title('$\\mathbf{(a)}$',x=0.05)

	ax2.plot(DT2,D2[0],'-',c=c.blood,label='IKKa')
	ax2.plot(DT2,D2[1],'--',c=c.navy,label='NF$\kappa$B')
	ax2.plot(DT2,D2[2],'-.',c=c.darkorange,label='A20')
	ax2.plot(DT2,D2[3],':',c=c.green,label='NF$\kappa$B:I$\kappa$B')
	
	#ax2.grid(linewidth=.25,color=c.lightslategrey)
	ax2.set_yticks([0,1,2])
	ax2.set_xticks(xticks)
	ax2.set_ylabel('Level')	
	ax2.set_xticklabels([])
	ax2.set_xlabel('Time (Steps)',x=.8)
	ax2.set_title('$\\mathbf{(b)}$',x=ax2.transAxes.inverted().transform(ax1.transAxes.transform(xtitle.get_position()))[0])

	trans = ax2.transAxes + ax1.transData.inverted()
	((xmin,_),(xmax,_)) = trans.transform([[0,1],[1,1]])
	ax2.set_xlim(xmin,xmax)
	
	handles, labels = ax1.get_legend_handles_labels()
	fig.legend(handles, labels, loc=(0.61,0.18),framealpha=1,prop={'size': 10},edgecolor=None)
	#fig.tight_layout()
	plt.savefig('../../graphics/evpltscale{}.png'.format(kwargs.get('strg','')),dpi=500)
	plt.close()

def compall(pt,py,pt2,py2,*string):
	if string:
		strg=string[0]
	else:
		strg=''
	###PLOTTING#########
	t=[pt,pt2]
	px=[[py[6],py2[6]],
	[py[12],py2[12]],
	[py[7],py2[7]],
	[py[1],py2[1]]]
	
	colour=[['navy','blue'],
	[c.green,c.limegreen],
	[c.darkorange,c.gold],
	[c.blood,c.darkred]]
	label=['wt','A20 KO']
	lstyle=['-','--']
	xlim=(-1,6)
	xlabel='t$\\ /\\ $h'
	ylabel='c / nM'
	vertal='baseline'

	plt.style.use('seaborn-paper')
	fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(2,2)

	for i,j in enumerate(px[0]):
		ax1.plot(t[i]-101,j*1000,c=colour[0][i],linestyle=lstyle[i],label=label[i])
	ax1.set_title('NF$\kappa$B')

	for i,j in enumerate(px[1]):
		ax2.plot(t[i]-101,j*1000,c=colour[1][i],linestyle=lstyle[i],label=label[i])
	ax2.set_title('I$\kappa$B:NF$\kappa$B')

	for i,j in enumerate(px[2]):
		ax3.plot(t[i]-101,j*1000,c=colour[2][i],linestyle=lstyle[i],label=label[i])
	ax3.set_title('A20')

	for i,j in enumerate(px[3]):
		ax4.plot(t[i]-101,j*1000,c=colour[3][i],linestyle=lstyle[i],label=label[i])
	ax4.set_title('IKK')

	for ax in fig.axes:
		ax.set_xlim(xlim)
		ax.tick_params(direction='in')
		ax.set_ylabel(ylabel)
		ax.set_xlabel(xlabel)
		ax.set_xticks([0],minor=True)
		ax.set_xticklabels(['*'],minor=True,fontsize=10,fontweight='bold',color='r',verticalalignment=vertal)


	handles=[Line2D([0], [0], color='black', lw=1,linestyle='-'),
	Line2D([0], [0], color='black', lw=1,linestyle='--')]
	labels=['wt','A20-/-']

	fig.legend(handles, labels, 'center',fontsize=7,framealpha=0,prop={'size': 8},edgecolor=None)

	fig.tight_layout()
	plt.savefig('../../graphics/compall{}.png'.format(strg),dpi=500)
	plt.close()
	
def varplt(var1,var2,colours,lab,**kwargs):
	plt.style.use('seaborn-paper')
	fig,ax=plt.subplots(1,1)	
	for i in range(1,len(var1)):		
		ax.plot(var1[0],var1[i],c=colours[i-1][0],label=lab[i-1][0])
		ax.plot(var2[0],var2[i],'--',c=colours[i-1][1],label=lab[i-1][1])
	if 'title' in kwargs:
		ax.set_title(kwargs.get('title'))
	ax.legend()
	ax.grid()
	ax.set_xlabel('time frame$\\ / \\ $h')
	ax.set_ylabel('value$\\ / \\ $ $\mu$M')
	ax.set_xlim(0,24)
	fig.tight_layout()	
	if 'path' in kwargs:
		fig.savefig(kwargs['path'],dpi=kwargs.get('DPI',500))
	else:
		plt.show()
	plt.close()