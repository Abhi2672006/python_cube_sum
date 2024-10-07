print('Enter a number till you want fibonacci series:')
n=int(input())
n1=0
n2=1
count=int()
for i in range(1,n):

    n3=n2+n1
    n1=n2
    n2=n3
    if n==n3:
        count=1

if count==1:
    print('a fibonacci number')
else:
    print('not a fibonacci number')    
