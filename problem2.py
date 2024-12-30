# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

prev_val = 1
curr_val = 2
sum = 0

while curr_val < 4000000:
    if curr_val % 2 == 0:
        sum = sum + curr_val
    temp = curr_val + prev_val 
    prev_val = curr_val
    curr_val = temp


print(f'Sum: {sum}')