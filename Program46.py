import sys

if len(sys.argv) != 4:
    print("Usage: python program.py num1 operator num2")
    sys.exit()

try:
    a = float(sys.argv[1])
    operator = sys.argv[2]
    b = float(sys.argv[3])

    if operator == "+":
        result = a + b

    elif operator == "-":
        result = a - b

    elif operator == "*":
        result = a * b

    elif operator == "/":
        if b == 0:
            print("Division by zero is not allowed")
            sys.exit()

        result = a / b

    else:
        print("Invalid operator")
        sys.exit()

    print("Result:", result)

except ValueError:
    print("Please enter valid numbers")
