num=123
n=num
fact = []
from math import sqrt
# Brut

# for i in range(1,num+1):
#     if n % i ==0:
#         fact.append(i)
#     else:""


# average

# for i in range(1,int(num/2)+1):
#     if n%i== 0:
#         fact.append(i)
        
#     else:""
# fact.append(num)
# print(fact)

# best 
for i in range(1,int(sqrt(num))+1):
    if n % i == 0:
        fact.append(i)
        if n//i!=0:  # Avoid adding the square root twice
            fact.append(n // i)

print(sorted(fact))
