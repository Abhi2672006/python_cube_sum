import math
sum=0
n=int(input())
c=0
temp=n
while n>0:
    n=n//10
    c=c+1
n=temp
while n>0:
    r=n%10
    sum=sum+pow(r,c)
    n=n//10
print(sum)
if temp==sum:
    print('armstrong')
else:
    print('not armstrong')    
