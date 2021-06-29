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


#Dataset - Bank customer

Bank_Customers = pd.read_csv("data.csv")

print(df.head())
#Count missing values in each column
missing_values_count = netflix_data.isnull().sum()
print(missing_values_count[0:5])

#Drop rows where data is missing
droprows= netflix_data.dropna()
print(netflix_data.shape,droprows.shape)
#Drop Colunm where data is missing
dropcolumns = netflix_data.dropna(axis=1)
print(netflix_data.shape,dropcolumns.shape)

#Fill All missing values with 0
cleaned_data = netflix_data.fillna(0)
#Fill all missing values to the value that comes next in the same column
cleaned_data = netflix_data.fillna(method='bfill', axis=0).fillna(0)

#Drop rows where data is missing
droprows= netflix_data.dropna()
print(netflix_data.shape,droprows.shape)

#Drop Columns where data is missing
dropcolumns = netflix_data.dropna(axis=1)
print(netflix_data.shape,dropcolumns.shape)
#Fill all missing values with 0
cleaned_data = netflix_data.fillna(0)

#Fill all missing values to the value that comes next in the same column
cleaned_data = netflix_data.fillna(method='bfill', axis=0).fillna(0)
#Fill all missing values to the value that comes next in the same column
cleaned_data = netflix_data.fillna(method='bfill', axis=0).fillna(0)

#Drop all rows that are duplicates
drop_duplicates= netflix_data.drop_duplicates()
print(netflix_data.shape,drop_duplicates.shape)
#Drop Duplicate Rows based on specific columns
drop_duplicates= netflix_data.drop_duplicates(subset=['show_id'])
print(netflix_data.shape,drop_duplicates.shape)










#Creating a list in python

job = ["admin", "technican", "management", "blue_collar", "services", "student", "self_employed", "housemaid", "retired", "un_employed", "entrepreneur"]
Martial_Status = ["single", "married", "divorced"]



#I want to subset the jobs were people arent working
jobs_subset = job[8:10]
print(jobs_subset)




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











