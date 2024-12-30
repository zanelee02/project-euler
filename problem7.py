# What is the 10,001st prime number?

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True

    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True

count = 0
i = 0
while count < 10001:
    i = i + 1
    if is_prime(i):
        count = count + 1
    
print(f'nth prime: {i}')