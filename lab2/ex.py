import numpy as np 
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler, StandardScaler
from sklearn.impute import SimpleImputer
import seaborn as sns

datasets = pd.read_csv('Exercise-CarData.csv')
# print(datasets.describe)

#Removing rows with null values
datasets.dropna(how='all', inplace=True)
# print(datasets)

#Removing first and non-numeric columns
X = datasets.iloc[:, 1:3].values
# print(X)

#Replacing null values with mean value of that attribute
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(X)
X = imputer.transform(X)
# print(X)

#Data Transformation
#Scaling
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
# print(X_scaled)

#Standardization
std = StandardScaler()
X_std = std.fit_transform(X)
# print(X_std)

#Handling Categorical Data
#Label Encoder for FuelType
Z = datasets.iloc[:, 4].values
print(Z)
le = LabelEncoder()
Z[:] = le.fit_transform(Z[:])
# print(Z[0])

#One column for each fuletype
dummy = pd.get_dummies(datasets['FuelType'])
# print(dummy)
datasets.drop(['FuelType'],axis=1)
datasets = pd.concat([dummy, datasets], axis=1)
# print(datasets)

#Feature Selection
datasets = pd.read_csv('Exercise-CarData.csv')
data = datasets.iloc[:, 1:3]

#Correlation
corr = data.corr()
# corr.head()

# sns.heatmap(corr)

#Remove correlation higher than 0.9
columns = np.full((corr.shape[0],), True, dtype=bool)
for i in range(corr.shape[0]):
    for j in range(i+1, corr.shape[0]):
        if corr.iloc[i,j] >= 0.9:
            if columns[j]:
                columns[j] = False
selected_columns = data.columns[columns]
# selected_columns.shape

data = data[selected_columns]
print(data)