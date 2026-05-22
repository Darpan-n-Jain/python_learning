class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def show(self):
        print(self.real,"+",self.img,"i")
    def __add__ (self,n2):# __add__ -> for overloding + similary sub for * -> __mul____ similary truediv(for /)and mod(for %)
        real=self.real+n2.real
        img=self.img+n2.img
        return complex(real,img)
        
n1=complex(10,3)
n2=complex(20,2)
n1.show()
n2.show()
n3=n1 + n2
n3.show()