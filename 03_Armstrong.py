num = 153

#  output num = 153 = 1*lnt(num)+5*lnt(num)+3*lnt(num) is equal to num which is 153
n = num
arm = 0
lnt = len(str(num))
while n > 0:
    ld = n % 10
    arm += ld**lnt
    n = n//10
print(arm)