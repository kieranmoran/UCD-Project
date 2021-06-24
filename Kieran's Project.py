import pandas as pd

data = pd.read_csv('gdp_csv.csv')

#make a copy of the data
df = data.copy()

print(df.info())
print(df.shape)
print(df.describe())
print(df.describe().transpose())
print(df.head())
print(df.tail())

#checking if there are some missing values
print(df.isnull().sum())

df["Country Name"].unique()

df.types 




