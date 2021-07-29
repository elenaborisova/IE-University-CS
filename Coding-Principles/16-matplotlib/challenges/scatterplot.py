import numpy as np
import matplotlib.pyplot as plt

x1 = 10 * np.random.rand(40)
x2 = 10 * np.random.rand(40) + 25
x3 = 25 * np.random.rand(20)
x = np.concatenate((x1, x2, x3))

y1 = 10 * np.random.rand(40)
y2 = 10 * np.random.rand(40) + 25
y3 = 25 * np.random.rand(20)
y = np.concatenate((y1, y2, y3))

plt.scatter(x, y, s=[200], marker='*', c='b')
plt.show()
