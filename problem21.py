import math

# let d(n) be sum of factors of n
# find sum of all n where n < 10,000 that share d(n) with at least 1 
# other number < 10,000 aka "amicable numbers"

# function to return all the factors of a number
# iterate from 1 to sqrt(n). If some number x even divides n,
# add it and n / x = y to the list of factors
UPPER_BOUND = 10000

def factors(n):
    factors = []
    i = 1
    upper_bound = math.sqrt(n)
    while i <= upper_bound:
        if n % i == 0:
            factors.append(i)
            if i != 1:
                factors.append(n // i)
        i = i + 1
    return factors

print(factors(284))
# evaluate d(n) for each n < 10,000.
# construct a map of n -> d(n)
# on each d(n), look up val associated with it as a key
# if it is current n, add 2 numbers to sum

res = 0
d_n_map = {}
for i in range(UPPER_BOUND):
    d_n = sum(factors(i))
    if d_n in d_n_map and d_n_map[d_n] == i:
        print(f'amicable numbers {i} and {d_n}')
        res = res + d_n + i
    d_n_map[i] = d_n

print(f'ssum of amicable numbers < 10,000: {res}')