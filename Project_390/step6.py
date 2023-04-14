import pandas as pd
import h5py
import pickle
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import RocCurveDisplay
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import recall_score

# INPUT DATA
train_df = h5py.File('./HDF5/data.h5', 'r')['dataset/training/Train_Features']
test_df = h5py.File('./HDF5/data.h5', 'r')['dataset/testing/Test_Features']

data = pd.DataFrame(train_df)
train_labels = data.iloc[:, -1]
train_data = data.iloc[:, 0:-1]
data = pd.DataFrame(test_df)
test_labels = data.iloc[:, -1]
test_data = data.iloc[:, 0:-1]

scaler = StandardScaler()
l_reg = LogisticRegression(max_iter=10000)
clf = make_pipeline(StandardScaler(), l_reg)


# # train the classifier on the training data
clf.fit(train_data, train_labels)

label_pred = clf.predict(test_data)
label_clf_prob = clf.predict_proba(test_data)

print(label_pred)
print(label_clf_prob)

# # predict the class labels of the test data
# y_pred = clf.predict(X_test)

# # evaluate the performance of the classifier
accuracy = accuracy_score(test_labels, label_pred)
print('Accuracy:', accuracy)

# filename = 'trained_model.sav'
# file = open(filename, 'wb')
# pickle.dump(clf, file)
# file.close()