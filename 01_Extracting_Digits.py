number = 451512 
dig = []
num = number


while num > 0:
    di = num%10
    dig.append(di)
    num = num//10
    
print(dig)

