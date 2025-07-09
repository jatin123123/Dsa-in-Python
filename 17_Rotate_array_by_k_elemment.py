arr = [1,2,3,4,5]
n = len(arr)
k = 3

rotation = k%n
# optimal
# for i in range(rotation):
#     temp = arr[-1]
#     for j in range(n-1,-1,-1):
#         arr[j] = arr[j-1]
#     arr[0] = temp


# better

def reverse(arr,l,r):
    while l < r :
        arr[l],arr[r] = arr[r],arr[l]
        l+=1
        r-=1

reverse(arr,n-k,n-1)
reverse(arr,0,n-k-1)
reverse(arr,0,n-1)

print(arr)