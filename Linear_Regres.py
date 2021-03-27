"""Accuracy:  43.709481451010035
[49.28781684]
Enter no. of hours: 100
y=4.587899 * 100.000000 + 12.584628
Risk Score:  471.3744889615699
"""
#import Packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#reading data sets
dataset=pd.read_csv("data.csv")
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values


from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x,y)
print("Accuracy: ", regressor.score(x,y)*100)

y_pred=regressor.predict([[8]])
print(y_pred)

hours=int(input("Enter no. of hours: "))
eq=regressor.coef_*hours+regressor.intercept_
print("y=%f * %f + %f" %(regressor.coef_, hours,regressor.intercept_))
print("Risk Score: ", eq[0])

plt.plot(x,y,'o')
plt.plot(x,regressor.predict(x));
plt.show();
