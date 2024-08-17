## Project Euler Q9 Solution
## There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
def c(x,y):
    return (x**2 + y**2)**0.5

for a in range(1,1000):
    for b in range(a, 1000):
        if a + b + c(a,b) == 1000:
            print(a*b*c(a,b))
            break

