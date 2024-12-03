import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
iris = load_iris()
X = iris.data  # Features (sepal length, sepal width, petal length, petal width)
y = iris.target  # Target labels (not used in unsupervised learning)

# Step 2: Apply KMeans
kmeans = KMeans(n_clusters=3, random_state=42)  # We know there are 3 classes in the Iris dataset
kmeans.fit(X)  # Fit the model to the data

# Step 3: Get cluster labels and centroids
labels = kmeans.labels_  # Cluster labels for each data point
centroids = kmeans.cluster_centers_  # Centroids of the clusters

# Step 4: Evaluate performance (using silhouette score)
silhouette_avg = silhouette_score(X, labels)
print("Silhouette Score:", silhouette_avg)

# Step 5: Visualize the clusters
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=labels, palette='viridis', s=100)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label="Centroids")
plt.title("KMeans Clustering (Iris Dataset)")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.legend()
plt.show()

# Step 6: Compare predicted clusters with actual classes (for visualization purposes)
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=y, palette='Set1', style=labels, s=100)
plt.title("Actual vs Predicted Classes (Iris Dataset)")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.legend()
plt.show()

#elbow method
inertia = []
K_range = range(1, 11)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

plt.plot(K_range, inertia, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.show()
