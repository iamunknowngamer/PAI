import matplotlib.pyplot as plt

name = ['Krachi','Lahore','islamabad','Peshawar','NawabShah','Larkana','Hyderabad','Maree']

Population = [80,58,84,95,70,100,80,75]

plt.barh(name,Population) 
plt.xlabel('Names',fontsize= 20)
plt.ylabel('Marks',fontsize= 20)
plt.xticks(rotation=30)

plt.show()
