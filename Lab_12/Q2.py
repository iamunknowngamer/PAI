import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits
import seaborn as sns

digits = load_digits()

pixels = pd.DataFrame(digits.data)

labels = digits.target

single_image = pixels.iloc[0]

image_array = single_image.to_numpy()

image_reshaped = image_array.reshape(8, 8)

plt.figure(figsize=(6, 6))
plt.imshow(image_reshaped, cmap='gray')  # cmap='gray' for grayscale images
plt.axis('off')  # Turn off axis
plt.show()

scaler = StandardScaler()
pixels_scaled = scaler.fit_transform(pixels)

pca = PCA(n_components=2)
pixels_pca = pca.fit_transform(pixels_scaled)

print(f"Explained variance by the first 2 components: {pca.explained_variance_ratio_}")
print(f"Total variance explained by 2 components: {np.sum(pca.explained_variance_ratio_):.2f}")

plt.figure(figsize=(8, 6))
sns.scatterplot(x=pixels_pca[:, 0], y=pixels_pca[:, 1], hue=labels, palette='tab10', s=100, marker='o', legend='full')
plt.title("PCA of Digits Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(title="Digit Label")
plt.show()
