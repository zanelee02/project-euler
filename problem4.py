# Find the largest palindrome made from the product of two 3-digit numbers

def is_palindromic(n):
    stringified = str(n)
    i = 0
    j = len(stringified) - 1
    while i < j:
        if stringified[i] != stringified[j]:
            return False
        i = i + 1
        j = j - 1
    return True

# # Testing is_palindromic:
# print(f'12345: {is_palindromic(12345)}')
# print(f'10301: {is_palindromic(10301)}')
# print(f'3003: {is_palindromic(3003)}')

# upper bound is 1000 * 1000 = 1,000,000
# lower bound is 100 * 100  = 10,000

# brute force: start at 999 and try every product

i = 999
max = -1
while i >= 100:
    j = 999
    while j >= 100:
        product = i * j 
        if is_palindromic(product) and product > max:
            max = product
            break
        j = j - 1
    i = i - 1

print(f'Biggest palindromic number: {max}')
