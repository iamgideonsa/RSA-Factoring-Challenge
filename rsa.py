#!/usr/bin/python3

import sys
import math

def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_rsa(n):
    """Split the RSA of a number"""
    a = int(math.sqrt(n)) + 1
    while True:
        b = a ** 2 - n
        if math.isqrt(b) ** 2 == b:
            c = math.isqrt(b)
            break
        a += 1
    if is_prime(a + c) and is_prime(a - c):
        print(f"{n}={a + c}*{a - c}")

def start():
    """Entry point of the script"""
    if len(sys.argv) < 2:
        print("Error!: <USAGE> -> ./rsa filename")
        sys.exit(1)
    
    filename = sys.argv[1]
    with open(filename) as file_in:
        line = file_in.readline().strip()
    
    if not line:
        print("The file is empty")
        sys.exit(1)
    
    is_rsa(int(line))

start()

