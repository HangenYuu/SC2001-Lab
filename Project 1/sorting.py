from comparison_counter import ComparisonCounter


def insertion_sort(arr: list, comparison_counter: ComparisonCounter) -> list:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and comparison_counter.is_less_than(key, arr[j]):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


def merge(
    arr: list, left_half: list, right_half: list, comparison_counter: ComparisonCounter
):
    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if comparison_counter.is_less_than(left_half[i], right_half[j]):
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

    return arr


def merge_sort(arr: list, comparison_counter: ComparisonCounter) -> list:
    mid = len(arr) // 2

    if len(arr) > 2:

        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])

    arr = merge(arr, left_half, right_half, comparison_counter)
    return arr


def hybrid_sort(arr, S):
    if len(arr) <= S:
        insertion_sort(arr)
    else:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        hybrid_sort(left_half, S)
        hybrid_sort(right_half, S)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Hemingway bridge: Only hybrid sort and testing is left.
