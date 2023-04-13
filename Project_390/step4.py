import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import h5py
from sklearn import preprocessing

# INPUT DATA SET
# with h5py.File('output_data/data.h5', 'r') as hdf:
train_df = h5py.File('./output_data/data.h5', 'r+')['dataset/training/Train_Data']
with h5py.File('./output_data/data.h5', 'r+') as f:
    # # Open the source and destination datasets
    # train_df = f['dataset/training/Train_Data']
    processed_df = f.create_dataset('dataset/training/Processed_Data', data=train_df)

    for i in range(len(train_df)):
        # NORMALIZE
        data = pd.DataFrame(train_df[i])
        train_data = data.iloc[:, 0:-1]
        train_label = data.iloc[:, 5]
        sc = preprocessing.StandardScaler()
        train = sc.fit_transform(train_data)
        normalized_data = pd.DataFrame(train, columns=train_data.columns)

        # DECLARE WINDOW SIZE
        window_size = 31
        normalized_data.rolling(window_size, center=True).mean()

        # PUT THEM TOGETHER
        result = pd.concat([normalized_data, train_label], axis=1)
        print(result)
        processed_df[i] = result


