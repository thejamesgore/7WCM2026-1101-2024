# Define a matrix (A) of size 3x6 with random integer elements between -10 and 10.

# Transpose the matrix A^T and find the result of:

# A * A^T
# A^T * A

import numpy as np

matrix_a = np.random.randint(-10,10,(2,2))

matrix_t = np.transpose(matrix_a)

print("The Matrix is", matrix_a)
print("The Matrix transposed is", matrix_t)

matrix_c = np.matmul(matrix_a,matrix_t)

matrix_d = np.matmul(matrix_t,matrix_a)

print("The matricies multiplied are: A * A^T", matrix_c)
print("     ")
print("The matricies multiplied are: A^T * A", matrix_d)