import numpy as np


# x = np.array([10, 20, 30])

# print(x * 2)      # element wise multiply
# print(x + 5)      # addition
# print(np.mean(x)) # average
# print(np.max(x))  # max value


# a=np.arange(1000)
# print(%timeit a**2)

# a=np.array([12,345,67])
# print(a)
# print(a.ndim)  # Dimension => 1D ARRAY
# print(a.shape)
# print(len(a))
# b=np.array([[1,3,4],[3,5,6]])
# print(b)
# print(b.ndim)  # Dimension => 2D ARRAY
# print(b.shape)
# c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(c)
# print(c.ndim) 
# print(c.shape)
# a=np.arange(10)
# print(a)
# b=np.arange(1,10,2) # start and (exclusive) ,step
# print(b)
# #using linspace
# a=np.linspace(1,2,6) # start ,end ,number of points
# print(a)
 

#  #common arrays
a=np.ones((3,5))
print(a)
a=np.zeros((3,5))
print(a)
print(a.dtype)


# # c=np.eye(3)
# # print(c) # identity
# # a=np.diag([1,2,3,4]) #diagonal
# # print(a)

# # # a=np.random.rand(4)
# # # print(a)

# a=np.random.randn(4) #return a sample (or samples ) from the
# print(a)

# a=np.arange(10)
# print(a.dtype)

# a=np.arange(10,dtype='float64')
# print(a.dtype)

# d=np.array([1+2j,2+4j]) #comples datatypes
# print(d.dtype)

# b=np.array([True ,False,True ,False]) #boolean datatype
# print(b.dtype)

# s=np.array(['Ram','Robert','Rahim'])
# print(s.dtype)

# a=np.arange(10)
# print(a[5])

# a=np.diag([1,2,3]) 
# print(a[2,2])
# # assigning value
# a[2,1]=5
# print(a)


# a=np.arange(1,10,2) # start and (exclusive) ,step
# print(a)


# a=np.arange(10)
# a[5:]=10
# print(a)

# b=np.arange(5)
# a[5:]=b[::-1]

# print(a)

# a=np.arange(10)
# print(a)
# b=a[::2]
# print(b)
# print(np.shares_memory(a,b))
# b[0]=10
# print(np.shares_memory(b,a))
# print(b)

# a=np.arange(10)
# print(a)
# c=a[::2].copy()
# print(np.shares_memory(a,c))
# c[0]=10
# print(np.shares_memory(c,a))
# print(c)
# print(a)




s=np.array(['Ram','Robert','Rahim'])
print(s.dtype)


# mport numpy as np


# # x = np.array([10, 20, 30])

# # print(x * 2)      # element wise multiply
# # print(x + 5)      # addition
# # print(np.mean(x)) # average
# # print(np.max(x))  # max value


# # a=np.arange(1000)
# # print(%timeit a**2)

# # a=np.array([12,345,67])
# # print(a)
# # print(a.ndim)  # Dimension => 1D ARRAY
# # print(a.shape)
# # print(len(a))
# # b=np.array([[1,3,4],[3,5,6]])
# # print(b)
# # print(b.ndim)  # Dimension => 2D ARRAY
# # print(b.shape)
# # c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# # print(c)
# # print(c.ndim) 
# # print(c.shape)
# # a=np.arange(10)
# # print(a)
# # b=np.arange(1,10,2) # start and (exclusive) ,step
# # print(b)
# # #using linspace
# # a=np.linspace(1,2,6) # start ,end ,number of points
# # print(a)
 

# #  #common arrays
# # a=np.ones((3,5))
# # print(a)
# a=np.zeros((3,5))
# print(a)
# print(a.dtype)


# # c=np.eye(3)
# # print(c) # identity
# # a=np.diag([1,2,3,4]) #diagonal
# # print(a)

# # # a=np.random.rand(4)
# # # print(a)

# a=np.random.randn(4) #return a sample (or samples ) from the
# print(a)

# a=np.arange(10)
# print(a.dtype)

# a=np.arange(10,dtype='float64')
# print(a.dtype)

# d=np.array([1+2j,2+4j]) #comples datatypes
# print(d.dtype)

# b=np.array([True ,False,True ,False]) #boolean datatype
# print(b.dtype)

# s=np.array(['Ram','Robert','Rahim'])
# print(s.dtype)

# a=np.arange(10)
# print(a[5])

# a=np.diag([1,2,3]) 
# print(a[2,2])
# # assigning value
# a[2,1]=5
# print(a)


# a=np.arange(1,10,2) # start and (exclusive) ,step
# print(a)


# a=np.arange(10)
# a[5:]=10
# print(a)

# b=np.arange(5)
# a[5:]=b[::-1]

# print(a)

# a=np.arange(10)
# print(a)
# b=a[::2]
# print(b)
# print(np.shares_memory(a,b))
# b[0]=10
# print(np.shares_memory(b,a))
# print(b)

# a=np.arange(10)
# print(a)
# c=a[::2].copy()
# print(np.shares_memory(a,c))
# c[0]=10
# print(np.shares_memory(c,a))
# print(c)
# print(a)







