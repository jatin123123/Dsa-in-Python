num = 153

#  output num = 153 = 1*lnt(num)+5*lnt(num)+3*lnt(num) is equal to num which is 153
n = num
arm = 0

while n > 0:
    ld = n % 10
    arm += ld**len(n)
    n = n//10
print(arm)
    
    