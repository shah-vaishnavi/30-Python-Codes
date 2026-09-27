while True:

    print("\n----- MENU -----")
    print("1. Prime")
    print("2. Palindrome")
    print("3. Armstrong")
    print("4. Factorial")
    print("5. Fibonacci Series")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 6:
        print("Exiting Program...")
        break

    n = int(input("Enter an integer: "))

    # Prime
    if choice == 1:

        if n < 2:
            print("Not Prime")
        else:
            prime = True

            for i in range(2, n):
                if n % i == 0:
                    prime = False
                    break

            if prime:
                print("Prime Number")
            else:
                print("Not Prime")

    # Palindrome
    elif choice == 2:

        original = n
        reverse = 0

        while n > 0:
            digit = n % 10
            reverse = reverse * 10 + digit
            n = n // 10

        if original == reverse:
            print("Palindrome")
        else:
            print("Not Palindrome")

    # Armstrong
    elif choice == 3:

        original = n
        digits = len(str(n))
        total = 0

        while n > 0:
            digit = n % 10
            total = total + digit ** digits
            n = n // 10

        if total == original:
            print("Armstrong Number")
        else:
            print("Not Armstrong Number")

    # Factorial
    elif choice == 4:

        factorial = 1

        for i in range(1, n + 1):
            factorial = factorial * i

        print("Factorial:", factorial)

    # Fibonacci
    elif choice == 5:

        a = 0
        b = 1

        print("Fibonacci Series:")

        for i in range(n):
            print(a, end=" ")

            c = a + b
            a = b
            b = c

        print()

    else:
        print("Invalid Choice")