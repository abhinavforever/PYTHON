import matplotlib.pyplot as plt
   
country = ['A', 'B', 'C', 'D', 'E']
gdp_per_capita = [45000, 42000, 52000, 49000, 47000]

colors = ['green', 'blue', 'purple', 'brown', 'teal']
plt.bar(country, gdp_per_capita, color=colors)
plt.title('Country Vs GDP Per Capita', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.ylabel('GDP Per Capita', fontsize=14)
plt.grid(True)
plt.show()