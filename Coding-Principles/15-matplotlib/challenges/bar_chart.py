import matplotlib.pyplot as plt

values = [5, 8, 9, 10, 4]
widths = [0.7, 0.8, 0.7, 0.7, 0.7]
colors = ['r', 'b', 'g', 'y', 'm']

ax = plt.axes()
ax.set_xticks([0, 1, 2, 3, 4])
ax.set_xticklabels(['red', 'blue', 'green', 'yellow', 'magenta'])

plt.title('Favourite Colors')
plt.xlabel('Colors')
plt.ylabel('Ages')

plt.bar(
    range(5),
    values,
    width=widths,
    color=colors,
    align='center',
)

plt.show()
