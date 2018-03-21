""""Performing basic array operations in numpy"""
import numpy as np

# initializing a basic numpy array
print("\nBASIC NUMPY ARRAY")
print("--------------------------")

ARR = np.array([1, 2, 3])
print("array 'ARR': ", ARR)
print("ARR[1]:      ", ARR[1])

# multi-dimensional numpy arrays
print("\nMULTI-DIMENSIONAL ARRAYS")
print("--------------------------")
#ARR = np.arange(12).reshape(4,3)
ARR = np.array([[1, 2, 7], [3, 4, 8], [5, 6, 9]])
print("array 'ARR':\n", ARR)
print("Number of dimensions:    ", ARR.ndim)
print("Shape of array:          ", ARR.shape)
print("Number of elements:      ", ARR.size)
print("Type of each element:    ", ARR.dtype)
print("Size of each element:    ", ARR.itemsize)

# zeroed or oned numpy arrays
print("\nZEROED & ONED ARRAYS")
print("--------------------------")
ARR = np.zeros((3, 4), dtype=int)
print("array 'ARR':\n", ARR)
ARR = np.ones((3, 4))
print("\narray 'ARR':\n", ARR)

# create a ranged array
print("\nRANGED ARRAYS")
print("--------------------------")
ARR = np.arange(13)
print("array 'ARR':\n", ARR)
ARR = np.arange(1, 14)
print("\narray 'ARR':\n", ARR)
ARR = np.arange(0, 100, 5)
print("\narray 'ARR':\n", ARR)
#linear sequence of numbers
ARR = np.linspace(1, 95, 20, dtype=int)
print("\narray 'ARR':\n", ARR)
