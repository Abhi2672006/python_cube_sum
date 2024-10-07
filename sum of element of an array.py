print('Enter the number of values you want to input:')
n=int(input())
arr=[]
max=0
print('enter the elements of array:')
for i in range(0,n):
    arr.append(int(input()))
for i in range(0,n):
    if arr[i]>max:
        max=arr[i]
print('max number is :',max)   