import random

print("\n🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.\n")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number.\n")
