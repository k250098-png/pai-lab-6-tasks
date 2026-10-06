import numpy as np

A = np.array([[4, 3], [2, 1]])
B = np.array([[1, 2], [3, 4]])

print("Shape of A:", A.shape)
print("Shape of B:", B.shape)
print("Addition:\n", A + B)
print("Subtraction:\n", A - B)
print("Element-wise Multiplication:\n", A * B)
print("Matrix Multiplication (@):\n", A @ B)
print("Transpose of A:\n", A.T)
print("Transpose of B:\n", B.T)
print("Determinant of A:", np.linalg.det(A))
print("Determinant of B:", np.linalg.det(B))
print("Inverse of A:\n", np.linalg.inv(A))
print("Inverse of B:\n", np.linalg.inv(B))
