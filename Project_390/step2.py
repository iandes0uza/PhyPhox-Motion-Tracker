import numpy as np
import pandas as pd
import h5py
from sklearn.model_selection import train_test_split

#                            TIPS FROM IAN
#--------------------------------------------------------------------------
# pandas needed an update for me (pip install pandas -U)
# xlrd needed an updated too (pip install xlrd -U)
#
# anaconda not needed because i hate package managers 
#
#       meow
#
# only run the file when the folder is opened in VS,
# will not work if u have it running in a folder (relative paths break?)
#---------------------------------------------------------------------------

# Download
#(For creating h5py files):          "conda install -c anaconda xlrd"
#(For reading excel / .xls files):   "conda install -c anaconda xlrd"
#(For sklearn):                      "conda install -c anaconda scikit-learn"

#If there is issue when reading excel file, issue is most likely due to the fact that the excel file is protected
# create a new copy of file and add new verison

# CREATE A STANDARD FILE READ SIZE
max_rows = 500*6

# Load the data from the Excel and CSV files:
# Jacob's Files:
df_JD1 = pd.read_csv('raw_data/Jacob_jump_back_pocket_data.csv', nrows=max_rows)
df_JD2 = pd.read_csv('raw_data/Jacob_jump_front_pocket_data.csv', nrows=max_rows)
df_JD3 = pd.read_csv('raw_data/Jacob_jump_hand_data.csv', nrows=max_rows)
df_JD4 = pd.read_csv('raw_data/Jacob_walking_back_pocket_data.csv', nrows=max_rows)
df_JD5 = pd.read_csv('raw_data/Jacob_walking_front_pocket_data.csv', nrows=max_rows)
df_JD6 = pd.read_csv('raw_data/Jacob_walking_hand_data.csv', nrows=max_rows)

# Omar's Files:
df_OD1 = pd.read_csv('raw_data/omar_jumping_back_pocket_data.csv', nrows=max_rows)
df_OD2 = pd.read_csv('raw_data/omar_jumping_front_pocket_data.csv', nrows=max_rows)
df_OD3 = pd.read_csv('raw_data/omar_jumping_hand_data.csv', nrows=max_rows)
df_OD4 = pd.read_csv('raw_data/omar_walking_back_pocket_data.csv', nrows=max_rows)
df_OD5 = pd.read_csv('raw_data/omar_walking_front_pocket_data.csv', nrows=max_rows)
df_OD6 = pd.read_csv('raw_data/omar_walking_hand_data.csv', nrows=max_rows)

# Ian's Files:
df_ID1 = pd.read_csv('raw_data/Ian_left_back_walk.csv', nrows=max_rows)
df_ID2 = pd.read_csv('raw_data/Ian_left_front_walk.csv', nrows=max_rows)
df_ID3 = pd.read_csv('raw_data/Ian_right_back_walk.csv', nrows=max_rows)
df_ID4 = pd.read_csv('raw_data/Ian_right_front_walk.csv', nrows=max_rows)
df_ID5 = pd.read_csv('raw_data/Ian_back_jump.csv', nrows=max_rows)
df_ID6 = pd.read_csv('raw_data/Ian_front_jump.csv', nrows=max_rows)

# Combine Data Sets
walk_df = [df_JD4, df_JD5, df_JD6,
           df_OD4, df_OD5, df_OD6,
           df_ID1, df_ID2, df_ID3]
walk_df = pd.concat(walk_df)
walk_df['label'] = 0

jump_df = [df_JD1, df_JD2, df_JD3,
           df_OD1, df_OD2, df_OD3,
           df_ID4, df_ID5, df_ID6]
jump_df = pd.concat(jump_df)
jump_df['label'] = 1

# Combine Both Datasets & Shuffle
raw_df = [walk_df, jump_df]
raw_data = pd.concat(raw_df)
# HOW DO I SHUFFLE LOL--------------------------------------------------------------------------
# shuffled_data = raw_data

# group the dataframe into groups of 100 rows each
# groups = raw_data.groupby(raw_data.index // 2000)
# print(groups)

# shuffle the rows within each group using the sample() method
# shuffled_df = groups.apply(lambda x: x.sample(frac=1)).reset_index(drop=True)
shuffled_data = np.array_split(raw_data, len(raw_data) // 500)

# # Print the first 5 rows of each smaller dataframe
# for i in range(len(shuffled_data)):
#     print("shuffled window", i+1)
#     print(shuffled_data[i].head())

np.random.shuffle(shuffled_data)

for i in range(len(shuffled_data)):
    print("shuffled window", i+1)
    print(shuffled_data[i])

# display the shuffled dataframe
# print(walk_df)
# print(jump_df)
# print(raw_df)
# print(raw_data)
# print(shuffled_df)
# print("MEOW")
# print(raw_data)
#---------------------------------------------------------------------------------------------------------------

# Split data into training and testing sets, with 90% of the data used for training and 10% used for testing
train_data, test_data = train_test_split(shuffled_data, test_size=0.1, random_state=42)

# Create the HDF5 File and start organizing
# Write to the file:
with h5py.File('output_data/data.h5', 'w') as hdf:
    # Create a group for each team members data
    Jacob_Data = hdf.create_group('/Jacob')
    Omar_Data = hdf.create_group('/Omar')
    Ian_Data = hdf.create_group('/Ian')
    main = hdf.create_group('/dataset')
    train = hdf.create_group('/dataset/training')
    test = hdf.create_group('/dataset/testing')

    #Add data to Train_Dataset_Group
    train.create_dataset('Train_Data', data=train_data)
    train_data.to_csv('train.csv', index=False)

    # Add data to Test_Dataset_Group
    test.create_dataset('Test_Data', data=test_data)
    test_data.to_csv('test.csv', index=False)

# Jacob_Data_Group----------------------------------------------------------------------------
    
    JD_Jump = hdf.create_group('/Jacob/Data_Jump')
    #Add data to JD_Jump Group
    JD_Jump.create_dataset('J_jump_backP', data=df_JD1.to_numpy())
    JD_Jump.create_dataset('J_jump_frontP', data=df_JD2.to_numpy())
    JD_Jump.create_dataset('J_jump_hand', data=df_JD3.to_numpy())

    JD_Walk = hdf.create_group('/Jacob/Data_Walk')
    # Add data to JD_Walk Group
    JD_Walk.create_dataset('J_walk_backP', data=df_JD4.to_numpy())
    JD_Walk.create_dataset('J_walk_frontP', data=df_JD5.to_numpy())
    JD_Walk.create_dataset('J_walk_hand', data=df_JD6.to_numpy())

# Omar_Data_Group----------------------------------------------------------------------------
    
    OD_Jump = hdf.create_group('/Omar/Data_Jump')
    #Add data to OD_Jump Group
    OD_Jump.create_dataset('O_jump_backP', data=df_OD1.to_numpy())
    OD_Jump.create_dataset('O_jump_frontP', data=df_OD2.to_numpy())
    OD_Jump.create_dataset('O_jump_hand', data=df_OD3.to_numpy())

    OD_Walk = hdf.create_group('/Omar/Data_Walk')
    # Add data to OD_Walk Group
    OD_Walk.create_dataset('O_walk_backP', data=df_OD4.to_numpy())
    OD_Walk.create_dataset('O_walk_frontP', data=df_OD5.to_numpy())
    OD_Walk.create_dataset('O_walk_hand', data=df_OD6.to_numpy())

# Ian_Data_Group----------------------------------------------------------------------------
    
    ID_Jump = hdf.create_group('/Ian/Data_Jump')
    # #Add data to OD_Jump Group
    ID_Jump.create_dataset('I_jump_backP', data=df_ID5.to_numpy())
    ID_Jump.create_dataset('I_jump_frontP', data=df_ID6.to_numpy())
    #
    ID_Walk = hdf.create_group('/Ian/Data_Walk')
    # # Add data to OD_Walk Group
    ID_Walk.create_dataset('I_walk_backLP', data=df_ID1.to_numpy())
    ID_Walk.create_dataset('I_walk_frontLP', data=df_ID2.to_numpy())
    ID_Walk.create_dataset('I_walk_backRP', data=df_ID3.to_numpy())
    ID_Walk.create_dataset('I_walk_frontRP', data=df_ID4.to_numpy())