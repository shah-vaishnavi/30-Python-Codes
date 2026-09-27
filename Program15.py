usage = float(input("Enter monthly mobile data usage (GB): "))
if usage <= 5:
    bill = 199
elif usage <= 15:
    bill = 199 + (usage - 5) * 20
elif usage <= 30:
    bill = 399 + (usage - 15) * 15
else:
    bill = 624 + (usage - 30) * 10
print("Total Bill:", bill)
