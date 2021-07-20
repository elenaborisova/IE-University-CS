import matplotlib.pyplot as plt


values = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
values2 = [3, 8, 9, 2, 1, 2, 4, 7, 6, 6]

line1 = plt.plot(range(1, 11), values)
line2 = plt.plot(range(1, 11), values2)

plt.legend(['First', 'Second'], loc=4)
plt.show()
