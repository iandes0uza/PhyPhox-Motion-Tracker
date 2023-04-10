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
# only run the file when the folder is opened in VS,
# will not work if u have it running in a folder (relative paths break?)
#---------------------------------------------------------------------------

# Download
#(For creating h5py files):          "conda install -c anaconda xlrd"
#(For reading excel / .xls files):   "conda install -c anaconda xlrd"
#(For sklearn):                      "conda install -c anaconda scikit-learn"

#If there is issue when reading excel file, issue is most likely due to the fact that the excel file is protected
# create a new copy of file and add new verison


# Load the data from the Excel and CSV files:
#Jacobs Files:
df_JD1 = pd.read_csv('Jacob_jump_back_pocket_data.csv')
df_JD2 = pd.read_csv('Jacob_jump_front_pocket_data.csv')
df_JD3 = pd.read_csv('Jacob_jump_hand_data.csv')
df_JD4 = pd.read_csv('Jacob_walking_back_pocket_data.csv')
df_JD5 = pd.read_csv('Jacob_walking_front_pocket_data.csv')
df_JD6 = pd.read_csv('Jacob_walking_hand_data.csv')

#Omars Files:
df_OD1 = pd.read_csv('omar_jumping_back_pocket_data.csv')
df_OD2 = pd.read_csv('omar_jumping_front_pocket_data.csv')
df_OD3 = pd.read_csv('omar_jumping_hand_data.csv')
df_OD4 = pd.read_csv('omar_walking_back_pocket_data.csv')
df_OD5 = pd.read_csv('omar_walking_front_pocket_data.csv')
df_OD6 = pd.read_csv('omar_walking_hand_data.csv')

#Ians Files:
df_ID1 = pd.read_csv('Ian_left_back_walk.csv')
df_ID2 = pd.read_csv('Ian_left_front_walk.csv')
df_ID3 = pd.read_csv('Ian_right_back_walk.csv')
df_ID4 = pd.read_csv('Ian_right_front_walk.csv')
df_ID5 = pd.read_csv('Ian_back_jump.csv')
df_ID6 = pd.read_csv('Ian_front_jump.csv')

# Create the HDF5 File and start organizing
# Write to the file:
with h5py.File('./hdf5_data.h5', 'w') as hdf:
    # Create a group for each team members data
    Jacob_Data = hdf.create_group('/Jacob_Data_Group')
    Omar_Data = hdf.create_group('/Omar_Data_Group')
    Ian_Data = hdf.create_group('/Ian_Data_Group')

#Jacob_Data_Group----------------------------------------------------------------------------
    
    JD_Jump = hdf.create_group('Jacob_Data_Group/Jacob_Data_Jump')
    #Add data to JD_Jump Group
    JD_Jump.create_dataset('J_jump_backP', data=df_JD1.to_numpy())
    JD_Jump.create_dataset('J_jump_frontP', data=df_JD2.to_numpy())
    JD_Jump.create_dataset('J_jump_hand', data=df_JD3.to_numpy())

    JD_Walk = hdf.create_group('Jacob_Data_Group/Jacob_Data_Walk')
    # Add data to JD_Walk Group
    JD_Walk.create_dataset('J_walk_backP', data=df_JD4.to_numpy())
    JD_Walk.create_dataset('J_walk_frontP', data=df_JD5.to_numpy())
    JD_Walk.create_dataset('J_walk_hand', data=df_JD6.to_numpy())

#Omar_Data_Group----------------------------------------------------------------------------
    
    OD_Jump = hdf.create_group('Omar_Data_Group/Omar_Data_Jump')
    #Add data to OD_Jump Group
    OD_Jump.create_dataset('O_jump_backP', data=df_OD1.to_numpy())
    OD_Jump.create_dataset('O_jump_frontP', data=df_OD2.to_numpy())
    OD_Jump.create_dataset('O_jump_hand', data=df_OD3.to_numpy())

    OD_Walk = hdf.create_group('Omar_Data_Group/Omar_Data_Walk')
    # Add data to OD_Walk Group
    OD_Walk.create_dataset('O_walk_backP', data=df_OD4.to_numpy())
    OD_Walk.create_dataset('O_walk_frontP', data=df_OD5.to_numpy())
    OD_Walk.create_dataset('O_walk_hand', data=df_OD6.to_numpy())

#Ian_Data_Group----------------------------------------------------------------------------
    
    ID_Jump = hdf.create_group('Ian_Data_Group/Ian_Data_Jump')
    # #Add data to OD_Jump Group
    ID_Jump.create_dataset('I_jump_backP', data=df_ID5.to_numpy())
    ID_Jump.create_dataset('I_jump_frontP', data=df_ID6.to_numpy())
    #
    ID_Walk = hdf.create_group('Ian_Data_Group/Ian_Data_Walk')
    # # Add data to OD_Walk Group
    ID_Walk.create_dataset('I_walk_backLP', data=df_ID1.to_numpy())
    ID_Walk.create_dataset('I_walk_frontLP', data=df_ID2.to_numpy())
    ID_Walk.create_dataset('I_walk_backRP', data=df_ID3.to_numpy())
    ID_Walk.create_dataset('I_walk_frontRP', data=df_ID4.to_numpy())

#Splitting the data into Trian and Test datasets----------------------------------------------------------------------------

# Read the data from the HDF5 file
with h5py.File('./hdf5_data.h5', 'r') as hdf:
    # Get the Jacob and Omar data groups
    jacob_data = hdf.get('/Jacob_Data_Group')
    omar_data = hdf.get('/Omar_Data_Group')
    ian_data = hdf.get('/Ian_Data_Group')

    # Get the jump and walk groups from each data group
    jacob_jump = jacob_data.get('Jacob_Data_Jump')
    jacob_walk = jacob_data.get('Jacob_Data_Walk')
    omar_jump = omar_data.get('Omar_Data_Jump')
    omar_walk = omar_data.get('Omar_Data_Walk')
    ian_jump = ian_data.get('Ian_Data_Jump')
    ian_walk = ian_data.get('Ian_Data_Walk')

    # Convert the datasets to NumPy arrays
    jacob_jump_backp = np.array(jacob_jump.get('J_jump_backP'))
    jacob_jump_frontp = np.array(jacob_jump.get('J_jump_frontP'))
    jacob_jump_hand = np.array(jacob_jump.get('J_jump_hand'))
    jacob_walk_backp = np.array(jacob_walk.get('J_walk_backP'))
    jacob_walk_frontp = np.array(jacob_walk.get('J_walk_frontP'))
    jacob_walk_hand = np.array(jacob_walk.get('J_walk_hand'))
    omar_jump_backp = np.array(omar_jump.get('O_jump_backP'))
    omar_jump_frontp = np.array(omar_jump.get('O_jump_frontP'))
    omar_jump_hand = np.array(omar_jump.get('O_jump_hand'))
    omar_walk_backp = np.array(omar_walk.get('O_walk_backP'))
    omar_walk_frontp = np.array(omar_walk.get('O_walk_frontP'))
    omar_walk_hand = np.array(omar_walk.get('O_walk_hand'))
    ian_walk_lbp = np.array(ian_walk.get('I_walk_backLP'))
    ian_walk_lfp = np.array(ian_walk.get('I_walk_frontLP'))
    ian_walk_rbp = np.array(ian_walk.get('I_walk_backRP'))
    ian_walk_rfp = np.array(ian_walk.get('I_walk_frontRP'))
    ian_jump_bp = np.array(ian_jump.get('I_jump_backP'))
    ian_jump_fp = np.array(ian_jump.get('I_jump_frontP'))

# Combine the jump and walk data
walk_data = np.concatenate([jacob_walk_backp, jacob_walk_frontp, jacob_walk_hand, 
                            omar_walk_backp, omar_walk_frontp, omar_walk_hand,
                            ian_walk_lbp, ian_walk_lfp, ian_walk_rbp, ian_walk_rfp])
jump_data = np.concatenate([jacob_jump_backp, jacob_jump_frontp, jacob_jump_hand,
                            omar_jump_backp, omar_jump_frontp, omar_jump_hand,
                            ian_jump_bp, ian_jump_fp])


# Split data into training and testing sets, with 90% of the data used for training and 10% used for testing
walk_train, walk_test = train_test_split(walk_data, test_size=0.1, random_state=42)
jump_train, jump_test = train_test_split(jump_data, test_size=0.1, random_state=42)

#For reference of training and test data being 90% and 10% respectfully
print(walk_data.shape)
print(walk_train.shape)
print(walk_test.shape)

# Create groups for Train and Test data within a dataset group
with h5py.File('./hdf5_data.h5', 'w') as hdf:
    main_dataset = hdf.create_group('/Main_Dataset_Group')
    train_dataset = hdf.create_group('Main_Dataset_Group/Train_Dataset_Group')
    test_dataset = hdf.create_group('Main_Dataset_Group/Test_Dataset_Group')

    #Add data to Train_Dataset_Group
    train_dataset.create_dataset('Walk_Train_Data', data=walk_data)
    train_dataset.create_dataset('Jump_Train_Data', data=jump_train)

    # Add data to Test_Dataset_Group
    test_dataset.create_dataset('Walk_Test_Data', data=walk_test)
    test_dataset.create_dataset('Jump_Test_Data', data=jump_test)