secret = 50

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret:
        print("Correct! You found the number.")
        break
    elif guess < secret:
        print("Too Low")
    else:
        print("Too High")