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
    0.00000000e+00, 3.15505483e-04, 2.29576678e-03, 4.78284745e-03,
    2.86970847e-06, 2.50662918e-03, 3.43573096e-03, 2.86970847e-06,
    5.92095582e-02, 7.89149811e-05]
    if args:
        a=[]
        for i in args:
            a.append(lim[i])
        a=np.stack(a)
        return a
    else:
        return np.stack(lim)

def limitKO(*args):
    lim=[0.00952381, 0.01465201, 0.17582418, 0.00054578, 0.00085994, 0.00729,
    0.22808224,0.,0.,0.01862454,0.00079904,0.0002851,0.0058691,0.00182252]
    if args:
        a=[]
        for i in args:
            a.append(lim[i])
        a=np.stack(a)
        return a
    else:
        return np.stack(lim)

def meanpy(*args):
    mn=[0.010789583777066793,
    0.0023029010928785443,
    0.18684839315435764,
    3.997413199367154e-05,
    0.0004727740136379802,
    0.005279228907067431,
    0.08729672300955137,
    0.1681909915145243,
    0.00010603615193516456,
    0.014019694739051985,
    0.0018930209617240641,
    0.00010603615193516456,
    0.03652715863953239,
    0.001307469189261111]
    if args:
        a=[]
        for i in args:
            a.append(mn[i])
        a=np.stack(a)
        return a
    else:
        return np.stack(mn)

def meanKO(*args):
    mn=[0.011024249766569676,
    0.016264004531803156,
    0.17256368664810606,
    0.0005355530461919283,
    0.000830580107941398,
    0.007327691024129917,
    0.22896065049771938,
    0.0,
    0.0,
    0.017937270143624378,
    0.0007788069895090412,
    0.00027496821420143936,
    0.005698516068356846,
    0.0017554135001379215]
    if args:
            a=[]
            for i in args:
                a.append(mn[i])
            a=np.stack(a)
            return a
    else:
        return np.stack(mn)