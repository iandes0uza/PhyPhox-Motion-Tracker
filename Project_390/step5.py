import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import h5py
from sklearn import preprocessing

window_size = 500
# #INPUT DATA USING HDF5 (maybe use different sets?)
df_train = h5py.File('./output_data/data.h5', 'r+')['dataset/training/Processed_Data']
with h5py.File('./output_data/data.h5', 'r+') as f:

    for i in range(len(df_train)):
        data = pd.DataFrame(df_train[i])
        feature_data = data
        features = pd.DataFrame(columns=['max', 'min', 'mean', 'median', 'var', 'skew', 'std', 'kurt'])
        # print(feature_data)
        features['max'] = feature_data.iloc[1:,1].rolling(window=window_size).max()
        features['min'] = feature_data.iloc[1:,1].rolling(window=window_size).min()
        features['mean'] = feature_data.iloc[1:,1].rolling(window=window_size).mean()
        features['median'] = feature_data.iloc[1:,1].rolling(window=window_size).median()
        features['var'] = feature_data.iloc[1:,1].rolling(window=window_size).var()
        features['skew'] = feature_data.iloc[1:,1].rolling(window=window_size).skew()
        features['std'] = feature_data.iloc[1:,1].rolling(window=window_size).std()
        features['kurt'] = feature_data.iloc[1:,1].rolling(window=window_size).kurt()
        features.dropna()
        # features = pd.DataFrame(columns=['mean', 'std', 'min', 'max', 'skew'])
        # window_size = 31
        print(features)
        # features['mean'] = feature_data[:, 0].rolling(window = window_size).mean()
        # # features['std'] = feature_data[:, 0].rolling(window = window_size).std()
        # # features['min'] = feature_data[:, 0].rolling(window = window_size).min()
        # # features['max'] = feature_data[:, 0].rolling(window = window_size).max()
        # # features['skew'] = feature_data[:, 0].rolling(window = window_size).skew()

        # print(feature_data)

        # # train_df = f['dataset/training/Train_Data']
        # f.create_dataset('dataset/training/Processed_Data', data=features)

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
    