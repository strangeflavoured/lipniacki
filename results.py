import numpy as np

def dump(path,**kwargs):
	fid=open(path, 'wb+')
	np.savez(fid,**kwargs)
	fid.close()

def load(path):
	f=open(path,'rb')
	lst=np.load(f)
	return lst