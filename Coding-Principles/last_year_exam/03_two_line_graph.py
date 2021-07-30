import matplotlib.pyplot as plt

x = [0, 3, 10, 7, 9, 5]
y = [2, 3, 4, 8, 10, 4]


plt.plot(range(0, 6), x, '--r')
plt.plot(range(0, 6), y, ':b')

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Values')

plt.grid()

plt.legend(['2021', '2022'], loc=1)
plt.show()
