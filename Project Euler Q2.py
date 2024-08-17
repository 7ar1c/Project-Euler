##Project Euler Q2 Solution
##By considering the terms in the Fibonacci sequence whose
# values do not exceed four million, find the sum of the even-valued terms.
nextterm = 0
i = 1
j = 0
ans = 0
while nextterm < 4000000:
        nextterm = i + j
        j = i
        i = nextterm
        if nextterm % 2 == 0:
            ans += nextterm

print(ans)