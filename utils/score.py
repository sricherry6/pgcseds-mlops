from collections import Counter
from numpy import mean, std
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import warnings
warnings.filterwarnings('ignore')

from utils.credit_data_actual_values import substitute


clf = RandomForestClassifier(max_depth=2, random_state=0)


def train_column_encoder(X, y):
	cat_ix = X.select_dtypes(include=['object', 'bool']).columns
	ct = ColumnTransformer([('o',OneHotEncoder(handle_unknown = 'ignore'),cat_ix)], remainder='passthrough')
	X = ct.fit_transform(X)
	yt = LabelEncoder()
	y = yt.fit_transform(y)
	return X, y, ct, yt

def train(df):
	df = pd.read_csv(
		"http://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data",
		sep=" ",
		header=None
	)
	last_ix = len(df.columns) - 1
	X, y = df.drop(last_ix, axis=1), df[last_ix]
	X, y, ct, yt = train_column_encoder(X, y)
	clf.fit(X, y)
	return ct, yt

def predict(test_sample, ct):
   sample = test_sample
   sample = ct.transform(sample)
   prediction = clf.predict(sample)
   return prediction


def main():
	ct, yt = train(df)
	test_sample = {'Status of existing checking account':'no checking account' , 'Duration in month':10, 'Credit history':'critical account', 'Purpose':'radio/television', 'Credit amount':1169, 'Savings account/bonds':'no savings account', 'Present employment since':'>=7 years','Installment rate in percentage of disposable income':4,'Personal status and sex':'male:single', 'Other debtors / guarantors':'none','Present residence since':2, 'Property':'real estate', 'Age in years':67, 'Other installment plans':'none', 'Housing':'own', 'Number of existing credits at this bank': 2, 'Job':'skilled employee / official', 'Number of people being liable to provide maintenance for':1, 'Telephone':'yes', 'foreign worker':'yes'}
	test_sample = pd.DataFrame([test_sample])
	test_sample = substitute(test_sample)
	print(test_sample)
	prediction = predict(test_sample, clf, ct)
	print(prediction)

def load_model():
	pass

def calc_risk(query):
	return 0







