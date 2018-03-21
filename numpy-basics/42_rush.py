""" PART 1 OF RUSH_NUMPY """
import numpy as np
import matplotlib.pyplot as pyplot

print("PART 1")
print("---------------------")

print("1. Create a matrix of random values of a distribution of your choice.")
ARR = np.random.randint(10, size = (3, 3))
print(ARR)

print("2. Create a 1-dimensional array of 12 sequential numbers and convert it to a 4x3 array.")
ARR = np.arange(12).reshape(4, 3)
print(ARR)

print("3. Write a function that creates an incremental N-dimensional (nd) array of dimension (1,n) with values between 0 and 1. Use arr.shape to verify")
def create_array(n=2):
    return np.linspace(0, 1, n).reshape(1, n)
ARR = create_array(3)
print(ARR)
print(type(ARR))
print(ARR.shape)

print("4. Generate a 10x12 array and extract row 0-4 of columns 8-12.")
TMP = np.random.randint(10, size=(10, 12))
ARR = TMP[0:5, 7:13]
print(TMP)
print(ARR)

print("5. Using the function in Q3, get m vectors and bind them together (to have a m x n) matrix. Plot the matrix with matplotlibs imshow")
def create_matrix(m, n):
    matrix = [create_array(n) for i in range(m)]
    return np.vstack(matrix)

ARR = create_matrix(3, 3)
print(ARR)
# pyplot.imshow(ARR)
print("6. Multiply the resulting matrix from Q5 with the matrix of a picture of your choice. Plot the resulting matrix.")
IMG = pyplot.imread('assets/img.png')
print(IMG)
print(IMG.shape)
