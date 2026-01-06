class car:
    @staticmethod
    def s():
        print("car started")
    @staticmethod
    def st():
        print("car stoped")
class tcar (car):
    def __init__(self,brand):
        self.brand=brand
c1=tcar("toyota")

class f(tcar):
    def __init__(self,type,b):
        self.type=type
        super().__init__(b)#super(). -> used to acces praent
        brand=b
c2=f("pretol","toyota")
c2.s()
c2.st()

class a:
    a="class a"
class b:
    b="class b"
class c(a,b):
    c="class c"
    
t=c()
print(t.a)
print(t.b)
print(t.c)
print(c2.brand)