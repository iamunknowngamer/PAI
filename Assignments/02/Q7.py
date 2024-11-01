import numpy as np

array = np.random.rand(50)
max_index = np.argmax(array)
min_index = np.argmin(array)

print(max_index, min_index)