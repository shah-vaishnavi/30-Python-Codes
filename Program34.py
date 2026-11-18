x = 10

def display():
    global x
    y = 20

    print("Global variable:", x)
    print("Local variable:", y)

    x = 30

display()

print("Modified global variable:", x)

square = lambda a: a * a
cube = lambda a: a * a * a
maximum = lambda a, b: max(a, b)
addition = lambda a, b: a + b

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

print("Square:", square(num1))
print("Cube:", cube(num1))
print("Maximum:", maximum(num1, num2))
print("Addition:", addition(num1, num2))