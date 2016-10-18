import pandas
from sklearn import svm, cross_validation
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

# read data into DataFrame
data = pandas.read_csv('zoo-data.csv')


# split for prediction

# y is the evaluation column
Y = data['type']
# x is the entire data set (feature set) that is used to predict y (does not include y)
X = data.drop('type', 1)

# this splits up both the evaluation column and the features to have a 80:20 split between training and testing data
train_x, test_x, train_y, test_y = train_test_split(X, Y, test_size=0.2)

# SVM Implementation

# initialize the model
model = svm.SVC()
# fit the data onto the model and train
model = model.fit(train_x, train_y)
# create the results from the test feature set
pred = model.predict(test_x)

# this will print the evaluation metrics for the model against the test set
print confusion_matrix(pred, test_y)
print classification_report(test_y, pred)
