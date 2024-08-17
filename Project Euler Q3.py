## Project Euler Q3 Solution
## What is the largest prime factor of the number 600851475143 ?

import math

def isprime(n):
    for j in range(2, math.floor(math.sqrt(n))+1):
        if n % j == 0:
            return False
    return True
        
number = 600851475143
factorlist = []
        
for i in range(2, math.floor(math.sqrt(number))+1):
    if number % i == 0 and isprime(i):
        factorlist.append(i)
answer = max(factorlist)
print(answer)
print(factorlist)
        
