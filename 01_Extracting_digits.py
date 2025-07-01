# Extracting Digits 

num=45612
n = num
n1 = num
# output = [4,5,6,1,2]

lnt = 0
while n1 > 0:
     n1 = n1 // 10
     lnt +=1

ex = [0]*lnt

index = lnt-1


while n>0:
    ld = n%10
    ex[index] = ld
    index -=1
    n = n//10
    
print(ex)