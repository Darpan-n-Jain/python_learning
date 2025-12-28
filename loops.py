#while condtion:
i=0
while i<=10 :
    print(i)
    i +=1
    
print(i)

a=100
while a>0 :
    print(a)
    a -=1
    
#for var in list/tupname : (start form 0 and end at end of tup or list)(auto increment)
t=(1,4,9,16,25,36,49,64,81,100)
for a in t :
    if a== 81:
        break
    else:
        print("num not found")
else :#part of for runs after loops ends can be skiped (only with no bresk condition )
    print("loop ended")
    
    
#range(start,stop,step)fot 2 valuse satar and stop and for 1 stop
for i in range(0,10,2):
    print(i)

#pass keyword to run empty for loop otherwise it gives error
for i in range(0,10,2):
    pass
else:
    print("loop ended")