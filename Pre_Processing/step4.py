import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import preprocessing

# INPUT DATA SET
train = pd.read_csv('train.csv')
train.plot()
window_size = 31

filtered_train = train.rolling(window_size, center=True).mean()

filtered_train.plot()
plt.show()

filtered_train.to_csv('train_filtered.csv', index=False)

