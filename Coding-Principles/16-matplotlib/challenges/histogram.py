import numpy as np
import matplotlib.pyplot as plt


x = 20 * np.random.randn(5000)
print(x)

plt.hist(x, 25, range=(-100, 100), histtype='stepfilled', align='mid', color='pink', label='Random Test Data')
plt.legend()
plt.title('Step Filled Histogram')
plt.show()
