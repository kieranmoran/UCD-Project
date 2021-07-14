

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











import pandas as pd
Employee_Details = pd.read_csv("current-employee-names-salaries-and-position-titles-1.csv")



Highest_Balance = [102127, 98417, 81204, 71188, 66721, 66653, 59649, 58544, 57435]


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

