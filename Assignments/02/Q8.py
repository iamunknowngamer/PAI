import numpy as np

A = np.array([[2, 3, 1],
              [4, 1, -2],
              [-3, 2, 3]])

B = np.array([1, -2, 3])
X = np.linalg.solve(A, B)

print(X)