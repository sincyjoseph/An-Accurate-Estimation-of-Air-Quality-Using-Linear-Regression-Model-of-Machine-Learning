# -*- coding: utf-8 -*-
"""ITWnew.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xdHwGg2vPqtAIsJ9-1EnsawViq_uiRER
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# %matplotlib inline

air_data = pd.read_excel('AirQualityUCI.xlsx')
air_data.head()

air_data.shape

import seaborn as sns
from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
sns.set(style='whitegrid', context='notebook')
features_plot = ['C6H6(GT)', 'RH', 'AH', 'PT08.S1(CO)']

data_to_plot = air_data[features_plot]
data_to_plot = scalar.fit_transform(data_to_plot)
data_to_plot = pd.DataFrame(data_to_plot)

sns.pairplot(data_to_plot, size=2.0);
plt.tight_layout()
plt.show()

"""# Step 1. Preprocessing data"""

air_data.dropna(axis=0, how='all')

"""# **Step 2. Features vs Labels**"""

features = air_data

features = features.drop('Date', axis=1)
features = features.drop('Time', axis=1)
features = features.drop('C6H6(GT)', axis=1)
features = features.drop('PT08.S4(NO2)', axis=1)

labels = air_data['C6H6(GT)'].values

features = features.values

"""# **Step 3. Train and test portions**"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3)

print("X_trian shape --> {}".format(X_train.shape))
print("y_train shape --> {}".format(y_train.shape))
print("X_test shape --> {}".format(X_test.shape))
print("y_test shape --> {}".format(y_test.shape))

"""# **Step 4. Regression**

## **Step 4.1 Linear Regression**
"""

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

for i in range (25,35):
  X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.30,random_state=i)
  regressor = LinearRegression()
  regressor.fit(X_train, y_train)
  #regressor.predict(X_test)
  y_pred=regressor.predict(X_test)
  y_pred=y_pred.reshape((-1, 1))
  maxm=regressor.score(X_test, y_test)
  MSE=mean_squared_error(y_pred,y_test)
  MAE=mean_absolute_error(y_pred,y_test) 
      
print(maxm)
print(MSE)
print(MAE)

from sklearn.metrics import mean_squared_error
from math import sqrt

rms = sqrt(mean_squared_error(y_pred, y_test))
rms

from sklearn.metrics import mean_squared_error
from math import sqrt

rms = sqrt(mean_squared_error(y_pred,y_test))
rms

"""## **Step 4.2 Support Vector Regression**"""

from sklearn.model_selection import KFold
from sklearn.svm import SVR

support_regressor = SVR(kernel='rbf', C=1000)
support_regressor.fit(X_train, y_train)

print("Coefficient of determination R^2 <-- on train set: {}".format(support_regressor.score(X_train, y_train)))

print("Coefficient of determination R^2 <-- on test set: {}".format(support_regressor.score(X_test, y_test)))

"""## **Step 4.3 Decision tree regression**"""

from sklearn.tree import DecisionTreeRegressor

dtr = DecisionTreeRegressor()
dtr.fit(X_train, y_train)

print("Coefficient of determination R^2 <-- on train set: {}".format(dtr.score(X_train, y_train)))

print("Coefficient of determination R^2 <-- on test set: {}".format(dtr.score(X_test, y_test)))

"""## **Step 4.4 Lasso regression**"""

from sklearn.linear_model import Lasso

indiana_jones = Lasso(alpha=1.0)
indiana_jones.fit(X_train, y_train)

print("Coefficient of determination R^2 <-- on train set : {}".format(indiana_jones.score(X_train, y_train)))

print("Coefficient of determination R^2 <-- on test set: {}".format(indiana_jones.score(X_test, y_test)))

"""## **Step 5. Feature selection**"""

from sklearn.ensemble import ExtraTreesRegressor

etr = ExtraTreesRegressor(n_estimators=300)
etr.fit(X_train, y_train)

print(etr.feature_importances_)
indecis = np.argsort(etr.feature_importances_)[::-1]

plt.figure(num=None, figsize=(14, 10), dpi=80, facecolor='w')
plt.title("Feature importances")
plt.bar(range(X_train.shape[1]), etr.feature_importances_[indecis],
       color="r", align="center")
plt.xticks(range(X_train.shape[1]), indecis)
plt.show()

plt.plot(y_pred, y_test)   
plt.scatter(y_pred,y_test,c='red')