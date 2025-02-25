# Which prime, below one-million, can be written as the sum of the most consecutive primes?

# Step 1- use the Sieve of Eratosthenes to find the primes from 1 to one million exclusive

sieve = {}
UPPER_BOUND = 1000000
for i in range(2, UPPER_BOUND):
    sieve[i] = True

for i in sieve:
    if sieve[i]:
        for num in range(i*i, UPPER_BOUND, i):
            sieve[num] = False

primes = []
for i in sieve:
    if sieve[i]:
        primes.append(i)

# Step 2- sliding window. If below target. add next number. if above target, subtract first number.
# if current number to add > target or at end of list, return -1

def num_consecutive_primes(target):
    left = 0
    right = 1
    num_consecutive = 1
    curr = primes[0]
    while right < len(primes) and primes[right] < target:
        if curr == target:
            return num_consecutive
        elif curr < target:
            curr = curr + primes[right]
            right = right + 1
            num_consecutive = num_consecutive + 1
        else:
            curr = curr - primes[left]
            left = left + 1
            num_consecutive = num_consecutive - 1
    return -1

# step 3- for each prime below 1 million, determine consecutive sum. If it is greater than the current
# max consecutive, overwrite
curr = 0
curr_max = 0
for prime in primes:
    res = num_consecutive_primes(prime)
    if res != -1:
        print(f'{prime} is the sum of {res} consecutive primes')
    else:
        print(f'No answer found for {prime}')
    if res > curr_max:
        curr = prime
        curr_max = res
print(f'Final Answer: {curr} (can be written as sum of {curr_max} consecutive primes)')