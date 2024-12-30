# Find the sum of all primes below 2 million

# Could brute force this, but it will be fun to implement the Sieve of Eratosthenes.

# start with a map of every integer from 1 to the upper limit, initially with every
# value set to True (representing that it is prime).

sieve = {}
UPPER_BOUND = 2000000
for i in range(2, UPPER_BOUND):
    sieve[i] = True

for i in sieve:
    if sieve[i]:
        for num in range(i*i, UPPER_BOUND, i):
            sieve[num] = False

sum = 0
for i in sieve:
    if sieve[i]:
        sum = sum + i

print(f'Sum of primes: {sum}')