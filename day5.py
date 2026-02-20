#Input and Typecasting

#Input
name = input("What is your name? ")
print("Welcome",name)


#Typecasting
age = int(input("What is your age? "))
print("Your age is",age)
age +=5
print("Your age after 5 years will be",age)

temperature = float(input("What is the temperature outside? "))
print(type(temperature))

#converting number to string

sales = 10000
text = "Total sales:"+str(sales)
print(text)

#Total Sales Calculator
product = input("Product Name:")
quantity = int(input("Enter quantity sold:"))
 rice_per_unit = float(input("Enter price per unit:"))

# total_sales = quantity * price_per_unit
 print("_________________________________________")
print("Product:", product)
print("Total Sales Amount =", total_sales)
fnum = int(input("Enter first num:"))
snum = int(input("Enter second num:"))
sum = fnum + snum
print("Sum =", sum)

'''Assignment: Salary Slip Calculator
"Create a python program to generate an Employee salary slip"
Write a python program that asks the user to enter:
Employee Name
Basic Salary
Bonus Amount
Tax Percentage

Your program should calculate
Gross Salary = Basic Salary + Bonus Amount
Tax Amount = (Gross Salary * Tax Percentage) / 100
Net Salary = Gross Salary - Tax Amount

Finally, your program should print the salary slip in a formatted manner, displaying all the details and calculations clearly.  
'''
Employee_Name = input("Employee Name:")
Basic_Salary = float(input("Basic Salary:"))
Bonus_Amount = float(input("Bonus Amount:"))
Tax_Percentage = float(input("Tax Percentage:"))

Gross_Salary = Basic_Salary + Bonus_Amount
Tax_Amount = (Gross_Salary * Tax_Percentage) / 100
Net_Salary = Gross_Salary - Tax_Amount
print("_________________________________________")
print("Employee Name:", Employee_Name)
print("Basic Salary:", Basic_Salary)
print("Bonus Amount:", Bonus_Amount)
# print("Gross Salary:", Gross_Salary)
# print("Tax Amount:", Tax_Amount)
# print("Net Salary:", Net_Salary)

