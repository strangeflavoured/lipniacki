import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np 

import plotset as ps
import colours as c
import plots as s
from results import load

restore=load('../../simres/resultswt2018-11-23.npz')
##print(restore.files)
#pt=restore['ptsim']
#py=restore['pysim']
pt=restore['pt']
py=restore['py']

restore2=load('../../simres/resultsKO2018-11-23.npz')
pt2=restore2['pt']
py2=restore2['py']

###ONE AT A TIME###
#s.plainall(pt,py,'KO')
s.compall(pt,py,pt2,py2,'comp')
#s.discreet(py,pt,mode='mean')
#s.discrall(py,pt,mode='mean')
#s.normplt(py,pt)
#s.thresh(py,pt,'wt')
#s.discrnor(py,pt,mode='custom2',name='')

#s.discreetmean(py,pt)#
#s.discreetmedian(py,pt)#
#s.threshmean(py,pt,'wt')#
#s.threshmedian(py,pt,'wt')#

'''x=[py[6]]#,py2[6]]
y=[py[9]]#,py2[9]]
z=[py[1]]#,py2[1]]
a=[py[7]]#,py2[7]]
t=[pt]#,pt2]
colour=[c.navy]
colourmap=cm.autumn
marker=['o']#,'1']
lab=['wt']
strg='NF-IkB-IKK'
ps.phase3d(x,y,z,a,colour,colourmap,marker,lab,xlabel='$NF\kappa B_n \\ /\\ \mu M$',ylabel='$(I\kappa B:NF\kappa B)_c\\ /\\ \mu M$',zlabel='$\mathrm{IKK}_a\\ /\\ \mu M$',path='../../graphics/phaseplot'+strg+'.png',DPI=500)
#ps.phaseplt(x,y,t,colour,colourmap,lab,xlabel='NF$\kappa$B',ylabel='I$\kappa$B',path='../../graphics/phaseplot'+strg+'.png',DPI=500)
##kwargs: title,style,xlabel,ylabel,label,xlim,path,DPI##'''

'''restore=load('../../anres/evresultscustom22018-08-03.npz')
dy=restore['y']
DY=restore['Y']
s.evplt(dy,DY,strg='custom2')'''

'''restore=load('../../anres/evresultsA20KOcustom22018-10-04.npz')
dy=restore['y']
DY=restore['Y']
print([1,int(restore['t0'][6]),int(restore['t0'][12]),int(restore['t0'][1]),int(restore['t0'][7])])
s.evplt(dy,DY,strg='A20KOcustom2')'''