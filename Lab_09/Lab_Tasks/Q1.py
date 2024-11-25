import matplotlib.pyplot as plt

name = ['Raghib','Fahad','Umar','Abdul Rahman','Talha','Saif','Adina','Sara','Hafsa','Arwa']

Height = [80,58,84,95,70,100,80,75,80,100]

colors = ['g','b','r','y','black','m']
plt.bar(name,Height,width=0.5,color=colors) 
plt.xlabel('Names',fontsize= 20)
plt.ylabel('Marks',fontsize= 20)
plt.xticks(rotation=30)

plt.show()
