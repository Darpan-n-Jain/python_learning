t=(1,4,9,16,25,36,49,64,81,100)
a=int(input("enter number:"))
b=len(t)
i=0
while i<b-1 :
    if a==t[i]:
        print("number found at index:",i)
        break
    else:
        i += 1
