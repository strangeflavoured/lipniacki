import numpy as np

from setting import analyse as ana, show, evaluate as ev
import results as res

ana('../../simres/resultswt2019-01-06.npz',mode='custom2',string='wt')
ev('../../simres/resultswt2019-01-06.npz',mode='custom2',string='wt')

#show('../../anres/anresults2018-07-25.npz')