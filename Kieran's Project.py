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

#Sorting - Bank Customer Data

import pandas as pd
Customer_Data = pd.read_csv("data.csv")
print(Customer_Data.head())
print(Customer_Data.shape)
#Print the row index of Bank Customer Data
print(Customer_Data.index)
# Print the column index of homelessness
print(Customer_Data.columns)

#Index Customer Data by job
Customer_Data_Ind = Customer_Data.set_index(("job"))
print(Customer_Data_Ind)
# Reset the index, keeping its contents
print(Customer_Data_Ind.reset_index())
# Reset the index, dropping its contents
print(Customer_Data_Ind.reset_index(drop=True))



print(Customer_Data.sort_values("marital"))
#Sort in Descending order
print(Customer_Data.sort_values("age", ascending=False))
# Sort Customer Data by age, then descending Martial Status
Customer_Data_Age = Customer_Data.sort_values(["age", "marital"], ascending=[True, False])
print(Customer_Data_Age.head())

#Subsetting just the Education Column
print(Customer_Data["education"])

#Dropping Duplicates
import pandas as pd
Employee_Details = pd.read_csv("current-employee-names-salaries-and-position-titles-1.csv")
#Checking info, to see if there missing
print(Employee_Details.info())
#checking if there are some missing values - Is isnull sum is a function sums missing values
print(Employee_Details.isnull().sum())

#Drop Columns instead of rows use the axis 1 -
Missing_Value = Employee_Details.dropna(axis=1)
print(Employee_Details.shape,Missing_Value.shape)
print(Employee_Details.shape,Missing_Value.shape)

print(Employee_Details.drop_duplicates(subset="Name"))
Job_titles = Employee_Details.drop_duplicates(subset=["Name", "Department"])
print(Job_titles.head())

#If i wanted to fill the missing values i would use the following code -
Missing_Value = Employee_Details.fillna(Missing_Value.mean)
#bfill is backword value, fill all missing values to the value that comes next in the same column
Missing_Value = Employee_Details.fillna(method="bfill", axis=None).fillna(0)


#Grouped Summaries

Employee_Details_Dept = Employee_Details.groupby("Job Titles")["Typical Hours"].sum()
print(Employee_Details_Dept)

Employee_Details_Multiple = Employee_Details.groupby(["Job Titles", "Department"])["Typical Hours"].sum()
print(Employee_Details_Multiple)









