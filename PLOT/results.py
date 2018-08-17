import numpy as np

def load(path):
	f=open(path,'rb')
	lst=np.load(f)
	return lst