import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt


start_date = dt.datetime(2021, 7, 29)
end_date = dt.datetime(2021, 8, 7)
daterange = pd.date_range(start_date, end_date)
sales = (np.random.rand(len(daterange)) * 40).astype(int)
df = pd.DataFrame(sales, index=daterange, columns=['Study time'])

df.loc['Jul 30 2021':'Aug 05 2021'].plot()
plt.ylim(0, 40)
plt.xlabel('Study date')
plt.ylabel('Study time')
plt.title('Plotting Time')
plt.show()
