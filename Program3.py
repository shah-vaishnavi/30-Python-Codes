Units = float(input("Enter the units:"))

if Units <= 100:
    bill = Units * 5 
elif Units <= 200:
    bill = (100 * 5) + ((Units - 100) * 7)
elif Units <= 300:
    bill = (100 * 5) + (100 * 7) + ((Units - 200) * 10)
else:
    bill = (100 * 5) + (100 * 7) + (100 * 10) + ((Units - 300) * 15)

print("Electricity Bill:",bill)    

    