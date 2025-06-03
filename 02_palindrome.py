num=123214

n=num
result=0
while n>0:
    digit = n%10
    result=(result*10)+digit
    n=n//10

if result == num :
    print("num is an pailndrome number")
else:
    print("No this is not an pilndrome number")


