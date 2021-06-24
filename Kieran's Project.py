import pandas as pd

data=pd.read_csv('gdp_csv.csv')

print(data.info())
print(data.shape)
print(data.describe())
print(data.describe().transpose())
print(data.head())
print(data.tail())





