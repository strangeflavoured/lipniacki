import numpy as np

from setting import analyse as ana, show, evaluate as ev
import results as res

ana('../../simres/resultsA20KO2019-01-03.npz',mode='custom2',string='KO')
ev('../../simres/resultsA20KO2019-01-03.npz',mode='custom2',string='KO')

#show('../../anres/anresults2018-07-25.npz')