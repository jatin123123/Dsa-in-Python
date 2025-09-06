number = 121
num = number
palin = 0

while num > 0 :
    di = num%10
    palin = (palin*10)+di
    num = num//10
    
if palin == number:
    print("Yes")
else:
    print("NO")
