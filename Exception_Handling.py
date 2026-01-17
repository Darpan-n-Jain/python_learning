a=input("enter the number:")
print("multipaction tabel for",a,"is:\n")

try:
    for i in range (1,11):
        print(int(a),"*",i,"=",int(a)*i)
except Exception as e:
    print("please enter a number!\n\n")
    
print("end of program")