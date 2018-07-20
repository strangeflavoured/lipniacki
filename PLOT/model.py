#   ##############################################################
#    #         Function includes system of ODEs describing       #
#    #         NF-kB regulatory pathway. System                  #
#    #         includes A20 gene products action as a            #
#    #         inhibitor of active IKK.                          #    
#    #         Other protein and compexes are coded as follows:  #
#    #                                                           #  
#    #         y[0]   IKKn   neutral                             #    
#    #         y[1]   IKKa   active                              #
#    #         y[2]   IKKi   inactive                            #
#    #         y[3]   (IKKa|IkBa)                                #
#    #         y[4]   (IKKa|IkBa|NFkB)                           #
#    #         y[5]   NFkB                                       #
#    #         y[6]   NFkBn                                      #
#    #         y[7]   A20                                        #
#    #         y[8]   A20t                                       #
#    #         y[9]  IkBa                                        #
#    #         y[10]  IkBan                                      #
#    #         y[11]  IkBat                                      #      
#    #         y[12]  (IkBa|NFkB) cytoplasmic                    #  
#    #         y[13] (IkBan|NFkBn) nuclear                       #        
#    #                                                           #
#    #############################################################

import numpy as np

def limit1(*args):
    lim=[9.52380952e-03, 1.24984047e-03, 1.89226350e-01, 3.39089784e-05,
    4.67791580e-04, 5.12005325e-03, 8.36402420e-02, 1.74250504e-01,
    1.04550302e-04, 1.35653230e-02, 1.53037973e-03, 1.04550302e-04,
    3.74281041e-02, 1.28001331e-03]
    if args:
        a=[]
        for i in args:
            a.append(lim[i])
        a=np.stack(a)
        return a
    else:
        return np.stack(lim)

def limit0(*args):
    lim=[2.00000000e-01, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
    0.00000000e+00, 3.15505471e-04, 2.29576678e-03, 4.78284745e-03, 2.86970847e-06,
    2.50662918e-03, 3.43573096e-03, 2.86970847e-06, 5.92095860e-02, 7.87758754e-05]
    if args:
        a=[]
        for i in args:
            a.append(lim[i])
        a=np.stack(a)
        return a
    else:
        return np.stack(lim)

def limitKO(*args):
    lim=[0.00952381, 0.01465201, 0.17582418, 0.00054577, 0.00085994, 0.00729001,
    0.22808225, 0., 0.,0.01862454, 0.00079905, 0.0002851,0.0058691,  0.0018225 ]
    if args:
        a=[]
        for i in args:
            a.append(lim[i])
        a=np.stack(a)
        return a
    else:
        return np.stack(lim)