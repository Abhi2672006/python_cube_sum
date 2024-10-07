sum=0
choice='yes'

while choice=='yes':
    n=int(input())
    if n%4==0:
        sum=sum+n
    print('if you want to continue type yes or no:')
    choice=input()
print(sum)        