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
    mn=[0.014072925476425044,
    0.005034594435496627,
    0.18068921043762995,
    5.569496439148367e-05,
    0.00048555177347776385,
    0.005692455507044586,
    0.09685803946315466,
    0.15245472383590417,
    0.00010987602925388629,
    0.015192373854791223,
    0.002831629232167119,
    0.00010987602925388629,
    0.0341747527371434,
    0.001378160448516852]
    if args:
        a=[]
        for i in args:
            a.append(mn[i])
        a=np.stack(a)
        return a
    else:
        return np.stack(mn)

def meanKO(*args):
    mn=[0.015002015291045393,
    0.020537492327414527,
    0.16395790578122652,
    0.0005084571506466522,
    0.0007527441377600515,
    0.007427596110784487,
    0.2312892937030016,
    0.0,
    0.0,
    0.0161152676776444,
    0.0007251199935555095,
    0.00024810084629787305,
    0.005246285896797676,
    0.0015775755702848655]
    if args:
            a=[]
            for i in args:
                a.append(mn[i])
            a=np.stack(a)
            return a
    else:
        return np.stack(mn)

def mean24(*args):
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

def mean24KO(*args):
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

def pymax(*args):#max der simulation
    mx=[0.1999999999999998,
    0.08089627112811425,
    0.18922639487399606,
    0.0002324936229081099,
    0.006369140961230574,
    0.04758048244304242,
    0.2797994808147606,
    0.18421052142060007,
    0.0001917566106792885,
    0.0358453042514447,
    0.0191610929627825,
    0.0001917566106792885,
    0.05325671952227655,
    0.0033880406271132547]
    if args:
            a=[]
            for i in args:
                a.append(mx[i])
            a=np.stack(a)
            return a
    else:
        return np.stack(mx)

def median(*args):
    md=[0.009523809523809526,
    0.0012498410830373017,
    0.18922368538735926,
    3.390905124063913e-05,
    0.0004677915925478408,
    0.005120052818053156,
    0.08364024225144856,
    0.17425050379166204,
    0.00010455030258472008,
    0.01356532306104528,
    0.001530379743745633,
    0.00010455030258472008,
    0.037428103630962634,
    0.0012800133062893255]
    if args:
            a=[]
            for i in args:
                a.append(md[i])
            a=np.stack(a)
            return a
    else:
        return np.stack(md)

def medianKO(*args):
    md=[0.009523809523809526,
    0.014652014572830567,
    0.17581485082355638,
    0.0005457735301902752,
    0.0008599377515377297,
    0.007290002615469068,
    0.22808227858518373,
    0.0,
    0.0,
    0.018624542366917157,
    0.0007990499581103953,
    0.0002851028156494503,
    0.005869097678575827,
    0.0018224884062606932]
    if args:
            a=[]
            for i in args:
                a.append(md[i])
            a=np.stack(a)
            return a
    else:
        return np.stack(md)