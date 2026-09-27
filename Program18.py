n = int(input("Enter an integer: "))

sum_digits = 0
product = 1

while n > 0:
    digit = n % 10

    sum_digits = sum_digits + digit
    product = product * digit

    n = n // 10

print("Sum of digits:", sum_digits)
print("Product of digits:", product)