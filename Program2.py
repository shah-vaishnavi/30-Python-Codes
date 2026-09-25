Basic_Salary = float(input("Enter bacis salary:"))

da = Basic_Salary * 0.10
hra = Basic_Salary * 0.20

gross = Basic_Salary + da + hra
tax = gross * 10.0
net = gross - tax

print("DA:",da)
print("HRA:",hra)
print("Gross Salary:",gross)
print("Tax Deduction:",tax)
print("Net Salary:",net)
