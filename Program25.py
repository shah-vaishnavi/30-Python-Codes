n = int(input("Enter an integer: "))

count = 0

print("Factors:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
        count = count + 1

print()
print("Total factors:", count)