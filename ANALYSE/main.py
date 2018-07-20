import numpy as np

import results as res
import process as prc
import model as mod
from setting import discrprogr as dp

#restore=res.load('../../simres/results2018-07-18.npz')
#print(restore.files)
#pt=restore['pt']
#py=restore['py']

#x,X=dp(py)

#res.save('../../anres/results',x=x,X=X)
#res.dump('../../anres/results',x=x,X=X)
rest=res.load('../../anres/results2018-07-20.npz')
X=rest['X']
for i in range(0,len(X)):
	print(X[i])