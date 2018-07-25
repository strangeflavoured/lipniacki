import numpy as np
import datetime 

def dump(path,**kwargs):
	fid=open(path+'{}.npz'.format(datetime.datetime.today()), 'wb+')
	np.savez(fid,**kwargs)
	fid.close()

def save(path,**kwargs):
	fid=open(path+'{}.txt'.format(datetime.datetime.today()), 'a+')
	fid.write('{}\r\n'.format(datetime.datetime.today()))
	for key,value in kwargs.items():
		fid.write('{}={}\r\n'.format(key,value))
	fid.write('\r\n\r\n')
	fid.close()