start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

count = 0

print("Prime numbers:")

for n in range(start, end + 1):

    if n < 2:
        continue

    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(n, end=" ")
        count = count + 1

print()
print("Total prime numbers:", count)