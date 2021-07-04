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

#Dataframe -Stocks
stocks = pd.read_csv("NSE_BANKING_SECTOR.csv")

print(stocks.info)
print(stocks.describe())
print(stocks.dropna())

#sorting dataframe - you pass a single argument to the method containing the name of the column you want to sort by.
print(stocks.sort_values("TURNOVER"))
print(stocks.head(20))

stocks['DATE']=pd.to_datetime(stocks['DATE'])



#Dataset - Bank customer

Bank_Customers = pd.read_csv("data.csv")

print(df.head())
#Count missing values in each column
missing_values_count = data.isnull().sum()
print(missing_values_count[0:5])

#Drop rows where data is missing
droprows= data.dropna()
print(data.shape,droprows.shape)
#Drop Colunm where data is missing
dropcolumns = data.dropna(axis=1)
print(data.shape,dropcolumns.shape)

#Fill All missing values with 0
cleaned_data = data.fillna(0)
#Fill all missing values to the value that comes next in the same column
cleaned_data = data.fillna(method='bfill', axis=0).fillna(0)

#Drop rows where data is missing
droprows= data.dropna()
print(data.shape,droprows.shape)

#Drop Columns where data is missing
dropcolumns = data.dropna(axis=1)
print(data.shape,dropcolumns.shape)
#Fill all missing values with 0
cleaned_data = data.fillna(0)

#Fill all missing values to the value that comes next in the same column
cleaned_data = data.fillna(method='bfill', axis=0).fillna(0)
#Fill all missing values to the value that comes next in the same column
cleaned_data = data.fillna(method='bfill', axis=0).fillna(0)

#Drop all rows that are duplicates
drop_duplicates= data.drop_duplicates()
print(data.shape,drop_duplicates.shape)
#Drop Duplicate Rows based on specific columns

print(data.shape,drop_duplicates.shape)


#New Dataset
NSE_Banking_Sector = pd.read_csv("NSE_BANKING_SECTOR.csv")
print(NSE_Banking_Sector)

import matplotlib.pyplot as plt
fig,ax = plt.subplots()
plt.show()

x = NSE_Banking_Sector['volume'].head(5)
y1 = NSE_Banking_Sector['turnover'].head(5)
y2 = NSE_Banking_Sector['symbol'].head(5)

ax.plot(x,y1)
ax.plot(x,y2)

ax.plot(x,y1, marker="v", linestyle="--", color="r")
import matplotlib.pyplot as plt
import seaborn as sns
fig,ax = plt.subplots()
plt.show()

seaborn
sns.lineplot(x=data['video_id'].head(25),
		y=data['views'].head(25))











