arr = [1,3,13,2,25,23,2,4,2]

n = len(arr)

for i in range(n):
    key = arr[i]
    j = i-1
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = key

print(arr)