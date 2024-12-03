import numpy as np

# Example vectors
A = np.array([1, 2, 3]) 
B = np.array([4, 5, 6])

# Calculate cosine similarity
cosine_similarity = round(np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B)), 2)

print("Cosine Similarity:", cosine_similarity)
