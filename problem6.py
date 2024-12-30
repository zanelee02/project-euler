# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

sum_of_squares = 0
sum = 0
i = 1
while i <= 100:
    sum_of_squares = sum_of_squares + i*i 
    sum = sum + i
    i = i + 1
square_of_sums = sum*sum

print(sum_of_squares)
print(square_of_sums)

print(f'Difference: {square_of_sums - sum_of_squares}')