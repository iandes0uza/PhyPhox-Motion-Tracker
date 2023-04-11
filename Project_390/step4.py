import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import preprocessing

# INPUT DATA SET
train = pd.read_csv('input_data/train.csv')
# train.plot()

#NORMALIZE

# DECLARE WINDOW SIZE
window_size = 31
filtered_train = train.rolling(window_size, center=True).mean()


# filtered_train.plot()
# plt.show()

# OUTPUT DATA SET
filtered_train.to_csv('output_data/train_filtered.csv', index=False)

