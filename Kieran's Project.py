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











