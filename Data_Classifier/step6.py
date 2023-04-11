import pandas as pd
import h5py
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier

# Open the HDF5 file
with h5py.File('input_data/data.hdf5', 'r') as file:
    
    # Get the dataset you want to read
    train = file['/dataset/training/Train_Data']
    test = file['/dataset/testing/Test_Data']
    
    # Convert the dataset to a numpy array
    # np_array = dataset[()]
    
    # Convert the numpy array to a pandas DataFrame
    # df = pd.DataFrame(np_array)

clf = DecisionTreeClassifier()

# train the classifier on the training data
clf.fit(X_train, y_train)

# predict the class labels of the test data
y_pred = clf.predict(X_test)

# evaluate the performance of the classifier
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)