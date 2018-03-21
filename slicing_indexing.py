import numpy as np

# ARRAY SLICING IS THE SAME AS NORMAL PYTHON LIST
print("\nARRAY SLICING")
print("---------------------")
LST = [1,2, 3, 4, 6, 7, 8, 9]
print("normal python list:  ", LST)
print("LST[0]:              ", LST[0])
print("LST[4]:              ", LST[4])
print("LST[-1]:             ", LST[-1])
print("LST[0:2]:            ", LST[0:2])
print("LST[3:7]:            ", LST[3:7])
ARR = np.array([1,2, 3, 4, 6, 7, 8, 9])
print("\nnumpy array:         ", ARR)
print("ARR[0]:              ", ARR[0])
print("ARR[4]:              ", ARR[4])
print("ARR[-1]:             ", ARR[-1])
print("ARR[0:2]:            ", ARR[0:2])
print("ARR[3:7]:            ", ARR[3:7])

# MULTI-DIMENSIONAL SLICING
print("\nMULTI-DIMENSIONAL SLICING")
print("---------------------")
ARR = np.array([[6, 7, 8], [1, 2, 3], [9, 3, 2]])
print("numpy multi-dim array:\n", ARR)
print("\nARR[1, 2]:           ", ARR[1, 2])
print("ARR[0:2, 2]:         ", ARR[0:2, 2])
print("ARR[-1]:             ", ARR[-1])
print("ARR[-1, 0:2]:        ", ARR[-1, 0:2])
print("ARR[:, :]\n", ARR[:, :])
print("ARR[:, 1:3]\n", ARR[:, 1:3])

# ITERATING ARRAYS
print("\nITERATING ARRAYS")
print("---------------------")
ARR = np.array([[6, 7, 8], [1, 2, 3], [9, 3, 2]])

print("for row in ARR:")
for row in ARR:
    print(row, end=' ')

print("\n\nfor cell in ARR.flat:")
for cell in ARR.flat:
    print(cell, end=' ')

# STACKING ARRAYS
print("\STACKING ARRAYS")
print("---------------------")
ARR_A = np.arange(6).reshape(3, 2)
ARR_B = np.arange(6, 12).reshape(3, 2)
print("numpy array 'ARR_A':\n", ARR_A)
print("numpy array 'ARR_B':\n", ARR_B)
print("np.vstack((ARR_A, ARR_B)):\n", np.vstack((ARR_A, ARR_B)))
print("np.vstack((ARR_B, ARR_A)):\n", np.vstack((ARR_B, ARR_A)))
print("np.hstack((ARR_A, ARR_B)):\n", np.hstack((ARR_A, ARR_B)))
print("np.hstack((ARR_B, ARR_A)):\n", np.hstack((ARR_B, ARR_A)))

# SPLITTING ARRAYS
print("\nSPLITTING ARRAYS")
print("---------------------")
ARR = np.arange(30).reshape(2, 15)
print("numpy array 'ARR':\n", ARR)
print("np.hsplit(ARR, 3):\n", np.hsplit(ARR, 3))
print("np.vsplit(ARR, 1):\n", np.vsplit(ARR, 1))

# INDEXING W/ BOOLEAN ARRAYS
print("\nINDEXING W/ BOOLEAN ARRAYS")
print("---------------------")
ARR_A = np.arange(12).reshape(3, 4)
print("numpy array 'ARR_A':\n", ARR_A)
ARR_B = ARR_A > 4
print("ARR_B = ARR_A > 4:\n", ARR_B)
print("ARR_A[ARR_B]:\n", ARR_A[ARR_B])
ARR_A[ARR_B] = -1
print("ARR_A[ARR_B] = -1:\n", ARR_A)

# ITERATE W/ NDITER
