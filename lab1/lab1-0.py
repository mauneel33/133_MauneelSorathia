import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Data_for_Transformation.csv')

#Scatter plot b/w age and salary
plt.scatter(data['Age'], data['Salary'])
plt.show()

#Histogram of salary
plt.hist(data['Salary'], bins=6)
plt.show()

#Bar chart of Country
x = data['Country'].value_counts().index.tolist()
y = data['Country'].value_counts()
plt.bar(x, y)
plt.show()