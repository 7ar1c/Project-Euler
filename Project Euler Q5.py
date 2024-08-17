##Project Euler Q5 Solution
##What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
i = 0
while i >= 0:
    i += 20
    if i % 19 == 0 and i % 18 == 0 and i % 17 == 0 and i % 16 == 0 and i % 15 == 0 and i % 14 == 0 and i % 13 == 0 and i % 12 == 0 and i % 11 == 0:
        print(i)
        break
    else:
        continue