arr = [1,2,0,3,0,4,0,5] # output -> 1 2 3 4 5 0 0 0 
temp =[]

# brut ----------------------------------------------------------------
# for i in range(len(arr)):
#     if arr[i]!=0:
#         temp.append(arr[i])
# for i in range(len(temp)):
#     arr[i] = temp[i]
# for i in range(len(temp),len(arr)):
#     arr[i] = 0
# print(arr)

# optimal ----------------------------------------------------------------


for i in range(len(arr)):
    if arr[i] == 0:
        for j in range(i,len(arr)):
            if arr[j] !=0:
                arr[i],arr[j] = arr[j],arr[i]
                break
                
                
print(arr)