import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import h5py
from sklearn import preprocessing


# #INPUT DATA USING HDF5 (maybe use different sets?)
# with h5py.File('input_data/data.h5', 'r') as hdf:
#     trained_data = hdf['/dataset/training/Train_Data']
#     print(trained_data)
#     print("MEOW MEOW MEOW\n\n\n\n\n\n\n")
    

trained_data = pd.read_csv('train.csv')
print(trained_data)
#HAVE A PREDETERMINED WINDOW SIZE
window_size = 31

# Compute the statistical features for each group
features = trained_data.agg(['min', 'max', 'mean', 'median', 'var', 'skew', 'std'])

# Flatten the column names to remove the hierarchical index
features.columns = ['_'.join(col).strip() for col in features.columns.values]
print(features)

features = features.dropna()

features.to_csv('train_features.csv', index=False)

# #EXPORT BACK TO HDF5
# with h5py.File('output_data/data.h5', 'a') as hdf:
    
#     group = hdf['/dataset/training']
#     dataset = group.create_dataset('Features', data=features.to_numpy())
    