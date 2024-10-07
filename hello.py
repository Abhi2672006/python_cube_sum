dict={}
print("enter your marks in hindi ,punjabi,maths:")
h=int(input("hindi:"))
p=int(input("punjabi:"))
m=int(input("maths:"))
dict.update({"maths":m})
dict.update({"hindi":h})
dict.update({"punjabi":p})
print(dict)