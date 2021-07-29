import matplotlib.pyplot as plt


values = [0, 5, 8, 9, 2, 0, 3, 10, 4, 7]
plt.plot(range(1, 11), values)
plt.ioff()
plt.savefig('MySamplePlot.png', format='png')
