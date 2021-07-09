#basic sum function

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
#I will loop through the ages list and pnly print even numbers, and i wont print anything at the age of 65
ages = [95, 94, 92, 90, 89, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50
       ]
for age in ages:
    if age == 65:
        break

        if number %2 ==1:
            continue
print(age)


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
