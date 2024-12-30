# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20


def prime_factorization(n):
    factors = []
    curr_factor = 2
    while curr_factor <= n:
        while n % curr_factor == 0:
            factors.append(curr_factor)
            n = n / curr_factor
        curr_factor = curr_factor + 1
    return factors

print(prime_factorization(2520))

# # What is the prime factorization of 1-10?
# # and how does it relate to 2520
# for i in range(1, 11):
#     print(f'{i}: {prime_factorization(i)}')

# find the max number of times each prime factor appears in any of the factorizations
# Then multiply all those numbers together
factor_counts = {}
for i in range(1, 21):
    # get the prime factorization of this number
    factors = prime_factorization(i)
    print(f'{i}: {factors}')
    # create mapping of factors to counts WITHIN this factorization
    curr_counts = {}
    for factor in factors:
        if factor in curr_counts:
            curr_counts[factor] = curr_counts[factor] + 1
        else:
            curr_counts[factor] = 1
 
    # update mapping of overall factor_counts
    for factor in  curr_counts:
        if factor not in factor_counts or factor_counts[factor] < curr_counts[factor]:
            factor_counts[factor] = curr_counts[factor]

product = 1
for i in factor_counts:
    times = factor_counts[i]
    for j in  range(times):
        product = product * i

print(f'Result: {product}')