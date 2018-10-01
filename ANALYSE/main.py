import numpy as np

from setting import analyse as ana, show, evaluate as ev
import results as res

ana('../../simres/results2018-08-02.npz',mode='mean')
ev('../../simres/results2018-08-02.npz',mode='mean')

#show('../../anres/anresults2018-07-25.npz')