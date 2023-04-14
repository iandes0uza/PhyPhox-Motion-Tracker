import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle
import math
import h5py
from PIL import Image, ImageTk
from sklearn import preprocessing

def gui_execute(file_path):

    # STEP 1 - Data Storage
    raw = pd.read_csv(file_path)
    file_length = math.floor(len(raw)/500)
    raw = pd.read_csv(file_path, nrows = file_length*500)
    print(file_length)
    active = np.array_split(raw, len(raw) // 500)
    with h5py.File('HDF5/data.h5', 'r+') as hdf:
        if '/local_gui' in hdf:
            # Delete the group if it already exists
            del hdf['/local_gui']
        # Create a group for each team members data
        local = hdf.create_group('/local_gui')
        local.create_dataset('Local_Raw', data=active)
    # STEP 3 - Visualize
    # df.to_csv('mydata.csv', index=False)

    # STEP 4 - Pre-Process the Data
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
            window_size = 10
            result = normalized_data.rolling(window_size, center=True).mean()

            # PUT THEM TOGETHER
            # print(result)
            processed_df[i] = result
        

        # plt.plot(raw['Time (s)'], processed_df['Absolute acceleration (m/s^2)'], label="raw")
        # plt.legend()
        # plt.show()

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
    # STEP 6 - Classify
    clf = pickle.load(open('trained_model.sav', 'rb'))
    label_pred = clf.predict(features)
    label_clf_prob = clf.predict_proba(features)
    print(label_pred)
    print(label_clf_prob)

    # STEP 0 - Saving to CSV
    df_raw = h5py.File('./HDF5/data.h5', 'r')['/local_gui/Local_Raw']
    df_raw_2d = df_raw[:].reshape(-1, df_raw.shape[-1])
    df = pd.DataFrame(df_raw_2d)
    df.to_csv('Local_Raw.csv', index=False)
    x = df.iloc[:, 0]
    raw_x = df.iloc[:, 1]
    raw_y = df.iloc[:, 2]
    raw_z = df.iloc[:, 3]
    raw_abs = df.iloc[:, 4]

    df_processed = h5py.File('./HDF5/data.h5', 'r')['/local_gui/Processed_Data']
    df_processed_2d = df_processed[:].reshape(-1, df_processed.shape[-1])
    df = pd.DataFrame(df_processed_2d)
    df.to_csv('Local_Processed.csv', index=False)
    proc_x = df.iloc[:, 1]
    proc_y = df.iloc[:, 2]
    proc_z = df.iloc[:, 3]
    proc_abs = df.iloc[:, 4]

    df_features = h5py.File('./HDF5/data.h5', 'r')['/local_gui/Local_Features']
    df_features_2d = df_features[:].reshape(-1, df_features.shape[-1])
    df = pd.DataFrame(df_features_2d)
    df.to_csv('Local_Features.csv', index=False)

    # STEP 0.1 - Creating Graphs
    plt.figure()
    plt.plot(x, raw_x, color="red", label="Raw X Acceleration")
    plt.plot(x, proc_x, color='blue', label="Processed X Acceleration")
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s^2)')
    plt.title('Raw vs. Processed X-Axis Acceleration')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig('grab_img/rpx.png', dpi=300, bbox_inches='tight', pad_inches=0.2)
    plt.close()
    # plt.show()

    plt.figure()
    plt.plot(x, raw_y, color='red', label="Raw Y Acceleration")
    plt.plot(x, proc_y, color='blue', label="Processed Y Acceleration")
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s^2)')
    plt.title('Raw vs. Processed Y-Axis Acceleration')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig('grab_img/rpy.png', dpi=300, bbox_inches='tight', pad_inches=0.2)
    plt.clf()
    # plt.show()

    plt.figure()
    plt.plot(x, raw_z, color='red', label="Raw Z Acceleration")
    plt.plot(x, proc_z, color='blue', label="Processed Z Acceleration")
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s^2)')
    plt.title('Raw vs. Processed Z-Axis Acceleration')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig('grab_img/rpz.png', dpi=300, bbox_inches='tight', pad_inches=0.2)
    plt.close()
    # plt.show()

    plt.figure()
    plt.plot(x, raw_abs, color='red', label="Raw Absolute Acceleration")
    plt.plot(x, proc_abs, color='blue', label="Processed Absolute Acceleration")
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s^2)')
    plt.title('Raw vs. Processed Absolute Acceleration')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig('grab_img/rpabs.png', dpi=300, bbox_inches='tight', pad_inches=0.2)
    plt.clf()
    # plt.show()

    plt.figure()
    plt.plot(x, raw_x, color='red', label="Raw X Acceleration")
    plt.plot(x, raw_y, color='blue', label="Raw Y Acceleration")
    plt.plot(x, raw_z, color='green', label="Raw Z Acceleration")
    plt.plot(x, raw_abs, color='purple', label="Raw Absolute Acceleration")
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s^2)')
    plt.title('Raw Acceleration')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig('grab_img/raw.png', dpi=300, bbox_inches='tight', pad_inches=0.2)
    plt.cla()
    # plt.show()
    
    plt.figure()
    plt.plot(x, proc_x, color='red', label="Processed X Acceleration")
    plt.plot(x, proc_y, color='blue', label="Processed Y Acceleration")
    plt.plot(x, proc_z, color='green', label="Processed Z Acceleration")
    plt.plot(x, proc_abs, color='purple', label="Processed Absolute Acceleration")
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s^2)')
    plt.title('Processed Acceleration')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig('grab_img/proc.png', dpi=300, bbox_inches='tight', pad_inches=0.2)
    plt.clf()
    # plt.show()

    df = pd.DataFrame(label_pred)
    walk_jump = df.mode()
    if (walk_jump.iloc[0,0] > 0.1): return 1
    else: return 0
# gui_execute("raw_data/Ian_left_front_walk.csv")
