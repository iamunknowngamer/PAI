import pandas as pd
import matplotlib.pyplot as plt

dataset = {
    'Name': ['Raghib', 'Fahad', 'Abdul Rahman', 'Umar', 'Talha', 'Saif', 'Adina', 'Sara', 'Hafsa', 'Arwa'],
    'Sci': [50, 80, 40, 50, 40, 85, 84, 95, 95, 85],
    'Maths': [100, 58, 85, 48, 58, 75, 82, 99, 85, 95]
}

df = pd.DataFrame(dataset)

plt.scatter(df['Name'], df['Sci'], color='blue', label='Science')

plt.scatter(df['Name'], df['Maths'], color='pink', label='Maths')

plt.xlabel('Student Names')
plt.ylabel('Scores')
plt.title('Science and Maths Scores')
plt.xticks(rotation=45)
plt.legend()
plt.show()
