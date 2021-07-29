import numpy as np
import matplotlib.pyplot as plt


spread = 50 * np.random.rand(50)
center = np.ones(25) * 25
flier_high = 50 * np.random.rand(10) + 50
flier_low = -50 * np.random.rand(10)
data = np.concatenate((spread, center, flier_high, flier_low))

plt.boxplot(data, sym='gx', widths=1.5, notch=False)
plt.show()
