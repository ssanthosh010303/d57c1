# Author: Apache X692 Attack Helicopter
# Created on: 29/06/2024
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True

def list_n_primes(n):
    primes = []
    num = 2

    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1

    return primes

def main():
    n = int(input("Enter the value of N: "))

    if n <= 0:
        print("N should be a positive integer.")
    else:
        prime_list = list_n_primes(n)
        print(f"The first {n} prime numbers are: {prime_list}")

if __name__ == "__main__":
    main()
