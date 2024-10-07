# Prompt the user for input
a,b,c = input("Enter three values separated by spaces: ").split()

# Print the values
if a>b and a>c:
    print('a is the greatest')
elif b>a and b>c:
    print('b is the greatest')
else:
    print('c is the greatest')
    