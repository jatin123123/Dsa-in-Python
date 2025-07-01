num=12321
n = num
pail = 0

while n > 0:
    ld = n%10
    pail = (pail*10)+ld
    n = n//10

if pail == num:
    print("number is Palindrome")
else:
    print("Number is not an Palindrome")
