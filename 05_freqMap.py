num = [1,1,3,4,23,5,2,4,23,2,1,3]

dist = {}

for i in range(len(num)):
    if num[i] in dist:
        dist[num[i]] +=1
    else:
        dist[num[i]] = 1
        
print(dist)