import random


def generate_input(size: int, max_val: int) -> list:
    return [random.randint(1, max_val) for i in range(size)]
