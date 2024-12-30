# Find the 13 adjacent digits in the 1000-digit number that have the greates product.
# What is the value of this product?

val = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)

# step 1: partition on 0s and remove anything with len() < 13
partitions = val.split('0')
valid_partitions = []
for option in partitions:
    if len(option) >= 13:
        valid_partitions.append(option)

# for each valid partition, do a sliding window where you divide by the number that just left the partition
# and multiply by the number that just entered

def compute_max(partition):
    curr = 1
    for i in range(13):
        curr = curr * int(partition[i])
    
    max = curr

    i = i + 1
    while i < len(partition):
        curr = curr / int(partition[i - 13])
        curr = curr * int(partition[i])
        if curr > max:
            max = curr
        i = i + 1
    return max

overall_max = 0
for partition in valid_partitions:
    curr_max = compute_max(partition)
    if curr_max > overall_max:
        overall_max = curr_max

print(f'largest product: {overall_max}')