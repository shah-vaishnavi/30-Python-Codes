def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter a number: "))

print("Factorial:", factorial(num))

terms = int(input("Enter number of Fibonacci terms: "))

print("Fibonacci Series:")

for i in range(terms):
    print(fibonacci(i), end=" ")