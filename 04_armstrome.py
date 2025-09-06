number = 153
num = number
arm = 0
n = len(str(number))
while num > 0:
    di = num%10 
    arm = (di**n) + arm 
    num = num//10 
    
if arm == number:
    print("Yes")
else:
    print("NO")