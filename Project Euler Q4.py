## Project Euler Q4 Solution
## Find the largest palindrome made from the product of two 3-digit numbers.
answerlist = []
def ispalindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
    

for i in range(100,1000,1):
    for j in range(100,1000,1):
        if ispalindrome(i*j):
            answerlist.append(i*j)
            break
print(max(answerlist))