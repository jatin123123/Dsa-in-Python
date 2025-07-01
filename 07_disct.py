n=[2,5,2,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,10]
m=[23,54,12,1,5,3,2,5,8,90,23,5,34,23,23,24,1]

disct = {}

for i in n:
    if i in disct:
        disct[i] +=1
    else:
        disct[i] = 1

for i in m:
    if i>10 or i<-1:
        print(0)
    else:
        print(disct[i])
