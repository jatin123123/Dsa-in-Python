numbers = [21,324,123,1,23,121,123,4454,97667,563423,21313,32423,523543,23423423,344353,1,221,122,]

disct = {}

for i in numbers:
    if i in disct:
        disct[i] += 1
    else:
        disct[i]=1

print(disct)


optimal = {}

for i in numbers:
    optimal[i] = optimal.get(i,0)+1

print(optimal)