class ComparisonCounter:
    def __init__(self):
        self.count = 0

    def is_less_than(self, a: int, b: int) -> bool:
        self.count += 1
        return a < b

    def increment_count(self, value: int):
        self.count += value

    def reset_count(self):
        self.count = 0

    def get_count(self):
        return self.count
