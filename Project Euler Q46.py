## Project Euler Q46 Solution
## What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
import math
def isprime(n):
    for j in range(2, math.floor(math.sqrt(n))+1):
        if n % j == 0:
            return False
    return True

def is_twice_square(n):
    for i in range(0, math.floor(math.sqrt(n))+1):
        remainder = n - 2*i**2
        if remainder < 0:
            continue
        if isprime(remainder):
            return True   
    return False

j = 1
while j < 10001:
    j += 2
    if isprime(j):
        continue
    if not is_twice_square(j):
        print(j)
        break

is_twice_square(1001)