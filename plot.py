import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def save(fig,bool):
	if bool==True:
		save=str(input('save as: '))
		save='../'+save
		if save not in ('0', 'NO', 'no', 'No', 'nein', 'NEIN', 'Nein','n', 'N', '', ' ','q', 'Q','quit', 'Quit'):
			fig.savefig(save, dpi=500)#fullscreen
			s=save+'small'
			fig.savefig(s, dpi=150)

def figa(pt,px,colour,stl,start,lim,ttl,xl,yl,bool):
	fig, ax=plt.subplots(nrows=1,ncols=1)
	plt.style.use(stl)

	ax.plot(pt-start,px,c=colour)
	ax.set_xlim(lim)
	ax.set_title(ttl)
	ax.set_xlabel(xl)
	ax.set_ylabel(yl)

	ax.grid(which='major', c='gray', linewidth=0.5, linestyle='--')
	ax.grid(which='minor', linewidth=0.25, linestyle=':')

	fig.tight_layout()
	plt.show()
	save(fig,bool)
	plt.close()
