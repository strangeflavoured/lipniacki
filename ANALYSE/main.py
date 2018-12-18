import numpy as np

from setting import analyse as ana, show, evaluate as ev
import results as res

ana('../../simres/resultsA20KO2018-07-25.npz',mode='custom2',string='A20KO')
ev('../../simres/resultsA20KO2018-07-25.npz',mode='custom2',string='A20KO')

#show('../../anres/anresults2018-07-25.npz')