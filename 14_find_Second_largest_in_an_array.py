arr = [10,20,30,40,50,60,70,80,90]
largest = arr[0]
second_largest = 0


for i in range(len(arr)):
    if arr[i]>= largest:
        second_largest = largest
        largest = arr[i]

# print(largest  , second_largest)


for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]
        
    
        
print(largest , second_largest)