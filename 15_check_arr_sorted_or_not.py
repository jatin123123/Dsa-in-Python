arr = [10,20,30,40,50,60,70,80,90]
arr2 = [45,2,646,16,4845,1]

sorted = True
for i in range(1,len(arr)):
    if arr[i]<arr[i-1]:
        sorted = False
        break


if sorted == True:
    print("sorted")
else:
    print("Not sorted")
        
