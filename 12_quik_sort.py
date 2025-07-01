def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose middle element as pivot
    left = [x for x in arr if x < pivot]     # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]    # Elements greater than pivot

    return quick_sort(left) + middle + quick_sort(right)


arr = [12,34,23,5,23,53,23,5,23,23]
print(quick_sort(arr))
