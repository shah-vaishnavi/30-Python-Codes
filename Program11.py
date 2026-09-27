Persons_age = int(input("Enter your age:"))
Monthly_income = float(input("Enter your monthly income:"))
credit_score = int(input("Enter your credit score:"))

if Persons_age >= 21 and Monthly_income >= 25000 and credit_score >= 700:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")