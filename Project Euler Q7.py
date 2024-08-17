## Project Euler Q7 Solution
## What is the 10 001st prime number?
import math
def isprime(n):
    for j in range(2, math.floor(math.sqrt(n))+1):
        if n % j == 0:
            return False
    return True
primecount = 0
n = 2
while n >=0:
    if isprime(n):
        primecount += 1
    if primecount == 10001:
        print(n)
        break
    n += 1