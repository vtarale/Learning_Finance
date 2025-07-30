import numpy as np

# 1 dimensional array
array_1d = np.array([1, 2, 3, 4])

# 2 dimensional array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:\n", array_2d)

# slicing arrays
slice_1d = array_1d[0::3]  
print("Sliced 1D Array:", slice_1d)

slice_2d = array_2d[::2]  
print("Sliced 2D Array:\n", slice_2d)

# element-wise arthimetic operations
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
print("Addition:", array_a + array_b)
print("Subtraction:", array_a - array_b)
print("Multiplication:", array_a * array_b)
print("Division:", array_a / array_b)

# boradcasting
scalar = 2
print("Array + Scalar:", array_a + scalar)
print("Matirx + array:", array_2d + array_a)

#statistical functions
print("Mean of 1D Array:", np.mean(array_1d))
print("Standard Deviation of 1D Array:", np.std(array_1d))
print("Variance of 1D Array:", np.var(array_1d))
print("Sum of 1D Array:", np.sum(array_1d))

# matrix operations
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
print("Matrix Multiplication:\n", np.dot(matrix_a, matrix_b))
print("Inverse of 2D Array:\n", np.linalg.inv(array_2d))