import numpy as np
import datetime 

def dump(path,**kwargs):
	fid=open(path+'{}.npz'.format(datetime.datetime.now()), 'wb+')
	np.savez(fid,**kwargs)
	fid.close()

def save(path,**kwargs):
	fid=open(path+'{}.txt'.format(datetime.datetime.now()), 'a+')
	fid.write('{}\r\n'.format(datetime.datetime.now()))
	for key,value in kwargs.items():
		fid.write('{}={}\r\n'.format(key,value))
	fid.write('\r\n\r\n')
	fid.close()