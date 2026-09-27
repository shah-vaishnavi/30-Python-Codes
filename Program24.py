n = int(input("Enter number of terms: "))

a = 0
b = 1
total = 0

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")

    total = total + a

    c = a + b
    a = b
    b = c

print()
print("Sum:", total)