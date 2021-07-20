
# Import pandas library
import matplotlib.pyplot as plt
import pandas
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

Countries_EU = ["Germany", "France", "Belgium", "Netherlands", "Italy", "Luxembourg"]
Values = [1.237255e+12, 1.858913e+12, 2.465454e+12, 3.477796e+12, 1.953051e+11, 4.713644e+11]

explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
plt.pie(Values, labels=Countries_EU,
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


Population_2020 = pd.read_csv('population_by_country_2020.csv')

Countries = ["China", "India", "United States", "Indonesia", "Pakstan"]
total_populations = [1438207241, 1377233523, 330610570, 272931713, 219992900,]

plt.plot(Countries, total_populations)
plt.title("Countries vs Population in 2020")
plt.xlabel("total_population")
plt.ylabel("Countries")
plt.show()

import matplotlib.pyplot as plt

Median_Age = [38, 28, 38, 30, 23,]
Countries = ["China", "India", "United States", "Indonesia", "Pakistan"]

plt.scatter(Median_Age, Countries)
plt.title("Median Age of Highest Population")
plt.xlabel("Median Age")
plt.ylabel("Highest Population")
plt.show()


import matplotlib.pyplot as plt

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

# Creating our bar plot
plt.bar(y_positions, Urban_Population)
plt.xticks(y_positions, Countries)
plt.ylabel("Urban Population (%)")
plt.title("Urban Population Percentage")
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
fig,ax = plt.subplots
plt.show()
