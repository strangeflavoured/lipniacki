import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import FormatStrFormatter
from matplotlib.lines import Line2D

from parameters import para
from model import model
import process as prc

def init(AA,AB,AC,kv,nftot,TR):

	##MODEL#############
	par=para(AA,AB,AC,kv)
	f=model(par,TR)

	##INITIAL VALUES####
	y0=np.zeros(14)
	y0[12]=nftot

	###INITIATION#######
	tspan=[0,60*60*101]

	sol=solve_ivp(f,tspan,y0,method='LSODA')

	return sol

def sim(AA,AB,AC,kv,TR,y0,time,**kwargs):

	##MODEL#############
	par=para(AA,AB,AC,kv)
	ikk=kwargs.get('ikk',False)
	if ikk:
		f=model(par,TR,ikk=ikk)
	else:
		f=model(par,TR)

	###INITIATION#######
	tspan=[0,time]

	sol2=solve_ivp(f,tspan,y0,method='LSODA')

	return sol2

def varkv(AA,AB,AC,nftot,time,itr,pvar):
	SUM=[]
	colour=cm.autumn_r(np.linspace(0,1,len(itr)))
	plt.style.use('seaborn-dark')
	fig,ax=plt.subplots(nrows=1,ncols=1)
	for i,kv in enumerate(itr):
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
		ax.plot(pt-100,py[pvar],label='kv={}'.format(np.around(kv,1)),c=colour[i])
	ax.set_xlim(0,pt[-1]-100)
	ax.set_xlabel('t/h')
	ax.set_ylabel('NF$\kappa$B/$\mu$M')
	fig.suptitle('Variation of nuclear Volume')
	ax.legend()
	ax.grid()
	fig.tight_layout()
	plt.show()
	return SUM

def solve(AA,AB,AC,kv,nftot,**kwargs):
	tspan=kwargs.get('t',60*60*24)
	rev=kwargs.get('reverse',False)
	if rev:
		TR=1
	else:
		TR=0
	###INITIATION#######
	sol=init(AA,AB,AC,kv,nftot,TR)

	###SIMULATION#######
	if rev:
		TR=0
	else:
		TR=1
	y0=sol.y[:,-1]
	sol1=sim(AA,AB,AC,kv,TR,y0,tspan)

	###PROCESSING#######
	SOL=prc.fuse(sol.t,sol.y,sol1.t,sol1.y)
	pt=np.stack(prc.hour(SOL[0]))
	py=np.stack(SOL[1:SOL.shape[0]])
	return[pt,py,sol1,sol.t.shape[0]]

def ikkKO(AA,AB,AC,kv,nftot,**kwargs):	
	TR=kwargs.get('TR',1)
	start=kwargs.get('start',2)
	ikk=kwargs.get('ikk')
	###INITIATION#######
	sol=init(AA,AB,1,kv,nftot,0)

	###SIMULATION#######
	Y0=sol.y[:,-1]
	sol1=sim(AA,AB,1,kv,TR,Y0,60*60*24)

	###PROCESSING#######
	SOL=prc.fuse(sol.t,sol.y,sol1.t,sol1.y)
	pt=np.stack(prc.hour(SOL[0]))
	py=np.stack(SOL[1:SOL.shape[0]])	

	KO=False
	time=None
	for i,j in enumerate(sol1.t):
		if j/3600>=start:
			KO=i
			time=j/3600
			break

	py0=sol1.y[1,KO]###.00128 1.8; .00125 24###
	py1=sol1.y[6,KO]*1000
	pt1=sol1.t[KO]/3600
	y0=sol1.y[:,KO]
	y0[1]=0
	sol3=sim(AA,AB,AC,kv,TR,y0,(24-start)*60*60,ikk=True)
	y0[1]=py0/2
	sol4=sim(AA,AB,AC,kv,TR,y0,(24-start)*60*60,ikk=True)
	y0[1]=py0/4
	sol5=sim(AA,AB,AC,kv,TR,y0,(24-start)*60*60,ikk=True)
	y0[1]=py0
	sol6=sim(AA,AB,AC,kv,TR,y0,(24-start)*60*60,ikk=True)
	y0[1]=2*py0
	sol7=sim(AA,AB,AC,kv,TR,y0,(24-start)*60*60,ikk=True)


	plt.style.use('seaborn-paper')

	MAP=np.linspace(0,1,6)

	fig=plt.figure()
	gs=GridSpec(9,1,hspace=0.1)
	
	ax = fig.add_subplot(gs[:8,:])
	ax3=fig.add_subplot(gs[-1,:])

	colours1=cm.winter(MAP)

	ax.plot(pt-101,1000*py[6],c=(0,0,128/255))
	ax.plot(time+sol7.t/3600,1000*sol7.y[6],linestyle=(0,(5,1)),c=colours1[0])
	ax.plot(time+sol6.t/3600,1000*sol6.y[6],linestyle=(0,(5,5)),c=colours1[1])	
	ax.plot(time+sol4.t/3600,1000*sol4.y[6],'-.',c=colours1[2])
	ax.plot(time+sol5.t/3600,1000*sol5.y[6],linestyle=(0, (3, 1, 1, 1, 1, 1)),c=colours1[3])
	ax.plot(time+sol3.t/3600,1000*sol3.y[6],c=colours1[4],linestyle=(0, (1, 1)))

	handles= [Line2D([0], [0], color='black', lw=1,linestyle='-'),
	Line2D([0], [0], color='black', lw=1,linestyle=(0,(5,1))),
	Line2D([0], [0], color='black', lw=1,linestyle=(0,(5,5))),
	Line2D([0], [0], color='black', lw=1,linestyle='-.'),
	Line2D([0], [0], color='black', lw=1,linestyle=(0, (3, 1, 1, 1, 1, 1))),
	Line2D([0], [0], color='black', lw=1,linestyle=(0,(1,1)))]

	PY0=1000*py0
	labels= ['wild-type', 'IKK={} nM'.format(np.around(2*PY0,decimals=1)),'IKK={} nM'.format(np.around(PY0,decimals=1)),'IKK={} nM'.format(np.around(PY0/2,decimals=1)),'IKK={} nM'.format(np.around(PY0/4,decimals=1)),'IKK=0 nM']
	ax.legend(handles,labels,loc=0,fontsize=10,framealpha=0,prop={'size': 10},edgecolor=None)
	ax.set_xlim(-1,8)
	ax.set_xticks([])
	ax.set_ylabel('$c$ in nM')
	ax2=ax.twinx()
	ax2.set_yticks([])
	ax2.set_ylabel('NF$\kappa$B')
	
	colours2=cm.autumn(MAP)

	ax3.plot(pt-101,1000*py[1],c=(170/255,0,0))
	ax3.plot(time+sol7.t/3600,1000*sol7.y[1],linestyle=(0,(5,1)),c=colours2[0])
	ax3.plot(time+sol6.t/3600,1000*sol6.y[1],linestyle=(0,(5,5)),c=colours2[1])	
	ax3.plot(time+sol4.t/3600,1000*sol4.y[1],'-.',c=colours2[2])
	ax3.plot(time+sol5.t/3600,1000*sol5.y[1],linestyle=(0, (3, 1, 1, 1, 1, 1)),c=colours2[3])
	ax3.plot(time+sol3.t/3600,1000*sol3.y[1],c=colours2[4],linestyle=(0, (1, 1)))
	
	ax3.set_ylim(-.1,3)
	ax3.set_yticks([0,1000*py0,2000*py0])
	ax3.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
	ax3.set_xlabel('$t$ in h')
	ax4=ax3.twinx()
	ax4.set_yticks([])
	ax4.set_ylabel('IKK')

	trans = ax3.transAxes + ax.transData.inverted()
	((xmin,_),(xmax,_)) = trans.transform([[0,1],[1,1]])
	ax3.set_xlim(xmin,xmax)
	ax3.axvline(pt1,linewidth=0.5,c='gray')
	ax.axvline(pt1,linewidth=0.5,c='gray')

	fig.tight_layout()	
	plt.savefig('../../graphics/IKKvar.png',dpi=500)
	plt.close()

	return[pt,py,sol1,sol.t.shape[0],sol3,time]