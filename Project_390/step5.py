import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import h5py
from sklearn import preprocessing

# #INPUT DATA USING HDF5 (maybe use different sets?)
df_train = h5py.File('./HDF5/data.h5', 'r+')['dataset/training/Processed_Data']
with h5py.File('./HDF5/data.h5', 'r+') as f:

    feature_list = []
    features = pd.DataFrame(columns=['X_max', 'X_min', 'X_median', 'X_var', 'X_skew', 'X_std', 'X_kurt',
                                     'Y_max', 'Y_min', 'Y_median', 'Y_var', 'Y_skew', 'Y_std', 'Y_kurt',
                                     'Z_max', 'Z_min', 'Z_median', 'Z_var', 'Z_skew', 'Z_std', 'Z_kurt',
                                     'ABS_max', 'ABS_min', 'ABS_median', 'ABS_var', 'ABS_skew', 'ABS_std', 'ABS_kurt', 'label'])

    for i in range(len(df_train)):
        data = pd.DataFrame(df_train[i], columns=['Time (s)', 'x', 'y',
                                         'z', 'Abs', 'label'])
        print(data)
        # features = pd.DataFrame(columns=['max', 'min'])
        x_max = data.x.max()
        x_min = data.x.min()
        x_median = data.x.median()
        x_var = data.x.var()
        x_skew = data.x.skew()
        x_std = data.x.std()
        x_kurt = data.x.kurt()

        y_max = data.y.max()
        y_min = data.y.min()
        y_median = data.y.median()
        y_var = data.y.var()
        y_skew = data.y.skew()
        y_std = data.y.std()
        y_kurt = data.y.kurt()

        z_max = data.z.max()
        z_min = data.z.min()
        z_median = data.z.median()
        z_var = data.z.var()
        z_skew = data.z.skew()
        z_std = data.z.std()
        z_kurt = data.z.kurt()

        abs_max = data.Abs.max()
        abs_min = data.Abs.min()
        abs_median = data.Abs.median()
        abs_var = data.Abs.var()
        abs_skew = data.Abs.skew()
        abs_std = data.Abs.std()
        abs_kurt = data.Abs.kurt()

        label_val = data.label.mode()

        # feature_list.append(features)
        features.loc[i] = [x_max, x_min, x_median, x_var, x_skew, x_std, x_kurt,
                           y_max, y_min, y_median, y_var, y_skew, y_std, y_kurt,
                           z_max, z_min, z_median, z_var, z_skew, z_std, z_kurt,
                           abs_max, abs_min, abs_median, abs_var, abs_skew, abs_std, abs_kurt, label_val]
    
    print(features)
    features_arr = features.to_numpy(dtype=float)
    f.create_dataset('dataset/training/Train_Features', data=features_arr)

# #INPUT DATA USING HDF5 (maybe use different sets?)
df_train = h5py.File('./HDF5/data.h5', 'r+')['dataset/testing/Processed_Data']
with h5py.File('./HDF5/data.h5', 'r+') as f:

    feature_list = []
    features = pd.DataFrame(columns=['X_max', 'X_min', 'X_median', 'X_var', 'X_skew', 'X_std', 'X_kurt',
                                     'Y_max', 'Y_min', 'Y_median', 'Y_var', 'Y_skew', 'Y_std', 'Y_kurt',
                                     'Z_max', 'Z_min', 'Z_median', 'Z_var', 'Z_skew', 'Z_std', 'Z_kurt',
                                     'ABS_max', 'ABS_min', 'ABS_median', 'ABS_var', 'ABS_skew', 'ABS_std', 'ABS_kurt', 'label'])

    for i in range(len(df_train)):
        data = pd.DataFrame(df_train[i], columns=['Time (s)', 'x', 'y',
                                         'z', 'Abs', 'label'])
        print(data)
        # features = pd.DataFrame(columns=['max', 'min'])
        x_max = data.x.max()
        x_min = data.x.min()
        x_median = data.x.median()
        x_var = data.x.var()
        x_skew = data.x.skew()
        x_std = data.x.std()
        x_kurt = data.x.kurt()

        y_max = data.y.max()
        y_min = data.y.min()
        y_median = data.y.median()
        y_var = data.y.var()
        y_skew = data.y.skew()
        y_std = data.y.std()
        y_kurt = data.y.kurt()

        z_max = data.z.max()
        z_min = data.z.min()
        z_median = data.z.median()
        z_var = data.z.var()
        z_skew = data.z.skew()
        z_std = data.z.std()
        z_kurt = data.z.kurt()

        abs_max = data.Abs.max()
        abs_min = data.Abs.min()
        abs_median = data.Abs.median()
        abs_var = data.Abs.var()
        abs_skew = data.Abs.skew()
        abs_std = data.Abs.std()
        abs_kurt = data.Abs.kurt()

        label_val = data.label.mode()

        # feature_list.append(features)
        features.loc[i] = [x_max, x_min, x_median, x_var, x_skew, x_std, x_kurt,
                           y_max, y_min, y_median, y_var, y_skew, y_std, y_kurt,
                           z_max, z_min, z_median, z_var, z_skew, z_std, z_kurt,
                           abs_max, abs_min, abs_median, abs_var, abs_skew, abs_std, abs_kurt, label_val]
    
    print(features)
    features_arr = features.to_numpy(dtype=float)
    f.create_dataset('dataset/testing/Test_Features', data=features_arr)