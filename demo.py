import numpy as np
import matplotlib.pyplot as plt

from my_answers import *

### load in and normalize the dataset
dataset = np.loadtxt('datasets/normalized_apple_prices.csv')

# lets take a look at our time series
print(type(dataset))
print(len(dataset))

plt.plot(dataset)
plt.xlabel('time period')
plt.ylabel('normalized series value')
plt.show()