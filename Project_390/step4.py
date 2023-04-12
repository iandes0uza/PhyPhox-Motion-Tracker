import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import h5py
from sklearn import preprocessing

# INPUT DATA SET
with h5py.File('output_data/data.h5', 'r') as hdf:
    train_df = hdf['dataset/training/Train_Data']

# NORMALIZE
for sub_array in train_df:
    for element in sub_array:
        train_data = element.iloc[:, 1:3]
        sc = preprocessing.StandardScaler()
        train = sc.fit_transform(train_data)
        element = pd.DataFrame(train, columns=train_data.columns)

        # DECLARE WINDOW SIZE
        window_size = 31
        element.rolling(window_size, center=True).mean()


train_df.plot()
plt.show()

# OUTPUT DATA SET
# filtered_train.to_csv('output_data/train_filtered.csv', index=False)

