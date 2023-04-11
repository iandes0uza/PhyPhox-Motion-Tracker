import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import preprocessing

#INPUT DATA USING HDF5 (maybe use different sets?)
trained_data = pd.read_csv('input_data\trained.csv')

#HAVE A PREDETERMINED WINDOW SIZE
window_size = 31

#PERFORM FEATURE EXTRACTION ON WALK
mean_train = pd.Series(trained_data).rolling(window_size).mean()
std_train = pd.Series(trained_data).rolling(window_size).std()
max_train = pd.Series(trained_data).rolling(window_size).max()
min_train = pd.Series(trained_data).rolling(window_size).min()
median_train = pd.Series(trained_data).rolling(window_size).median()
var_train = pd.Series(trained_data).rolling(window_size).var()
corr_train = pd.Series(trained_data).rolling(window_size).corr()
cov_train = pd.Series(trained_data).rolling(window_size).cov()
skew_train = pd.Series(trained_data).rolling(window_size).skew()

#EXTRACT FEATURES FOR WALK AND JUMP
features = pd.DataFrame({'mean': mean_train,
                         'std': std_train,
                         'max': max_train,
                         'min': min_train,
                         'median': median_train,
                         'var': var_train,
                         'corr': corr_train,
                         'cov': cov_train,
                         'skew': skew_train})

#DROP NAN's PRODUCED BY WINDOW
features = features.dropna()

#EXPORT BACK TO HDF5

