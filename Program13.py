pin = input("Enter PIN: ")
balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))
correct_pin = "1234"
if pin != correct_pin:
    print("Invalid PIN")
elif amount <= 0:
    print("Invalid withdrawal amount")
elif amount > balance:
    print("Insufficient Balance")
else:
    balance -= amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)