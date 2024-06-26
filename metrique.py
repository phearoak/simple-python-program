#!/usr/bin/env python3

# Ce programme calcule la factorielle d'un nombre et vérifier si ce nombre est premier

# Fonction pour calculer la factorielle d'un nombre
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
# Fonction pour vérifier si un nombre est premier
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Fonction principale
def main():
    number = 5
    print('Factorial of {} is {}'.format(number, factorial(number)))
    if (is_prime(number)):
        print('{} is a prime number'.format(number))
    else:
        print('{} is not a prime number'.format(number))

if __name__ == '__main__':
    main()

