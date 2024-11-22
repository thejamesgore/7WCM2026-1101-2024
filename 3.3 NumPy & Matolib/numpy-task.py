# Define a matrix (A) of size 3x6 with random integer elements between -10 and 10.

# Transpose the matrix A^T and find the result of:

# A * A^T
# A^T * A

import numpy as np

matrix_a = np.random.randint(-10,10,(3,6))

matrix_t = np.transpose(matrix_a)

print("The Matrix is", matrix_a)
print("The Matrix transposed is", matrix_t)