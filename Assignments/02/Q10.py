import numpy as np

def normalize_array(arr):
    mean = np.mean(arr)
    standardDeviation = np.std(arr)
    narr = (arr - mean) / standardDeviation
    return narr

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
normalized = normalize_array(arr)

print("Original Array:", arr)
print("Normalized Array:", normalized)