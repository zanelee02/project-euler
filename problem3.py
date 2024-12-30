# What is the largest prime factor of the number 600851475143?

# We actually don't need to test for prime-ness, as it will be implicitly captured
# by the incrememntal nature of this algorithm. 
def prime_factorization(n):
    factors = []
    curr_factor = 2
    while curr_factor <= n:
        while n % curr_factor == 0:
            factors.append(curr_factor)
            n = n / curr_factor
        curr_factor = curr_factor + 1
    return factors

factors = prime_factorization(600851475143)
print(f'Largest prime factor of 600851475143: {factors[len(factors) - 1]}')


## KEEPING BELOW FOR ARCHIVE

# to determine if a number is prime, we check if any numbers between 2
# and sqrt(n) inclusive are factors- if not, it is prime
# This would be in O(sqrt(n))
# def is_prime(n):

#     # 1 and 2 are base cases we don't care ab
#     if n == 1:
#         return False
#     if n == 2:
#         return True

#     i = 2
#     while i*i <= n:
#         if n % i == 0:
#             return False
#         i = i + 1
#     return True

# To get the prime factorization of a number, we can start at 2
# and keep dividing it by incrementally increasing prime numbers
# in until the current prime number we are on is larger than the number itself



# # Testing
# res = prime_factorization(13195)
# print(f'Prime factorization of 13195: {res}')
# print(f'Largest prime factor of 13195: {res[len(res) - 1]}')

# Now we ca just get the prime factorization of the big number and find the last element
