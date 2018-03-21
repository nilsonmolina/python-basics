"""INTRO TO NUMPY"""
import sys
import time
import numpy as np

# numpy uses less memory
SIZE = 1000

LST = range(SIZE)
print("Size of python list (1000 items): ", sys.getsizeof(14) * len(LST))

ARR = np.arange(SIZE)
print("Size of numpy array (1000 items): ", ARR.size * ARR.itemsize)

# numpy is faster
SIZE = 1000000
L1 = range(SIZE)
L2 = range(SIZE)

A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

START = time.time()
RESULT = [(x+y) for x, y in zip(L1, L2)]
print("python list took: ", (time.time() - START) * 1000)
START = time.time()
RESULT = A1 + A2
print("numpy array took: ", (time.time() - START) * 1000)
