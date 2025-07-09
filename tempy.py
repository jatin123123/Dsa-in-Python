arr = [1,3,13,2,25,23,2,4,2,99]

def largest(arr):
    largest = arr[0]
    second_largest = arr[0]
    for i in range(len(arr)):
        if largest < arr[i]:
            largest = arr[i]
    for i in range(len(arr)):
        if arr[i] != largest and arr[i] > second_largest:
            second_largest = arr[i]
    return largest , second_largest

print(largest(arr))