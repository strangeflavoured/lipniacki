import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10
plt.style.use('seaborn-paper')
fig = plt.figure()
ax = fig.gca(projection='3d')
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = 200*r * np.sin(np.pi*z)
y = r * np.tan(z)
ax.grid(False)
ax.plot(z,np.full((100,),0),x, label='parametric curve 1')
ax.plot(z,np.full((100,),1),y, label='parametric curve 2')
ax.legend()
ax.zaxis._axinfo['juggled'] = (1,2,0)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

#fig.patch.set_alpha(0.)

plt.show()