import requests

Microsoft_Stock=requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=1S103UUI8J864BDK")
print(Microsoft_Stock)
Stock_Data=Microsoft_Stock.json()
print(Stock_Data)
print(Stock_Data["Meta Data"])

Microsoft_Stock_Overview=requests.get("https://www.alphavantage.co/query?function=OVERVIEW&symbol=MSFT&apikey=1S103UUI8J864BDK")
print(Microsoft_Stock_Overview.status_code)

# Date and time now
import datetime
now = datetime.datetime.now()
print(now)

import pandas as pd
from matplotlib import pyplot as plt

GDP_Data = pd.read_csv('gdp_csv.csv')
#checking if there are some missing values
print(GDP_Data.isnull().sum())

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

Ireland.plot(x="Year", y="Value", kind="line", title="Ireland GDP")
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

#Showed a simple matplot lib chart using marker & linestyle
import matplotlib.pyplot as plt
fix,ax=plt.subplots()
x = ["Germany", "France", "Belgium", "Netherlands", "Italy", "Luxembourg"]
y = [1.237255e+12, 1.858913e+12, 2.465454e+12, 3.477796e+12, 1.953051e+11, 4.713644e+11]
ax.plot(x,y, color="green", linestyle="--", marker="*")
plt.show()

stocks = pd.read_csv("Microsoft_Stock.csv")

print(stocks.head(10))
print(stocks.tail(10))
print(stocks.describe())
print(stocks.dtypes)
print(stocks.info)

## Renaming column names and converting the data types
Stocks_df = stocks
Stocks_df.columns = ["Date", "Open", "High", "Low", "Close", "Volume"]

Stocks_df.plot(x='Date', y='Close', rot=90, title="Microsoft Stock Price")
plt.show()

Stocks_df.plot(x='Date', y='Volume', kind='hist', rot=90, title="Microsoft Stock Price")
plt.show()

#sorting dataframe - you pass a single argument to the method containing the name of the column you want to sort by.
print(stocks.sort_values("Volume"))
print(stocks.head(20))

Customer_Data = pd.read_csv("data.csv")
print(Customer_Data.head())
print(Customer_Data.shape)
#correltaion which columns are depenndents on each other
print(Customer_Data.corr())

print(Customer_Data.isnull().sum())

#Print the row index of Bank Customer Data
print(Customer_Data.index)

print(Customer_Data.columns)

#Index Customer Data by job
Customer_Data_Ind = Customer_Data.set_index(("job"))
print(Customer_Data_Ind)
# Reset the index, keeping its contents
print(Customer_Data_Ind.reset_index())

print(Customer_Data_Ind.reset_index(drop=True))

print(Customer_Data.sort_values("marital"))
#Sort in Descending order
print(Customer_Data.sort_values("age", ascending=False))
# Sort Customer Data by age, then descending Martial Status
Customer_Data_Age = Customer_Data.sort_values(["age", "marital"], ascending=[True, False])
print(Customer_Data_Age.head())

#Subsetting just the Education Column
print(Customer_Data["education"])

#Creating a data Frame

Job = pd.DataFrame([["retired", "admin", "blue Collar", "management", "self-employed",
                    "student", "services", "technician"]])

# Itering over the data frame rows
# using df.iterrows()
itr = next(Job.iterrows())[1]
print(itr)

#Dropping Duplicates

Employee_Details = pd.read_csv("current-employee-names-salaries-and-position-titles-1.csv")
#Checking info, to see if there missing
print(Employee_Details.info())
#checking if there are some missing values - Is isnull sum is a function sums missing values
print(Employee_Details.isnull().sum())

#Drop Columns instead of rows use the axis 1 -
Missing_Value = Employee_Details.dropna(axis=1)
print(Employee_Details.shape,Missing_Value.shape)
print(Employee_Details.shape,Missing_Value.shape)

droprows= Employee_Details.dropna()
print(Employee_Details.shape,droprows.shape)

print(Employee_Details.drop_duplicates(subset="Name"))
Job_titles = Employee_Details.drop_duplicates(subset=["Name", "Department"])
print(Job_titles.head())

Missing_Value = Employee_Details.fillna(Missing_Value.mean)

Missing_Value = Employee_Details.fillna(method="bfill", axis=None).fillna(0)

#Grouped Summaries
# Group by type; calc total weekly sales
Employee_Details_Dept = Employee_Details.groupby("Job Titles")["Typical Hours"].sum()
print(Employee_Details_Dept)

Employee_Details_Multiple = Employee_Details.groupby(["Job Titles", "Department"])["Typical Hours"].sum()
print(Employee_Details_Multiple)

Employee_Details = pd.read_csv("current-employee-names-salaries-and-position-titles-1.csv")
print(Employee_Details.head())
print(Employee_Details.isnull().sum())

print(Employee_Details['Annual Salary'].value_counts().head(10))
print(Employee_Details['Hourly Rate'].value_counts().head(10))

annual_Salary = [104628, 45720, 52176, 54768, 84054, 72510, 84054, 76266, 1000980, 92274]
annual_Salary.sort()
print(annual_Salary)

import numpy as np
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[2])
print(type(a))

array_a = np.array([1, 2, 3, 4])
array_b = np.array([9, 10, 11, 12])
print(array_a + array_b)

#Two dimensional arrays
#Using customer data to get the total balance by month

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

Total_Balance_std = np.std(Total_Balance)
print(Total_Balance_std)
Total_Balance_mean = np.mean(Total_Balance)
print(Total_Balance_mean)

Employee_Details = pd.read_csv("current-employee-names-salaries-and-position-titles-1.csv")
print(Employee_Details.info())

print(Employee_Details['Annual Salary'].value_counts().head(10))
print(Employee_Details['Hourly Rate'].value_counts().head(10))
print(len(Employee_Details))

Annual_Salary = [90024, 87006, 93354, 48078, 84054, 72510, 96060, 76266, 1000980, 92274]
annual_salary_array = np.array(Annual_Salary)
#Calculating the mean of an inputt
print(np.mean(annual_salary_array))
print(np.std(annual_salary_array))

#Merging Dataframes
Employee_Details_Dept = pd.DataFrame({'Name': ['Mike', 'Michelle', 'James', 'Dennis', "David"],
                    'Department': ['Fire', 'Police', 'Human Resources', 'Finance', "Law"]})
Employee_Details_Salary = pd.DataFrame({'Name': ['Michelle', "Mike", 'Dennis', 'David', "James", ],
                    'Salary': [100656, 100776, 99648, 99780, 98592]})

inner_merged = pd.merge(Employee_Details_Dept, Employee_Details_Salary)
print(inner_merged)

concatenated = pd.concat([Employee_Details_Dept, Employee_Details_Salary], axis=1)
print(concatenated)

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


Population_2020 = pd.read_csv('population_by_country_2020.csv')

Countries = ["China", "India", "United States", "Indonesia", "Pakstan"]
total_populations = [1438207241, 1377233523, 330610570, 272931713, 219992900,]

plt.plot(Countries, total_populations)
plt.title("Countries vs Population in 2020")
plt.xlabel("Countries")
plt.ylabel("total_population")
plt.show()

import matplotlib.pyplot as plt

Median_Age = [38, 28, 38, 30, 23,]
Countries = ["China", "India", "United States", "Indonesia", "Pakistan"]

plt.scatter(Median_Age, Countries)
plt.title("Median Age of Highest Population")
plt.xlabel("Median Age")
plt.ylabel("Highest Population")
plt.show()


Fertility_rate = [1.7, 2.2, 1.8, 2.3, 3.6,]

plt.hist(Fertility_rate, bins = 3)
plt.xlabel("Number")
plt.ylabel("Frequency")
plt.show()

# Our data
Countries = ["China", "India", "United States", "Indonesia", "Pakistan"]
Urban_Population = [61, 35, 83, 56, 35]

# Generating the y positions. Later, we'll use them to replace them with labels.
y_positions = range(len(Countries))

