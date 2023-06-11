'''
Install cupy before running this file. 
'''

import os
import numpy as np
import time

def program():
    t_now = float(time.time())
    for i in range(10000):
        x = cp.arange(1000000).reshape(1000, 1000).astype('f')
    print("count with cupy by cuda {} \n".format(float(time.time())-t_now))

    t_now = float(time.time())
    for i in range(10000):
        x = np.arange(1000000).reshape(1000, 1000).astype('f')
    print("count with numpy by cpu {} \n".format(float(time.time())-t_now))

    os.system('pause')

try:
    os.system('nvidia-smi.exe')
    import cupy as cp
    program()

except:
    print("Cuda not avaliable")
    os.system('pause')