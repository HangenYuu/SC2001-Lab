import random

def generate_input(size: int, max_val: int) -> list:
    return [random.randint(0, max_val) for i in range(size)]

sizes = [10**3, 10**4, 10**5, 10**6, 10**7]

for size in sizes:
    with open(f"input_size_{size}.txt", 'w') as file:
        for item in generate_input(size, size):
            file.write(f"{item}\n")
    print(f"Generated input of size {size} and wrote it to input_size_{size}.txt")