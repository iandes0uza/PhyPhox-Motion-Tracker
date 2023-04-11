import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import preprocessing

# INPUT DATA SET
walking_train = pd.read_csv('input_data\walking_train.csv')
jumping_train = pd.read_csv('input_data\jumping_train.csv')

window_size = 31
filtered_walk = walking_train.rolling(window_size, center=True).mean()
filtered_jump = jumping_train.rolling(window_size, center=True).mean()
