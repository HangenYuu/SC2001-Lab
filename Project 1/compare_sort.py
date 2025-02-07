from mergesort import merge_sort

def sort_file(input_file, output_file):
    with open(input_file, 'r') as file:
        arr = list(map(int, file.readlines()))

    merge_sort(arr)

    with open(output_file, 'w') as file:
        for item in arr:
            file.write(f"{item}\n")

# Example usage
sort_file('input.txt', 'output.txt')