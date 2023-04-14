import tkinter as tk
import pandas as pd
import numpy as np
import pickle
import math
import h5py
from PIL import Image, ImageTk
from tkinter import filedialog
from sklearn import preprocessing

file_path = "./raw_data/Jacob_walking_hand_data.csv"
raw = pd.read_csv(file_path)
file_length = math.floor(len(raw)/500)
raw = pd.read_csv(file_path, nrows = file_length*500)
print("------------------------------------------------------------------")
# print(raw)
print(file_length)
active = np.array_split(raw, len(raw) // 500)
with h5py.File('HDF5/data.h5', 'r+') as hdf:
    if '/local_gui' in hdf:
        # Delete the group if it already exists
        del hdf['/local_gui']
    # Create a group for each team members data
    local = hdf.create_group('/local_gui')
    local.create_dataset('Local_Raw', data=active)
print("-------------------SPLIT---------------------------------")
# print(active)
# # df.to_csv('mydata.csv', index=False)
# pp = pd.DataFrame(columns=['Time (s)', 'Linear Acceleration x (m/s^2)', 'Linear Acceleration y (m/s^2)',
#                                           'Linear Acceleration z (m/s^2)', 'Absolute acceleration (m/s^2)'])
# STEP 3 - Visualize
# df.to_csv('mydata.csv', index=False)
# STEP 4 - Pre-Process the Data
# print(active)
train_df = h5py.File('./HDF5/data.h5', 'r+')['/local_gui/Local_Raw']
with h5py.File('./HDF5/data.h5', 'r+') as f:
    processed_df = f.create_dataset('/local_gui/Processed_Data', data=train_df)

    for i in range(len(train_df)):
        # NORMALIZE
        train_data = pd.DataFrame(train_df[i])
        sc = preprocessing.StandardScaler()
        train = sc.fit_transform(train_data)
        normalized_data = pd.DataFrame(train, columns=train_data.columns)

        # DECLARE WINDOW SIZE
        window_size = 31
        result = normalized_data.rolling(window_size, center=True).mean()

        # PUT THEM TOGETHER
        # print(result)
        processed_df[i] = result

# STEP 5 - Extract Features
df_train = h5py.File('./HDF5/data.h5', 'r+')['/local_gui/Processed_Data']
with h5py.File('./HDF5/data.h5', 'r+') as f:
    print("----------------------------FEATURES---------------------------------")
    features = pd.DataFrame(columns=['X_max', 'X_min', 'X_median', 'X_var', 'X_skew', 'X_std', 'X_kurt',
                                        'Y_max', 'Y_min', 'Y_median', 'Y_var', 'Y_skew', 'Y_std', 'Y_kurt',
                                        'Z_max', 'Z_min', 'Z_median', 'Z_var', 'Z_skew', 'Z_std', 'Z_kurt',
                                        'ABS_max', 'ABS_min', 'ABS_median', 'ABS_var', 'ABS_skew', 'ABS_std', 'ABS_kurt'])

    for i in range(len(df_train)):
        data = pd.DataFrame(df_train[i], columns=['t', 'x', 'y', 'z', 'Abs'])
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

        # feature_list.append(features)
        features.loc[i] = [x_max, x_min, x_median, x_var, x_skew, x_std, x_kurt,
                            y_max, y_min, y_median, y_var, y_skew, y_std, y_kurt,
                            z_max, z_min, z_median, z_var, z_skew, z_std, z_kurt,
                            abs_max, abs_min, abs_median, abs_var, abs_skew, abs_std, abs_kurt]
    # print(features)
    features_arr = features.to_numpy(dtype=float)
    f.create_dataset('/local_gui/Local_Features', data=features_arr)

# print(features)
print("YAY")
# STEP 6 - Classify
# clf = pickle.load(open('trained_model.sav', 'rb'))
# label_pred = clf.predict(features)
# label_clf_prob = clf.predict_proba(features)
# print(label_pred)
# print(label_clf_prob)
