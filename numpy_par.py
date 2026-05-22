import numpy as np
a= np.array([1,2,3])
b= np.array([[1,2,3],[4,5,6]])
print(b)
print(b.ndim)#how many dimension dose array haye
print(b.shape)#gives no of r,c in array
print(a.itemsize)
z=np.array_equal(a,b)
print(z)