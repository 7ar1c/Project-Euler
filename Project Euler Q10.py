## Project Euler Q10 Solution
## Find the sum of all the primes below two million.
import math
def isprime(n):
    for j in range(2, math.floor(math.sqrt(n))+1):
        if n % j == 0:
            return False
    return True

sum_of_primes = 0

for i in range(2, 2000000):
    if isprime(i):
        sum_of_primes += i
print(sum_of_primes)