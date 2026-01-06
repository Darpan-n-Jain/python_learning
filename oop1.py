class info:
    name= "name"
    roolno="123"
    collage="iiitn"
dar=info()
name=input("enter your name:")
rol=int(input("enter your rool no. :"))
dar.name=name
dar.roolno=rol
print(dar.name)
print(dar.roolno)
print(dar.collage)

class i:
    def __init__(self,name,marks,sub):#conctcor self->to point at itself nessey part of format rest are args
        self.name=name
        self.marks=marks
        self.sub=sub
    def he(self):
        print("hello",self.name,"wellcome to IIITN")
    @staticmethod #used to avoid self
    def h():
        print("hello")
d=i("darpan",97,"oop")
d1=i("abc",80,"bc")
print(d.name)
print(d.marks)
print(d.sub)
print(d1.name)
print(d1.marks)
print(d1.sub)
i.he(d)
i.h()
del d#used to delete
class a:
    def __init__(self,n,p):
        self.name="n"
        self.__pas="p"#private