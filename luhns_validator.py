# Author: Apache X692 Attack Helicopter
# Created on: 29/06/2024
def luhn_algorithm(card_number):
    card_number = card_number.replace(' ', '')

    if not card_number.isdigit():
        return False

    n_digits = len(card_number)

    if n_digits < 2:
        return False

    total = 0
    parity = n_digits % 2

    for i in range(n_digits):
        digit = int(card_number[i])

        if i % 2 == parity:
            digit *= 2

            if digit > 9:
                digit -= 9

        total += digit

    return total % 10 == 0

def main():
    card_number = input("Enter a credit card number: ")

    if luhn_algorithm(card_number):
        print("The credit card number is valid.")
    else:
        print("The credit card number is not valid.")

if __name__ == "__main__":
    main()
