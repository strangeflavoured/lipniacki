import numpy as np

from setting import analyse as ana, show, evaluate as ev
import results as res

ana('../../simres/results2018-10-04.npz',mode='custom2',string='wt')
ev('../../simres/results2018-10-04.npz',mode='custom2',string='wt')

#show('../../anres/anresults2018-07-25.npz')