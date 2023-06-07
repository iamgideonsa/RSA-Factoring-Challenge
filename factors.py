#!/usr/bin/python3

import sys

def factorize_number(number):
    factors = []
    for i in range(2, number):
        if number % i == 0:
            factors.append((i, number // i))
    return factors

def factorize_file(filename):
    with open(filename, 'r') as file:
        numbers = file.read().splitlines()
    
    factorizations = []
    for number in numbers:
        number = int(number)
        factors = factorize_number(number)
        for factor in factors:
            factorizations.append(f"{number}={factor[0]}*{factor[1]}")
    
    for factorization in factorizations:
        print(factorization)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: factors <file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    factorize_file(filename)

