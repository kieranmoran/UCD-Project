from datetime import datetime

import pandas as pd
from matplotlib import pyplot as plt

# Date and time now
import datetime
now = datetime.datetime.now()
print(now)

GDP_Data = pd.read_csv('gdp_csv.csv')

print(GDP_Data.head)
print(GDP_Data.tail)

#Listing all the countries and regions
print(GDP_Data["Country Name"].unique())
print(GDP_Data["Country Name"].nunique(5))

#For Ireland
Ireland = GDP_Data[GDP_Data['Country Name']=='Ireland']
print(Ireland)
#Shape
print(GDP_Data.shape)

Ireland.plot(x="Year", y="Value", kind="line")
plt.show()

#Creating Lists
Countries_I = ["Iceland", "India", "Indonesia", "Iran", "Islamic Rep", "Iraq", "Ireland", "Isle of Man", "Israel", "Italy"]
Countries_I_GDP_Data = GDP_Data[GDP_Data["Value"].isin(GDP_Data)]
print(len(Countries_I_GDP_Data))

# Use slicing on list names
#Subsetting Indonesia
Countries_I_Subset= Countries_I[2:3]
print(Countries_I_Subset)

#Subsetting from the tail of the list
Countries_I_Subset= Countries_I[-3:-1]
print(Countries_I_Subset)

#Make a list of the 1st 6 countries to join the EU
EU_Countries = ["Germany", "France", "Belgium", "Netherlands", "Italy", "Luxembourg"]
EU_Countries.append("EU_Countries")
print(EU_Countries)

#Extend list names-the next 3 countries to join the EU
Joined_1973 = ["Denmark", "Ireland", "United Kingdom"]
EU_Countries.extend(Joined_1973)
print(EU_Countries)

#Dictionary
Countries_abbreviation = {"Germany":"Ger", "France":"FRA", "Belgium":"Bel", "Netherlands":"Net", "Italy": "Itl", "Luxembourg":"Lux"}
print(Countries_abbreviation)
#adding to Dictionaries
Countries_abbreviation["Irl"] = "Ireland"
print(Countries_abbreviation)
#Accessing Values
print(Countries_abbreviation["Belgium"])

del(Countries_abbreviation["Germany"])

import pandas as pd
stocks = pd.read_csv("Microsoft_Stock.csv")

print(stocks.head())
print(stocks.tail())
print(stocks.describe())
print(stocks.dtypes)

## Renaming column names and converting the data types
df = stocks
df.columns = ["Date", "Open", "High", "Low", "Close", "Volume"]

#The rotation parameter lets us rotate the labels of the plot
df.plot(x='Date', y='Close', rot=90, title="Microsoft Stock Price")
plt.show()


#Histogram plot is a great way to see the distribution of values.
df.plot(x='Date', y='Volume', kind='hist', rot=90, title="Microsoft Stock Price")
plt.show()


