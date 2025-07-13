def merge_sort(arr):
    # Base case: if array has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Split array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both halves and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements from both halves (if any)
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Example usage
arr = [3,2,1,4]
sorted_arr = merge_sort(arr)
print(sorted_arr)