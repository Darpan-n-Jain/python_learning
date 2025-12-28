#def fun_name (paramaters):
def sum(a=1,b=1):#par1=value;are defult values are conciderd if no valu is present in calling
    s=a+b
    return s
x=int(input("enter 1st number:"))
y=int(input("enter 2st number:"))
b=sum(x,y)
print("sun of numbers is:",b)

def avg(a,b,c):
    s=(a++b+c)/3
    return s
x=int(input("enter 1st number:"))
y=int(input("enter 2st number:"))
z=int(input("enter 3st number:"))

d=avg(x,y,z)
print(d)