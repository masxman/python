import numpy as np

# Creating a 1D array
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

# Creating a 2D array
nparray = np.array([[1,2,3],[11,22,33],[4,5,6],[8,9,10],[20,30,40]])
print(nparray)

# Summing column-wise
output = nparray.sum(axis=1)
print("\n\nSum column-wise:", output)

# Checking the shape of an array
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)

# Checking the data type of an array
arr = np.array([1,2,3,4])
print(arr.dtype)
