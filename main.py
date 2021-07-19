
# Import pandas library
import matplotlib.pyplot as plt
import pandas as pd

# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])


months = ["jan", "feb", "mar", "april", "may", "june", "july", "aug", "sept", "oct", "nov", "dec"]


GDP_Data = pd.read_csv('gdp_csv.csv')
def Countryinclude_area_plot(country):
    # Slice and create the dataframes
    df_country = df.loc[df['Country Name'] == country]
    # Starting to plot data from the country
    x = df_country['Year']
    y = df_country['Value']
    plt.stackplot(x, y)
    plt.title('GDP plot from 1968 to 2016')
    plt.xlabel('Date')
    plt.ylabel('GDP value (USD)')
    plt.legend(loc='best')


plot1 = plt.figure(2)

Countries = ["Germany", "France", "Belgium", "Netherlands", "Italy", "Luxembourg"]
Values = [1.237255e+12, 1.858913e+12, 2.465454e+12, 3.477796e+12, 1.953051e+11, 4.713644e+11]

explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
plt.pie(Values, labels=Countries,
        shadow=True,
        explode=explode,  # to have the pie open.
        autopct='%1.0f%%',
        pctdistance=0.8,
        startangle=90)
plt.title('1st 6 countries to join the EU')
plt.show()

GDP_Data['Date'] = pd.to_datetime(GDP_Data.Year, format='%Y')
GDP_Data.set_index('Date', inplace=True)
GDP_Data = GDP_Data.loc[GDP_Data["Country Name"] == "Ireland"]
GDP_Data.head()
print(GDP_Data)

import pandas as pd
Employee_Details = pd.read_csv("current-employee-names-salaries-and-position-titles-1.csv")

Highest_Balance = [102127, 98417, 81204, 71188, 66721, 66653, 59649, 58544, 57435]



