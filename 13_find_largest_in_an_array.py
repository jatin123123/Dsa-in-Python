arr = [45,4,216,4164,41,1948844,1,484,6412444,448,99999999,1]
largest = arr[i]
for i in range(len(arr)):
    if arr[i]>=largest:
        largest = arr[i]
print(largest)  