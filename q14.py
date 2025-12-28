def ln(list):
    x=int(len(list))
    return x

marks = ["darpan",52.4,94,96.8,87,20,55.5,99]
print(ln(marks))
def prl(list):
    for i in list:
        print(i, end=" ")#end ="value" at end write value dosent go to next line
    else:
        print("\n")
prl(marks)
def fact(n):
    i=1
    s=1
    while i<=n:
        s*=i
        i+=1
    return s

print(fact(3))
def con(a):
    a=a*83
    return a
print(con(2))
def ero(a):
    if(a%2==0):
        s="even"
    else:
        s="odd"
    return s
n=int(input("enter a num:"))
print("your number is",ero(n))

#rec
def rfact(a):
    if(a==0 or a==1):
        return 1
    else:
        return a * rfact(a-1)
print(rfact(3))
def sumr(a):
    if(a==1):
        return 1
    else:
        return a + sumr(a-1)
    
print(sumr(n))
def prlr(list,a=0):
    n=len(list)
    if a==len(list):
        return
    else:
        print(list[a])
        print(list[a+1])
print(prl(marks))
        