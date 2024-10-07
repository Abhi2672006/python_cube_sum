n=int(input('enter the number to check is palindrome or not:'))
l=n
r=0
while n!=0:
    x=n%10
    r=x+r*10
    n=n//10

if r==l:
    print('is palindrome')
else:
    print('not palindrome')