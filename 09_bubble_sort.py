arr = [12, 43, 12, 4, 1, 42, 1, 53, 1]
n = len(arr)

for i in range(n):
    isSorted = False
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            isSorted = True
    if not isSorted:
        break

print(arr)


# 🧠 Time Complexity:
# Best case: O(n) (when optimized and array is already sorted)

# Average/Worst case: O(n²)

# Space complexity: O(1)
