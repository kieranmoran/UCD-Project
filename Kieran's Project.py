import requests
# basics of using a Stock Market API
Microsoft_Stock=requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=1S103UUI8J864BDK")
print(Microsoft_Stock)
Stock_Data=Microsoft_Stock.json()
print(Stock_Data)
print(Stock_Data["Meta Data"])

Microsoft_Stock_Overview=requests.get("https://www.alphavantage.co/query?function=OVERVIEW&symbol=MSFT&apikey=1S103UUI8J864BDK")
print(Microsoft_Stock_Overview.status_code)

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
#We have the GDP data from 1960 to 2016, The lowest GDP registered was 8,824,447.74
print(GDP_Data.describe())

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
#correltaion which columns are depenndents on each other
print(Customer_Data.corr())

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
# Group by type; calc total weekly sales
Employee_Details_Dept = Employee_Details.groupby("Job Titles")["Typical Hours"].sum()
print(Employee_Details_Dept)

Employee_Details_Multiple = Employee_Details.groupby(["Job Titles", "Department"])["Typical Hours"].sum()
print(Employee_Details_Multiple)



#Numpy
import numpy as np

import pandas as pd
Employee_Details = pd.read_csv("current-employee-names-salaries-and-position-titles-1.csv")

print(Employee_Details['Annual Salary'].value_counts().head(10))
print(Employee_Details['Hourly Rate'].value_counts().head(10))

annual_Salary = [104628, 45720, 52176, 54768, 84054, 72510, 84054, 76266, 1000980, 92274]

import numpy as np
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[2])
print(type(a))

array_a = np.array([1, 2, 3, 4])
array_b = np.array([9, 10, 11, 12])
print(array_a + array_b)


#Two dimensional arrays
#Using customer data to get the total balance by month
import numpy as np
Months = ["Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
Total_Balance = [13790, 6379, 161861, 364772, 188432, 142142, 397764, 91608, 238760, 332773, 83141]

Total_Balance_Month = np.array([Months, Total_Balance])
print(Total_Balance_Month)

months_transposed = np.transpose(Total_Balance_Month)
print(months_transposed)

months_array = np.array(["Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"])
indexing_array = np.array([2, 5, 5])
months_subset = months_array[indexing_array]
print(months_subset)

import pandas as pd
Employee_Details = pd.read_csv("current-employee-names-salaries-and-position-titles-1.csv")

print(Employee_Details['Annual Salary'].value_counts().head(10))
print(Employee_Details['Hourly Rate'].value_counts().head(10))
print(len(Employee_Details))

import numpy as np
Annual_Salary = [90024, 87006, 93354, 48078, 84054, 72510, 96060, 76266, 1000980, 92274]
annual_salary_array = np.array(Annual_Salary)
#Calculating the mean of an inputt
print(np.mean(annual_salary_array))
print(np.std(annual_salary_array))

Highest_Balance = [102127, 98417, 81204, 71188, 66721]
#Implmenting_Loops

Education =["secondary", "tertiary", "primary", "unknown"]
#For Loops
#For loops iterate over a given sequence
Highest_Balance = [102127, 98417, 81204, 71188, 66721, 66653, 59649, 58544, 57435]
for Highest_Balance in [102127, 98417, 81204, 71188, 166721, 66653, 59649, 58544, 57435]:
 print(Highest_Balance)

for Highest_Balance in range(5):
    print(Highest_Balance)


Top_Five = [102127, 98417, 81204, 71188, 66721]
for Top_Five in [102127, 98417, 81204, 71188, 66721]:
    if Top_Five == 102127:
        continue
print(Top_Five)


#While Loops - While loops repeat as long as a certain boolean condition is met
count = 0
while count < 100:
    print(count)
    count += 10

i = 1
while i <=10:
    print(i)
    i=i+1
print("Finish")

import pandas as pd
Customers_Data = pd.read_csv("data.csv")
#Creating a data Frame

df = pd.DataFrame([["retired", "admin", "blue Collar", "management", "self-employed",
                    "student", "services", "technician"]])

# Itering over the data frame rows
# using df.iterrows()
itr = next(df.iterrows())[1]
print(itr)

#Asking what Arraon works at age 50
def name_age(name, age):
     print("What does " + name + " work at age " + age)

name_age("AAron Jeffery", "50")

def Annual_Salary(num):
    return num*num

result = Annual_Salary(316)
print(result)

#Example of a simple sum function
def sum(a, b):
    return a + b

total=sum(10, 20)
print(total)
total=sum(5, sum(10, 20))
print(total)
