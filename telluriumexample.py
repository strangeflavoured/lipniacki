import tellurium as te
import matplotlib.pyplot as plt
plt.rcParams["backend"] = "TkAgg"
import numpy as np
#import matplotlib.animation as animation


#model laden
r = te.loada('paper.txt')

#integrator laden und einstellen
r.getIntegrator().setValue('relative_tolerance',0.005)
r.setIntegrator('rk45')

#parametersets und auswahl so noetig

#parset=input('Parameter: ')

#dictionary mit sets; dimension!
#dc={'name1':[1,2,3]}
#definition der parameter
#par=dc[parset]
#r.parameter=par[nummer]

#simuliert einfach fuer eingegebene Parameter
r.reset()

#waelt variablen fuer resultliste
r.timeCourseSelections=['T','E']

result=r.simulate(0,2000,2000) #anfang,ende,schritte

#ploteinstellungen
fig, ax=plt.subplots(nrows=1,ncols=1)
plt.style.use('seaborn-darkgrid')
ax.plot(result[:,0],result[:,1:],label='T0=%s'%1)
ax.legend()
ax.set_xlim([0,25])
ax.set_xlabel('Targets')
ax.set_ylabel('Effectors') 
ax.legend(loc='upper right')
fig.tight_layout()
plt.savefig('fig.png')
plt.show()