from os import X_OK
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
import numpy as np

gaus = GaussianNB()

reg = LogisticRegression(penalty='l2',C=1.0, max_iter=500)
clf	=	gaus


classes = {
    0: "Iris Setosa",
    1: "Iris Versicolour",
    2: "Iris Virginica"
}

r_classes = {y: x for x, y in classes.items()}

def load_model():
	X, y = datasets.load_iris(return_X_y=True)

	X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
	gaus.fit(X_train, y_train)

	acc_gaus = accuracy_score(y_test, gaus.predict(X_test))
	print(f" GaussianNB Model trained with accuracy: {round(acc_gaus, 3)}")

	reg.fit(X_train, y_train)

	acc_reg = accuracy_score(y_test, reg.predict(X_test))
	print(f"Logistic Regression Model trained with accuracy: {round(acc_reg, 3)}")

	 
	if acc_gaus > acc_reg :
		 clf = gaus
	else:
		 clf = reg


def predict(query_data):
	print(f"query_data.dict().values()={query_data.dict().values()}")
	x = list(query_data.dict().values())
	prediction = clf.predict([x])[0] 
	print(f"Model prediction: {classes[prediction]}")
	return classes[prediction]

# function to retrain the model as part of the feedback loop
def retrain(data):
    # pull out the relevant X and y from the FeedbackIn object
    X = [list(d.dict().values())[:-1] for d in data]
    y = [r_classes[d.flower_class] for d in data]

    # fit the classifier again based on the new data obtained
    clf.fit(X, y)
	