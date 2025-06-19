def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the middle
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursively sort left half
        merge_sort(right_half)  # Recursively sort right half

        # Merging the sorted halves
        i = j = k = 0

        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


arr = [12,34,23,5,23,53,23,5,23,23]

merge_sort(arr)

print(arr)