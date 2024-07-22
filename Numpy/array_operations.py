import numpy as np
#dimension
a= np.array([(1,2,3),(5,6,7)])
print(a.ndim)
#Byte size
print(a.itemsize)
print(a.dtype)
print(a.size)
print(a.shape)
#print 5 value between two values
a=np.linspace(1,3,10)
print(a)
#axis sum
a= np.array([(1,2,3),(5,6,7)])
print(a.sum(axis=0))
print(a.sum(axis=1))
#addition,sub,mul,div
a= np.array([(1,2,3),(5,6,7)])
b= np.array([(1,2,3),(5,6,7)])
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#vertical stacking and horizontal sacling of array
a= np.array([(1,2,3),(5,6,7)])
b= np.array([(1,2,3),(5,6,7)])

print(np.vstack((a,b)))
print(np.hstack((a,b)))
#converting array in a single column
a= np.array([(1,2,3),(5,6,7)])
print(a.ravel())

