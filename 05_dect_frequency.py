numbers = [1,1,1,1,51451,5,5,48,48,5,6]

dist = {}

for i in numbers:
    if i in dist:
        dist[i] +=1
    else:
        dist[i] = 1
        
        
print(dist)