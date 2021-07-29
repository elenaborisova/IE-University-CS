import matplotlib.pyplot as plt


values = [1, 5, 2, 5, 2]
values2 = [3, 4, 5, 7, 3]

ticks = [1, 2, 3, 4, 5]
labels = ['week 1', 'week 2', 'week 3', 'week 4', 'week 5']

plt.title('Wage earning during 5-week period')
plt.xlabel('Weeks')
plt.ylabel('Wage (100$)')
plt.xticks(ticks, labels)

plt.plot(range(1, 6), values)
plt.plot(range(1, 6), values2)

plt.legend(['Household 1', 'Household 2'], loc=4)

plt.show()
