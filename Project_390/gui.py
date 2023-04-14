import tkinter as tk
import pandas as pd
import numpy as np
import pickle
import math
import h5py
from PIL import Image, ImageTk
from tkinter import filedialog
from sklearn import preprocessing

# Create the main window
root = tk.Tk()
filepath = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
root.title("My GUI")
root.geometry("700x900")  # Set window size

# Create a label widget
label = tk.Label(root, text="ELEC 390 Final Project Results", font=("Helvetica", 24), fg="#333", bg="#eee")
label.pack(pady=20)

# Create a sublabel widget
sublabel = tk.Label(root, text="Group 47", font=("Helvetica", 18), fg="#666", bg="#eee")
sublabel.pack()
# Create a sublabel widget
sublabel1 = tk.Label(root, text="Omar Barakat – 20199519 – 19oksb@queensu.ca\n Ian Desouza – {Insert Student #} – 20iagd@queensu.ca \n Jacob O’Neil – 20221893 – 19jmon1@queensu.ca \n ", font=("Helvetica", 12), fg="#666", bg="#eee")
sublabel1.pack()


# # Function to display an image
# def display_image(image_file):
#     # Open the selected image file using Pillow
#     image = Image.open(image_file)
#     # Resize the image to fit inside the label widget
#     image = image.resize((500, 500))
#     # Convert the image to a Tkinter-compatible format
#     photo = ImageTk.PhotoImage(image)
#     # Update the label widget with the new image
#     label.config(image=photo)
#     label.image = photo

def perform_all(file_path):
    
    # STEP 2 - Store Data (Directly from CSV is fine)
    raw = pd.read_csv(file_path)
    file_length = math.floor(len(raw)/500)
    raw = pd.read_csv(file_path, nrows = file_length*500)
    print("------------------------------------------------------------------")
    # print(raw)
    print(file_length)
    active = np.array_split(raw, len(raw) // 500)
    with h5py.File('HDF5/data.h5', 'r+') as hdf:
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
    train_df = h5py.File('./HDF5/data.h5', 'r+')['dataset/local_gui/Test_Data']
    with h5py.File('./HDF5/data.h5', 'r+') as f:
        processed_df = f.create_dataset('dataset/local_gui/Processed_Data', data=train_df)

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
            print(result)
            processed_df[i] = result

    # print("-------------------PP---------------------------------")
    # for i in range(len(active)):
    #     # NORMALIZE
    #     train_data = pd.DataFrame(active[i])
    #     # train_label = data.iloc[:, 5]
    #     sc = preprocessing.StandardScaler()
    #     train = sc.fit_transform(train_data)
    #     normalized_data = pd.DataFrame(train, columns=train_data.columns)

    #     # DECLARE WINDOW SIZE
    #     window_size = 31
    #     result = normalized_data.rolling(window_size, center=True).mean()

    #     # PUT THEM TOGETHER
    #     # print(result)
    #     print(active[1])
    #     print(result)
    #     active[i] = result
    # meowmeow = pd.DataFrame(active)
    # meowmeow.to_csv('processed_sample.csv', index=False)

    # STEP 5 - Extract Features
    print("----------------------------FEATURES---------------------------------")
    features = pd.DataFrame(columns=['X_max', 'X_min', 'X_median', 'X_var', 'X_skew', 'X_std', 'X_kurt',
                                     'Y_max', 'Y_min', 'Y_median', 'Y_var', 'Y_skew', 'Y_std', 'Y_kurt',
                                     'Z_max', 'Z_min', 'Z_median', 'Z_var', 'Z_skew', 'Z_std', 'Z_kurt',
                                     'ABS_max', 'ABS_min', 'ABS_median', 'ABS_var', 'ABS_skew', 'ABS_std', 'ABS_kurt'])

    for i in range(len(active)):
        data = pd.DataFrame(active[i], columns=['t', 'x', 'y', 'z', 'Abs'])
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

    # STEP 6 - Classify
    clf = pickle.load(open('trained_model.sav', 'rb'))
    label_pred = clf.predict(features)
    label_clf_prob = clf.predict_proba(features)
    # print(label_pred)
    # print(label_clf_prob)




 
# Define the image file names for each button
# image_a_file = "omar_photo.jpeg"
# image_b_file = "displayB.png"
# image_c_file = "image_c.jpg"
# image_d_file = "image_d.jpg"
# image_e_file = "image_e.jpg"
# image_f_file = "image_f.jpg"

# Create five buttons that display different images
button_a = tk.Button(root, text="Data Collection", font=("Helvetica", 16), fg="#fff", bg="#333", command=lambda: perform_all(filepath))
button_a.pack(pady=10)

# button_b = tk.Button(root, text="Data Storing", font=("Helvetica", 16), fg="#fff", bg="#333", command=lambda: display_image(image_b_file))
# button_b.pack(pady=10)

# button_c = tk.Button(root, text="Visualization", font=("Helvetica", 16), fg="#fff", bg="#333", command=lambda: display_image(image_c_file))
# button_c.pack(pady=10)

# button_d = tk.Button(root, text="Preprocessing", font=("Helvetica", 16), fg="#fff", bg="#333", command=lambda: display_image(image_d_file))
# button_d.pack(pady=10)

# button_e = tk.Button(root, text="Feature Extraction", font=("Helvetica", 16), fg="#fff", bg="#333", command=lambda: display_image(image_e_file))
# button_e.pack(pady=10)

# button_f = tk.Button(root, text="Training the Classifier", font=("Helvetica", 16), fg="#fff", bg="#333", command=lambda: display_image(image_e_file))
# button_f.pack(pady=10)
# Run the main event loop
root.mainloop()