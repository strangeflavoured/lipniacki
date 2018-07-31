import numpy as np
import datetime

def dump(path,**kwargs):
	fid=open(path+'{}.npz'.format(datetime.date.today()), 'wb+')
	np.savez(fid,**kwargs)
	fid.close()

def load(path):
	f=open(path,'rb')
	lst=np.load(f)
	return lst

def save(path,**kwargs):
	fid=open(path+'{}.txt'.format(datetime.date.today()), 'a+')
	fid.write('{}\r\n'.format(datetime.date.today()))
	for key,value in kwargs.items():
		fid.write('{}={}\r\n'.format(key,value))
	fid.write('\r\n\r\n')
	fid.close()