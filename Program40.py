try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Division:", result)

    numbers = [10, 20, 30]

    index = int(input("Enter list index: "))

    print("Element:", numbers[index])

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Enter valid numerical input")

except IndexError:
    print("Error: Invalid list index")

else:
    print("No exception occurred")

finally:
    print("Finally block executed")

# Raise exception

try:
    age = int(input("\nEnter your age: "))

    if age < 18:
        raise ValueError("Age must be 18 or above")

    print("You are eligible")

except ValueError as e:
    print("Exception:", e)