# Author: Apache X692 Attack Helicopter
# Created on: 29/06/2024
import random

def generate_secret_number():
    digits = list(range(10))
    random.shuffle(digits)

    if digits[0] == 0:
        digits[0], digits[1] = digits[1], digits[0]

    secret_number = digits[:4]
    return secret_number

def count_cows_and_bulls(secret_number, guess):
    cows = bulls = 0

    for i in range(len(secret_number)):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1

    return (cows, bulls)

def main():
    print("Welcome to the Cow and Bull Game!")

    secret_number = generate_secret_number()
    attempts = 0

    while True:
        guess = input("Enter your guess (4 digits with no repeated digits): ")

        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Invalid input, please enter 4 unique digits.")
            continue

        attempts += 1
        guess = list(map(int, guess))
        cows, bulls = count_cows_and_bulls(secret_number, guess)

        if bulls == 4:
            print(
                f"Congratulations! You've guessed the number {secret_number}"
                f"in {attempts} attempts."
            )
            break
        else:
            print(f"Your guess {guess} has {cows} cows and {bulls} bulls.")

if __name__ == "__main__":
    main()
