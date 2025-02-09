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

    if i < len(left_half):
        h = len(left_half) - i
        arr[k : k + h] = left_half[i : i + h]
        i += h
        k += h

    if j < len(right_half):
        h = len(right_half) - j
        arr[k : k + h] = right_half[j : j + h]
        j += h
        k += h

    return arr


def merge_sort(arr: list, comparison_counter: ComparisonCounter) -> list:
    mid = len(arr) // 2

    if len(arr) > 2:

        arr[:mid] = merge_sort(arr[:mid], comparison_counter)
        arr[mid:] = merge_sort(arr[mid:], comparison_counter)

    arr = merge(arr, arr[:mid], arr[mid:], comparison_counter)
    return arr


def hybrid_sort(arr: list, comparison_counter: ComparisonCounter, S: int):
    if len(arr) < 2:
        return arr

    if len(arr) <= S:
        arr = insertion_sort(arr, comparison_counter)
        return arr

    mid = len(arr) // 2

    arr[:mid] = hybrid_sort(arr[:mid], comparison_counter, S)
    arr[mid:] = hybrid_sort(arr[mid:], comparison_counter, S)

    arr = merge(arr, arr[:mid], arr[mid:], comparison_counter)

    return arr
