import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np 

import plotset as ps
import colours as c
import plots as s
from results import load

restore=load('../../simres/results2018-07-19.npz')
#print(restore.files)
pt=restore['pt']
py=restore['py']

###ONE AT A TIME###
s.plainall(pt,py,'wt')
s.discreet(py,pt)
s.discrall(py,pt)
s.normplt(py,pt)
s.thresh(py,pt,'wt')
s.discrnor(py,pt)

#s.discreetmean(py,pt)#
#s.discreetmedian(py,pt)#
#s.threshmean(py,pt,'wt')#
#s.threshmedian(py,pt,'wt')#

#px=[py[6]]
#py=[py[9]]
#colour=['r']
#colourmap=[cm.autumn]
#lab=['wt']
#p.phaseplt(px,py,colour,colourmap,lab,xlabel='NF$\kappa$B',ylabel='I$\kappa$B')