def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b=1):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(a=num1, b=num2))
print("Multiplication:", multiply(a=num1, b=num2))
print("Division:", divide(num1, num2))
print("Division with default argument:", divide(num1))