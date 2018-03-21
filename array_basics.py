""""Performing basic array operations in numpy"""
import numpy as np

# INITIALIZING A BASIC NUMPY ARRAY
print("\nBASIC NUMPY ARRAY")
print("--------------------------")

ARR = np.array([1, 2, 3])
print("array 'ARR': ", ARR)
print("ARR[1]:      ", ARR[1])

# MULTI-DIMENSIONAL NUMPY ARRAYS
print("\nMULTI-DIMENSIONAL ARRAYS")
print("--------------------------")
ARR = np.array([[1, 2, 7], [3, 4, 8], [5, 6, 9]])
print("array 'ARR':\n", ARR)
print("Number of dimensions:    ", ARR.ndim)
print("Shape of array:          ", ARR.shape)
print("Number of elements:      ", ARR.size)
print("Type of each element:    ", ARR.dtype)
print("Size of each element:    ", ARR.itemsize)

# ZEROED OR ONED NUMPY ARRAYS
print("\nZEROED & ONED ARRAYS")
print("--------------------------")
ARR = np.zeros((3, 4), dtype=int)
print("array 'ARR':\n", ARR)
ARR = np.ones((3, 4))
print("\narray 'ARR':\n", ARR)

# CREATE A RANGED ARRAY
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

# SHAPING ARRAYS
print("\nSHAPING ARRAYS")
print("--------------------------")
ARR = np.arange(6).reshape(2, 3)
print("array 'ARR':\n", ARR)
print("numpy array:     ", ARR.shape)
# shaping returns a new array, so original remains unchanged
ARR.reshape(6, 1)
print("array 'ARR':\n", ARR)
print("numpy array:     ", ARR.shape)
print("array 'ARR':\n", ARR.reshape(6, 1))
print("numpy array:     ", ARR.shape)
print("array 'ARR':\n", ARR.ravel())
print("numpy array:     ", ARR.shape)
print("array 'ARR':\n", ARR)
print("numpy array:     ", ARR.shape)

# OPERATIONS ON ARRAYS
print("\nOPERATIONS ON ARRAYS")
print("--------------------------")
ARR = np.array([[1, 5, 2], [4, 3, 0]])
print("array 'ARR':\n", ARR)
print("min element in array:    ", ARR.min())
print("max element in array:    ", ARR.max())
print("sum of all elements:     ", ARR.sum())
print("sum of axis0 (columns):  ", ARR.sum(axis=0))
print("sum of axis1 (rows):     ", ARR.sum(axis=1))
print("standard deviation:      ", np.std(ARR))
print("sqr root of each element:\n", np.sqrt(ARR))

# OPERATIONS ON TWO ARRAYS
print("\nOPERATIONS ON TWO ARRAYS")
print("--------------------------")
ARR_A = np.array([[1, 2], [3, 4]])
ARR_B = np.array([[5, 6], [7, 8]])
print("array 'ARR_A:\n", ARR_A)
print("array 'ARR_B:\n", ARR_B)
print("\nARR_A + ARR_B:\n", ARR_A + ARR_B)
print("ARR_A * ARR_B:\n", ARR_A * ARR_B)
print("ARR_A / ARR_B:\n", ARR_A / ARR_B)
print("ARR_A.dot(ARR_B):\n", ARR_A.dot(ARR_B))
