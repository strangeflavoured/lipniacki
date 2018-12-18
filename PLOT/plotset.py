import matplotlib.pyplot as plt
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

def phaseplt(px,py,colour,colourmap,lab,**kwargs):
	ttl=kwargs.get('title','phaseplot')
	stl=kwargs.get('style','seaborn-dark')
	xl=kwargs.get('xlabel')
	yl=kwargs.get('ylabel')
	label=kwargs.get('label')
	xlim=kwargs.get('xlim')

	plt.style.use(stl)

	fig, ax=plt.subplots(nrows=1,ncols=1)	
	for i in range(0,len(px)):
		ax.plot(px[i],py[i],c=colour[i],label=lab[i])
		col=colourmap[i](np.linspace(1,0,len(px[i])))
		for j,c in enumerate(col):
			ax.plot(px[i][j],py[i][j], 'o', c=c)

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