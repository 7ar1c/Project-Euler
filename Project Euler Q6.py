##Project Euler Q6 Solution
##Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
sum_of_squares = 0
square_of_sum = 0

for i in range(1,101,1):
    sum_of_squares += i**2
    square_of_sum += i

print(square_of_sum**2 - sum_of_squares)