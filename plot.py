import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def save(fig):
	save=input('save as: ')
	if save:
		fig.savefig(save, dpi=500)#fullscreen
		s=save+'small'
		fig.savefig(s, dpi=150)
	else:
		print('{} not saved'.format(fig))

def figa(pt,px,colour,lab,start,lim,**kwargs):
	ttl=kwargs.get('title')
	stl=kwargs.get('style','seaborn-dark')
	xl=kwargs.get('xlabel')
	yl=kwargs.get('ylabel')
	label=kwargs.get('label')

	plt.style.use(stl)

	fig, ax=plt.subplots(nrows=1,ncols=1)	
	for i in range(0,len(px)):
		ax.plot(pt-start,px[i],c=colour[i],label=lab[i])

	ax.set_xlim(lim)

	if ttl==True:
		ax.set_title(ttl)
	if xl==True:
		ax.set_xlabel(xl)
	if yl==True:
		ax.set_ylabel(yl)
	if label!=False:
		ax.legend()

	ax.grid(c='gray', linewidth=0.5, linestyle='--')

	fig.tight_layout()
	plt.show()
	if 'path' in kwargs:
		fig.savefig(kwargs['path'],dpi=kwargs.get('DPI',500))
	plt.close()
