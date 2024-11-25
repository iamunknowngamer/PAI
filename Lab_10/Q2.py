import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("WineQT.csv")

plt.figure(figsize=(10, 10))
sns.heatmap(df.isnull(), cmap='viridis', cbar=False)
plt.title('Missing Values Heatmap')
plt.show()

df_melted_box = df.melt(value_vars=df.select_dtypes(include=['float64', 'int64']).columns)
plt.figure(figsize=(12, 6))
sns.boxplot(x='variable', y='value', data=df_melted_box)
plt.title('Boxplot of All Numerical Features')
plt.xticks(rotation=45)
plt.show()

df_melted_hist = df.melt(value_vars=df.select_dtypes(include=['float64', 'int64']).columns)
plt.figure(figsize=(12, 6))
sns.histplot(df_melted_hist, x='value', hue='variable', multiple='stack', bins=30, kde=True)
plt.title('Distribution of All Numerical Features')
plt.show()

plt.figure(figsize=(10, 10))
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Correlation Matrix')
plt.show()

plt.figure()
sns.scatterplot(data=df)
plt.title("Scatter plot of Wine")
plt.show()

plt.figure(figsize=(10, 10))
sns.boxplot(data=df)
plt.title("Box Plot of All Features")
plt.show()
