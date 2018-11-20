import matplotlib.pyplot as plt
import matplotlib as mpl
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

def phase3d(px,py,pz,a,colourmap,lab,**kwargs):
	ttl=kwargs.get('title','')
	stl=kwargs.get('style','seaborn-paper')
	xl=kwargs.get('xlabel')
	yl=kwargs.get('ylabel')
	zl=kwargs.get('zlabel')
	label=kwargs.get('label')
	xlim=kwargs.get('xlim')

	plt.style.use(stl)

	fig= plt.figure(frameon=False)
	ax = plt.subplot2grid((10,1),(0,0),rowspan=9,projection='3d')	
	for i in range(0,len(px)):
		Da=np.amax(a[i])-np.amin(a[i])
		Amin=np.amin(a[i])
		cmap0,cmap1=colourmap[i](np.linspace(0,1,2))
		Dcmap=(cmap1[0]-cmap0[0],cmap1[1]-cmap0[1],cmap1[2]-cmap0[2],cmap1[3]-cmap0[3])
		c=[]
		for j,k in enumerate(px[i]):
			c0=cmap0[0]+Dcmap[0]*(a[i][j]-Amin)/Da
			c1=cmap0[1]+Dcmap[1]*(a[i][j]-Amin)/Da
			c2=cmap0[2]+Dcmap[2]*(a[i][j]-Amin)/Da
			c3=cmap0[3]+Dcmap[3]*(a[i][j]-Amin)/Da
			c.append((c0,c1,c2,c3))
		p=ax.scatter(np.flip(px[i],0),np.flip(py[i],0),np.flip(pz[i],0),'.',color=np.flip(c,0))


	#cbar = fig.colorbar(p, ticks=[-1, 0, 1],orientation='horizontal')
	#cbar.ax.set_xticklabels(['Low', 'Medium', 'High'])  # horizontal colorbar
	ax2=plt.subplot2grid((10,1),(9,0))

	norm = mpl.colors.Normalize(vmin=np.amin(a[i]), vmax=np.amax(a[i]))
	cb1 = mpl.colorbar.ColorbarBase(ax2, cmap=colourmap[i],norm=norm,orientation='horizontal')
	cb1.set_label('A20')

	if xlim:
		ax.set_xlim(xlim)

	ax.set_title(ttl)
	
	if xl:
		ax.set_xlabel(xl)
	if yl:
		ax.set_ylabel(yl)
	if zl:
		ax.set_zlabel(zl)
	if label:
		ax.legend()

	ax.grid(c='gray', linewidth=0.5, linestyle='--')

	fig.tight_layout()
	if 'path' in kwargs:
		fig.savefig(kwargs['path'],dpi=kwargs.get('DPI',500))
	else:
		plt.show()
	plt.close()