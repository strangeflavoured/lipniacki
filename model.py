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

def model(par,TR):

    kprod=par[0]
    kdeg1=par[1]
    k1=par[2]
    kdeg2=par[3]
    k3=par[4]
    kdeg3=par[5]
    a1=par[6]
    a1n=par[7]
    a2=par[8]
    a3=par[9]
    t1=par[10]
    t2=par[11]
    c6a=par[12]
    c5a=par[13]
    c1a=par[14]
    c3a=par[15]
    c4a=par[16]
    i1=par[17]
    e2a=par[18]
    i1a=par[19]
    e1a=par[20]
    c1=par[21]
    c3=par[22]
    c4=par[23]
    c5=par[24]
    k2=par[25]
    kv=par[26]
    c2=par[27]
    c2a=par[28]

    ##########################################################################
    ########################################################################## 
    def mod(t,y):
        dy=np.zeros(14)

        #neutral IKK
        dy[0]= kprod - kdeg1*y[0] - TR*k1*y[0]              

        #free active IKK
        dy[1]= TR*k1*y[0] - k3*y[1] - TR*k2*y[1]*y[7] - kdeg2*y[1] - a2*y[1]*y[9] + t1*y[3] - a3*y[1]*y[12] + t2*y[4] 

        #inactive IKK 
        dy[2]= k3*y[1] + TR*k2*y[1]*y[7] - kdeg3*y[2]   

        #cytoplasmic (IKK|IkBa) complex 
        dy[3]= a2*y[1]*y[9] - t1*y[3]                                                                                

        #cytoplasmic (IKK|IkBa|NFkB) complex
        dy[4]= a3*y[1]*y[12] - t2*y[4]                                                                               

        #free cytoplasmic NFkB
        dy[5]= c6a*y[12] - a1*y[5]*y[9] + t2*y[4] - i1*y[5]                                                          

        #free nuclear NFkB
        dy[6]=i1*kv*y[5] - a1n*y[10]*y[6]                                                                            

        #cytoplasmic A20
        dy[7]= c4*y[8] - c5*y[7]                                                                                      

        #A20 transcription
        dy[8]= c2 + c1*y[6] - c3*y[8]                                                                              

        #free cytoplasmic IkBa
        dy[9]=-a2*y[1]*y[9] - a1*y[9]*y[5] + c4a*y[11] - c5a*y[9] - i1a*y[9] + e1a*y[10]                      

        #free nuclear IkBan
        dy[10]=-a1n*y[10]*y[6] + i1a*kv*y[9] - e1a*kv*y[10]                                                  

        #IkB transcription
        dy[11]= c2a + c1a*y[6] - c3a*y[11]                                                                    

        #cytoplasmic (IkBa|NFkB) complex
        dy[12]= a1*y[9]*y[5] - c6a*y[12] - a3*y[1]*y[12] + e2a*y[13]                                         

        #Nuclear (IkBa|NFkB) complex
        dy[13]= a1n*y[10]*y[6] - e2a*kv*y[13]

        return dy

    return mod