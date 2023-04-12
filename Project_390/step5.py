import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import h5py
from sklearn import preprocessing


# #INPUT DATA USING HDF5 (maybe use different sets?)
processed_df = h5py.File('./output_data/data.h5', 'r+')['dataset/training/Processed_Data']
with h5py.File('./output_data/data.h5', 'r+') as f:
    # # Open the source and destination datasets

    for i in range(len(processed_df)):
        data = pd.DataFrame(processed_df[i])
        feature_data = data.iloc[:, 0:-1]
        features = pd.DataFrame(columns=['mean', 'std', 'min', 'max', 'skew'])
        window_size = 31
        features['mean'] = feature_data.rolling(window = window_size).mean()
        # features['std'] = data.iloc[:, 1:-1].rolling(window = window_size).std()
        # features['min'] = data.iloc[:, 1:-1].rolling(window = window_size).min()
        # features['max'] = data.iloc[:, 1:-1].rolling(window = window_size).max()
        # features['skew'] = data.iloc[:, 1:-1].rolling(window = window_size).skew()
        print(features)


    # train_df = f['dataset/training/Train_Data']
    f.create_dataset('dataset/training/Processed_Data', data=features)

# features = trained_data.agg(['min', 'max', 'mean', 'median', 'var', 'skew', 'std'])
# features.columns = ['_'.join(col).strip() for col in features.columns.values]

# print(features)

# # DROP NAN VALUES
# features = features.dropna()

# # OUTPUT DATA
# features.to_csv('output_data/train_features.csv', index=False)

# # #EXPORT BACK TO HDF5
# # with h5py.File('output_data/data.h5', 'a') as hdf:
    
# #     group = hdf['/dataset/training']
# #     dataset = group.create_dataset('Features', data=features.to_numpy())
    