import math

def is_prime(num):
    if num < 1:
        return "Not greater than 1"

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True
    
def find_primes(num):
    if num < 1:
        return "Not greater than 1"

    primes = []
    for i in range(2, num):
        if is_prime(i):
            primes.append(i)

    return primes
    

def erastosthenes(num):
    primes = [True] * (num + 1)
    primes[0] = False
    primes[1] = False

    for i in range(2, int(math.sqrt(num)) + 1):
        if primes[i]:
            for j in range(i * i, num + 1, i):
                primes[j] = False

    return [i for i, prime in enumerate(primes) if prime]

        #find first true, make all following multipels false

while True:
    # num = input("What number would you like to check if its prime?")
    # print(is_prime(int(num)))

    prime_range = input("To what number would you like to find primes? ")
    # print(find_primes(int(prime_range)))
    print(erastosthenes(int(prime_range)))



