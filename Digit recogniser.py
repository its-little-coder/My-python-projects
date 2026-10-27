#--------------import area-----------------
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, classification_report

#---------------core engine-----------------
digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

#----------------variables----------------	
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

#-------------print area--------------------
print("------------------AI INFO------------------")	
print("\n-----------model predicts-----------")
print(predictions)
print("\n-----------accuracy of AI------------")
print(accuracy)
print("\n----------confusion matrix---------")
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
