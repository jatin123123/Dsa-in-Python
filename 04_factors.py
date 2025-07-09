num=123

factor = []

for i in range(1,int(num/2)):
    if num % i == 0:
        factor.append(i)
        
factor.append(num)
print(factor)