arr = [1,1,1,1,2,6,2,5]
dist = {}

# for i in range(len(arr)):
#     dist[arr[i]] = 1
        
# ind = 0   
# for i in dist:
#     arr.insert(ind,i)
#     arr.pop()
#     ind+=1
    
    
    
# optimal

for i in range(len(arr)):
    j = i+1
    if arr[i] != arr[j]:
         j+=1
         arr[j]
    
print(arr)