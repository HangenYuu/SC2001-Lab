# Generate a random list of 10 million integers between 0 and 10^6
# and write them to a file called input.txt

import random

# Generate a list of 10 million random integers between 0 and 10^6
random_list = [random.randint(0, 10**6) for i in range(10**7)]

# Write the list to a file called input.txt
with open('input.txt', 'w') as f:
    for num in random_list:
        f.write(str(num) + '\n')