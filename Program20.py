n = int(input("Enter an integer: "))

original = n
digits = len(str(n))
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit ** digits
    n = n // 10

if sum == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")