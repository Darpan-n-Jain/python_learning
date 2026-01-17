from array import *
a=array('i',[1,2,3,4,5])
print(a)
print(a[1])
print(len(a))
a.append(6)#add element at last
print(a)
a.extend([7,8,9])#add multipel element at last
print(a)
a.insert(1,10)#insert element at given index
print(a)
a.pop(1)#removes element at index and returns values
print(a)
a.pop()#removes last element
print(a)
a.remove(4)#removes a perticular value
print(a)
b=array('i',[10,11,12,13])
c=array('i')
c=a+b#mearging of array(possible only if both array ahe same data type)
print(c)
print(a[0:3])#slicing of array
