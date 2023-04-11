import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import preprocessing

#INPUT DATA USING HDF5 (maybe use different sets?)
walking_train = pd.read_csv('input_data\walking_train.csv')
jumping_train = pd.read_csv('input_data\jumping_train.csv')

#HAVE A PREDETERMINED WINDOW SIZE
window_size = 31

#PERFORM FEATURE EXTRACTION ON WALK
mean_walk = pd.Series(walking_train).rolling(window_size).mean()
std_walk = pd.Series(walking_train).rolling(window_size).std()
max_walk = pd.Series(walking_train).rolling(window_size).max()
min_walk = pd.Series(walking_train).rolling(window_size).min()
median_walk = pd.Series(walking_train).rolling(window_size).median()
var_walk = pd.Series(walking_train).rolling(window_size).var()
corr_walk = pd.Series(walking_train).rolling(window_size).corr()
cov_walk = pd.Series(walking_train).rolling(window_size).cov()
skew_walk = pd.Series(walking_train).rolling(window_size).skew()

#PERFORM FEATURE EXTRACTION ON JUMP
mean_jump = pd.Series(jumping_train).rolling(window_size).mean()
std_jump = pd.Series(jumping_train).rolling(window_size).std()
max_jump = pd.Series(jumping_train).rolling(window_size).max()
min_jump = pd.Series(jumping_train).rolling(window_size).min()
median_jump = pd.Series(jumping_train).rolling(window_size).median()
var_jump = pd.Series(jumping_train).rolling(window_size).var()
corr_jump = pd.Series(jumping_train).rolling(window_size).corr()
cov_jump = pd.Series(jumping_train).rolling(window_size).cov()
skew_jump = pd.Series(jumping_train).rolling(window_size).skew()

#EXTRACT FEATURES FOR WALK AND JUMP
features_walking = pd.DataFrame({'mean': mean_walk,
                                 'std': std_walk,
                                 'max': max_walk,
                                 'min': min_walk,
                                 'median': median_walk,
                                 'var': var_walk,
                                 'corr': corr_walk,
                                 'cov': cov_walk,
                                 'skew': skew_walk})

features_jumping = pd.DataFrame({'mean': mean_jump,
                                 'std': std_jump,
                                 'max': max_jump,
                                 'min': min_jump,
                                 'median': median_jump,
                                 'var': var_jump,
                                 'corr': corr_jump,
                                 'cov': cov_jump,
                                 'skew': skew_jump})

#DROP NAN's PRODUCED BY WINDOW
features_walking = features_walking.dropna()
features_jumping = features_jumping.dropna()

#EXPORT BACK TO HDF5

