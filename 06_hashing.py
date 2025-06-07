n = [1,5,2,6,2,6,2,7,9,0,1,10,6,0,2,5]
m = [1,243,23,65,3,7,3,2,7,34,75,34,8,9]

has_list = [0]*11

for i in n:
    has_list[i] += 1
for i in m:
    if i > 10 or i<-1:print(0)
    else:
        print(has_list[i])


