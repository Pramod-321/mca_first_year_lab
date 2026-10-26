secret_number = 7

while True:
    guess = int(input("Guess a number from 1 to 10: "))
    if guess == secret_number:
        print("Correct guess")
        break
    print("Try again")
