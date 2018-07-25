import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np 

import plotset as ps
import colours as c
import plots as s
from results import load

restore=load('../../simres/results2018-07-25.npz')
#print(restore.files)
pt=restore['pt']
py=restore['py']

###ONE AT A TIME###
#s.plainall(pt,py,'wt')
#s.discreet(py,pt)
#s.discrall(py,pt)
#s.normplt(py,pt)
#s.thresh(py,pt,'wt')
#s.discrnor(py,pt)

#s.discreetmean(py,pt)#
#s.discreetmedian(py,pt)#
#s.threshmean(py,pt,'wt')#
#s.threshmedian(py,pt,'wt')#

#x=[py[6]]
#y=[py[9]]
#colour=['r']
#colourmap=[cm.winter]
#lab=['wt']
#strg='NF-IkB'
#ps.phaseplt(x,y,colour,colourmap,lab,xlabel='NF$\kappa$B',ylabel='I$\kappa$B',path='../../graphics/phaseplot'+strg+'.png',DPI=500)
##kwargs: title,style,xlabel,ylabel,label,xlim,path,DPI##

restore=load('../../anres/evresults2018-07-25.npz')
dy=restore['y']
DY=restore['Y']
s.evplt(dy,DY)