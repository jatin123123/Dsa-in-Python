# Extracting Digits 

num=4123421321

n=num
extracted=[]
while n>0:
    digit = n%10
    extracted.append(digit)
    n = n//10
extracted.reverse()
print(extracted)

