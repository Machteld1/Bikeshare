import numpy as np
# Let's create a rank 2 ndarray
X = np.random.randint(1,20, size=(50,5))
print("Shape of X is: ", X.shape)
print(X)

# Create a rank 1 ndarray that contains a randomly chosen 10 values between `0` to `len(X)` (50)
# The row_indices would represent the indices of rows of X
row_indices = np.random.randint(0,50, size=10)
print("Random 10 indices are: ", row_indices)
# To Do 1 - Print those rows of X whose indices are represented by entire row_indices ndarray
# Hint - Use the row_indices ndarray to select specified rows of X
X_subset = X[row_indices, :]
print(X_subset)
indices = np.array([1,3])
print('indices = ', indices)
print()
