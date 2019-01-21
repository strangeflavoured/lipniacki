import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np 

import plotset as ps
import colours as c
import plots as s
from results import load

'''restore=load('../../simres/resultswt2019-01-06.npz')
##print(restore.files)
pt=restore['pt']
py=restore['py']
#pt=restore['ptsim']
#py=restore['pysim']

restore2=load('../../simres/resultsA20KO2019-01-06.npz')
##print(restore.files)
pt2=restore2['pt']
py2=restore2['py']
#pt=restore['ptsim']
#py=restore['pysim']

'''restore=load('../../simres/resultsREV2019-01-18.npz')
##print(restore.files)
pt=restore['pt']
py=restore['py']
#pt=restore['ptsim']
#py=restore['pysim']'''


###ONE AT A TIME###
#s.plainall(pt,py,'REV')
#s.compall(pt,py,pt2,py2)
##s.discreet(py,pt,mode='mean')
##s.discrall(py,pt,mode='mean')
##s.normplt(py,pt)
##s.thresh(py,pt,'wt')
s.discrnor(py,pt,mode='custom',name='')
#s.discr(py,pt,mode='custom2',strg='A20')

#s.discreetmean(py,pt)#
#s.discreetmedian(py,pt)#
#s.threshmean(py,pt,'wt')#
#s.threshmedian(py,pt,'wt')#

'''x=[py[6]]
y=[py[9]]
colour=['r']
colourmap=[cm.winter]
lab=['wt']
strg='NF-IkB'
ps.phaseplt(x,y,colour,colourmap,lab,xlabel='NF$\kappa$B',ylabel='I$\kappa$B',path='../../graphics/phaseplot'+strg+'.png',DPI=500)
##kwargs: title,style,xlabel,ylabel,label,xlim,path,DPI##'''

'''restore=load('../../anres/evresultswtcustom22019-01-17.npz')
DY2=restore['Y']

restore3=load('../../anres/evresultsKOcustom22019-01-17.npz')
DY3=restore3['Y']

restore2=load('../../anres/evresultswtcustom2019-01-17.npz')
DY=restore2['Y']

#print([1,int(restore['t0'][6]),int(restore['t0'][12]),int(restore['t0'][1]),int(restore['t0'][7])])
s.evplt(DY,DY2,DY3,strg='ALLcustom2',start=[0,0,0,1])
#s.evplt3d(DY,DY2,DY3,strg='ALLcustom2',start=[0,0,0,1])'''

'''restore=load('../../simres/VARthreshwt2019-01-13.npz')
restore2=load('../../simres/VARthreshKO2019-01-13.npz')

mean=restore['mean']
median=restore['median']
Max=restore['max']

mean2=restore2['mean']
median2=restore2['median']
Max2=restore2['max']

colours=[[c.blood,c.deeppink],[c.navy,c.dodgerblue],[c.darkorange,c.gold],[c.green,c.lime]]
lab=[['IKK','IKK, A20 KO'],['NF$\kappa$B','NF$\kappa$B, A20 KO'],['A20','A20, A20 KO'],['I$\kappa$B','I$\kappa$B, A20 KO'],]

s.varplt(mean,colours,lab,path='../../graphics/varmean.png',title='Mean')
s.varplt(median,colours,lab,path='../../graphics/varmedian.png',title='Median')
#s.varplt(Max,Max2,colours,lab,path='../../graphics/varmax.png',title='Maximum/Minimum')'''

'''###############################################################
phase3d plot nfkb, ikb:nfkb, ikk
###############################################################'''