Price = []
Quantity = []

for i in range(3):
    Price.append(int(input("Enter the price:")))
    Quantity.append(int(input("Enter quantity:")))
    subtotal=0
for i in range(3):
    subtotal = subtotal + Price[i] + Quantity[i]
discount = subtotal*10/100
amount = subtotal - discount
gst = amount*18/100
final_amount = amount + gst

print("Subtotal:",subtotal)
print("Discount:",discount)
print("Amount:",amount)
print("GST:",gst)
print("Final Amount:",final_amount)
