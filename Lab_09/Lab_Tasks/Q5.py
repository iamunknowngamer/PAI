import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Education_2.csv')

male_count = df[df['Gender'] == 'Male'].shape[0]
female_count = df[df['Gender'] == 'Female'].shape[0]

counts = [male_count, female_count]
labels = ['Male', 'Female']

plt.figure(figsize=(6, 6))
plt.pie(counts, labels=labels, autopct='%1.1f%%', colors=['skyblue', 'pink'])
plt.title('Gender Distribution Among Students')
plt.show()
