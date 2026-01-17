import random

secret_number = random.randint(1, 100)
attempts = 0

print("Guess the number between 1 and 100!")
while True:
    try:
        guess = int(input("Your guess: "))
        attempts += 1
        if guess < secret_number:
            print("Try a higher number.")
        elif guess > secret_number:
            print("Try a lower number.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid number.")   