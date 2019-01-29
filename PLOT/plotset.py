import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.lines as mlines
from matplotlib.collections import LineCollection
from matplotlib.gridspec import GridSpec
from matplotlib.colors import LogNorm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import numpy as np

def hline(val,pt):
	hx=[]
	for i,j in enumerate(pt):
		hx.append(val)
	return hx

def save(fig):
	save=input('save as: ')
	if save:
		fig.savefig(save, dpi=500)#fullscreen
		s=save+'small'
		fig.savefig(s, dpi=150)
	else:
		print('{} not saved'.format(fig))

def figa(pt,px,colour,lab,**kwargs):
	ttl=kwargs.get('title')
	stl=kwargs.get('style','seaborn-paper')
	xl=kwargs.get('xlabel')
	yl=kwargs.get('ylabel')
	label=kwargs.get('label')
	xlim=kwargs.get('xlim')
	lstyle=kwargs.get('linestyle')
	note=kwargs.get('annotate')
	strt=kwargs.get('start',101)
	ytick=kwargs.get('yticks')
	xtick=kwargs.get('xticks')
	if not lstyle:
		lstyle=[]
		for i in range(0,len(px)):
			lstyle.append['-']

	plt.style.use(stl)

	fig, ax=plt.subplots(nrows=1,ncols=1)	
	for i in range(0,len(px)):
		ax.plot(pt[i]-strt,px[i],c=colour[i],label=lab[i],linestyle=lstyle[i])
	ax.scatter(0,0,c='k',marker=6)

	if xlim:
		ax.set_xlim(xlim)
	if ttl:
		ax.set_title(ttl)
	if xl:
		ax.set_xlabel(xl)
	if yl:
		ax.set_ylabel(yl)
	if label:
		ax.legend()
	if note:
		ax.annotate(note)
	if ytick:
		ax.set_yticks(ytick)
	if xtick:
		ax.set_xticks(xtick)
		

	ax.grid(c='gray', linewidth=0.5, linestyle='--')

	fig.tight_layout()	
	if 'path' in kwargs:
		fig.savefig(kwargs['path'],dpi=kwargs.get('DPI',500))
	#plt.show()
	plt.close()

def phaseplt(px,py,pt,colour,colourmap,lab,**kwargs):
	ttl=kwargs.get('title','phaseplot')
	stl=kwargs.get('style','seaborn-paper')
	xl=kwargs.get('xlabel')
	yl=kwargs.get('ylabel')
	label=kwargs.get('label')
	xlim=kwargs.get('xlim')

	plt.style.use(stl)

	fig, ax=plt.subplots(nrows=1,ncols=1)	
	for i in range(0,len(px)):
		dt=pt[i][-1]-pt[i][0]
		ax.plot(px[i],py[i],c=colour[i],label=lab[i])
		col=colourmap[i](np.linspace(1,0,len(px[i])))
		count=0
		steps=250
		for j,k in enumerate(pt[i]):
			if k>=count*dt/steps:
				ax.plot(px[i][j],py[i][j],'o',c=col[j])
				count+=1

	if xlim:
		ax.set_xlim(xlim)

	ax.set_title(ttl)
	
	if xl:
		ax.set_xlabel(xl)
	if yl:
		ax.set_ylabel(yl)
	if label:
		ax.legend()

	ax.grid(c='gray', linewidth=0.5, linestyle='--')

	fig.tight_layout()
	if 'path' in kwargs:
		fig.savefig(kwargs['path'],dpi=kwargs.get('DPI',500))
	else:
		plt.show()
	plt.close()

def phase3d(px,py,pz,a,colourmap,marker,**kwargs):
	ttl=kwargs.get('title','')
	stl=kwargs.get('style','seaborn-paper')
	xl=kwargs.get('xlabel','NF$\kappa$Bn / nM')
	yl=kwargs.get('ylabel','I$\kappa$Bc / nM')
	zl=kwargs.get('zlabel','IKKa / nM')
	label=kwargs.get('label')
	xlim=kwargs.get('xlim')

	plt.style.use(stl)

	fig= plt.figure(frameon=False)
	ax = plt.subplot2grid((10,9),(0,0),rowspan=9,colspan=9,projection='3d')
	ax2=plt.subplot2grid((10,9),(9,1),colspan=7)	

	Amax=np.amax(a)
	Amin=np.amin(a)
	Da=Amax-Amin	
	cmap0,cmap1=colourmap(np.linspace(0,1,2))
	Dcmap=(cmap1[0]-cmap0[0],cmap1[1]-cmap0[1],cmap1[2]-cmap0[2],cmap1[3]-cmap0[3])		
	
	NormA=plt.Normalize(vmin=0,vmax=Amax)
	p=ax.scatter(px,py,pz,c=colourmap(NormA(a)))
	
	norm = plt.Normalize(vmin=0, vmax=Amax)
	cb1 = mpl.colorbar.ColorbarBase(ax2, cmap=colourmap,norm=norm,orientation='horizontal')
	cb1.set_label('A20 / nM')

	if xlim:
		ax.set_xlim(xlim)

	ax.set_title(ttl)
	
	#ax.scatter(px[0],py[0],pz[0],marker=6,c='k',zorder=4)
	#ax.zaxis._axinfo['juggled'] = (1,2,0)
	ax.xaxis.pane.fill = False
	ax.yaxis.pane.fill = False
	ax.zaxis.pane.fill = False
	ax.xaxis.pane.set_edgecolor('black')
	ax.yaxis.pane.set_edgecolor('black')
	ax.zaxis.pane.set_edgecolor('black')
	ax.set_xticks([0,100,200,300])
	ax.set_yticks([0,10,20,30])
	ax.set_zticks([0,20,40,60,80])
	ax.invert_yaxis()
	ax.grid(False)	
	
	ax.set_xlabel(xl)
	ax.set_ylabel(yl)
	ax.set_zlabel(zl,rotation=85)

	#ax.view_init(90, 90)
	
	if label:
		ax.legend()

	fig.tight_layout()
	if 'path' in kwargs:
		fig.savefig(kwargs['path'],dpi=kwargs.get('DPI',500))
	else:
		plt.show()
	plt.close()