import matplotlib.pyplot as plt

labels = ['Python', 'Java', 'C++', 'JS']
sizes = [45, 20, 15, 20]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['cyan', 'orange', 'blue', 'yellow'])
plt.title("Programming Language Usage")
plt.show()