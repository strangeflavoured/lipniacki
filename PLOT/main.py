import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np 

import plotset as ps
import colours as c
import plots as s
from results import load

'''restore=load('../../simres/results2018-10-04.npz')
##print(restore.files)
pt=restore['pt']
py=restore['py']
pt=restore['ptsim']
py=restore['pysim']'''

'''###ONE AT A TIME###
s.plainall(pt,py,'wt')
#s.discreet(py,pt,mode='mean')
#s.discrall(py,pt,mode='mean')
#s.normplt(py,pt)
#s.thresh(py,pt,'wt')
#s.discrnor(py,pt,mode='custom2',name='')

#s.discreetmean(py,pt)#
#s.discreetmedian(py,pt)#
#s.threshmean(py,pt,'wt')#
#s.threshmedian(py,pt,'wt')#'''

'''x=[py[6]]
y=[py[9]]
colour=['r']
colourmap=[cm.winter]
lab=['wt']
strg='NF-IkB'
ps.phaseplt(x,y,colour,colourmap,lab,xlabel='NF$\kappa$B',ylabel='I$\kappa$B',path='../../graphics/phaseplot'+strg+'.png',DPI=500)
##kwargs: title,style,xlabel,ylabel,label,xlim,path,DPI##'''

'''restore=load('../../anres/evresultswtcustom22018-10-04.npz')
dy=restore['y']
DY=restore['Y']
#print([1,int(restore['t0'][6]),int(restore['t0'][12]),int(restore['t0'][1]),int(restore['t0'][7])])
s.evplt(dy,DY,strg='custom2')'''

restore=load('../../simres/VARthreshwt2018-12-18.npz')
restore2=load('../../simres/VARthreshKO2018-12-18.npz')

mean=restore['mean']
median=restore['median']
Max=restore['max']

mean2=restore2['mean']
median2=restore2['median']
Max2=restore2['max']

colours=[[c.blood,c.deeppink],[c.navy,c.dodgerblue],[c.darkorange,c.gold],[c.green,c.lime]]
lab=[['IKK, wt','IKK, A20 KO'],['NF$\kappa$B, wt','NF$\kappa$B, A20 KO'],['A20, wt','A20, A20 KO'],['I$\kappa$B, wt','I$\kappa$B, A20 KO'],]

s.varplt(mean,mean2,colours,lab,path='../../graphics/varmean.png',title='Mean')
s.varplt(median,median2,colours,lab,path='../../graphics/varmedian.png',title='Median')
s.varplt(Max,Max2,colours,lab,path='../../graphics/varmax.png',title='Maximum/Minimum')