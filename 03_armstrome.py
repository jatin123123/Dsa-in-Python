num = 153
n = num
result = []
arm=0
lenth = len(str(num))
while n>0:
    digit = n%10
    result.append(digit)
    n = n//10
    arm += digit**lenth

if num == arm:
    print("IT is an armstrome number")
else:
    print("It is not an armstrome number")

