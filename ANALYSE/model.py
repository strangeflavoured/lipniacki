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