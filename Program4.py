Seconds = int(input("Enter no.of seconds:"))

hours = Seconds//3600
minutes = (Seconds % 3600)//60
Seconds = Seconds % 60

print("Hours:",hours)
print("Minutes:",minutes)
print("Seconds:",Seconds)
