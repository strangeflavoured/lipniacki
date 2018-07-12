import numpy as np
import datetime 

def dump(path,**kwargs):
	fid=open(path, 'wb+')
	np.savez(fid,**kwargs)
	fid.close()

def load(path):
	f=open(path,'rb')
	lst=np.load(f)
	return lst

def save(path,**kwargs):
	fid=open(path, 'a+')
	fid.write('{}\r\n'.format(datetime.datetime.now()))
	for key,value in kwargs.items():
		fid.write('{}={}\r\n'.format(key,value))
	fid.write('\r\n\r\n')
	fid.close()