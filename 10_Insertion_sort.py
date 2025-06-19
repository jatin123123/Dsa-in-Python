# Initial unsorted array
arr = [12, 3, 123, 12, 43, 2, 21, 1, 0, 23, 2]

# Get the number of elements in the array
n = len(arr)

# Start from the second element (index 1) since the first is considered sorted
for i in range(1, n):
    key = arr[i]        # Current element to be placed at the correct position
    j = i - 1            # Index of the last element in the sorted part of the array

    # Shift elements of the sorted part that are greater than key to one position ahead
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]  # Shift element to the right
        j -= 1               # Move to the previous element

    # Insert the key at its correct position in the sorted part
    arr[j + 1] = key

# Print the sorted array
print(arr)


#🧮 Time Complexity:
# Best case (already sorted): O(n)
            
# Average/Worst case: O(n²)

# Space: O(1) (in-place)

