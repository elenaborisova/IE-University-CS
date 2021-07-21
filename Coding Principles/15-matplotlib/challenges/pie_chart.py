import matplotlib.pyplot as plt

values = [35, 3, 8, 20, 29, 5]
colors = ['b', 'g', 'r', 'c', 'm', 'y']
labels = ['games', 'news', 'music and videos', 'utilities', 'social networking', 'others']
explode = (0.1, 0, 0, 0, 0, 0)

plt.pie(
    values,
    colors=colors,
    labels=labels,
    explode=explode,
    autopct='%1.1f%%',
    counterclock=False,
    shadow=True,
)

plt.title('Time spend on smartphones')

plt.show()
