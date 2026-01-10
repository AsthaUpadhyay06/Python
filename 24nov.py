# Python me list ek ordered, mutable (change ho sakne wala) collection hoti hai — yani iske elements ko add, remove, update sab kar sakte ho.

# my_list = [10, 20, 30]


# Python me tuple (ट्यूपल) ek ordered, immutable (change na hone wala) collection hota hai — list ki tarah hota hai, bas usme values badal nahi sakte.

# my_tuple = (10, 20, 30)


# t=()
# t=(1,2,3)
# print(t)

# #touple with mixed data type

# t=(1,'raju',25,'abs')
# print(t)

# # nested tuple

# t=(1,(2,3,4),[1,'rajuu',34,'absd'])
# print(t)
# t=('satishh')
# print(type(t))
# t=('asthaaa',)
# print(t)


# #parenthesis is optional

# t=34,45,56
# print(type(t))
# print(t)
# print(t[0])

# print(t[-1]) # print data value

# t = (34, (45, 56, 67))
# print(t[1][2])   # yahan t[1] ek tuple hai



# # slicing
# t=(1,2,3,4,50)
# print(t[1:4])
# print(t[:-3])
# print(t[:])

# #creating tuple 
# t=(1,2,3,4,[5,6,7])  # tuple me change nhu hota but list me hota haii
# # t[2]='x' #will get tuple

# t[4][1]='astha'
# print(t)

# t=(1,2,3)+(4,5,6)
# print(t)

# # print tuple number of timess
# t=(1,2,3,4,5,6,6)
# t=((3,)*4)
# print(t)


# #deletion of tuple
# t=(1,2,3,4)
# del t

# t=(3,4,56,78,3,3,3,3,4)
t = (3,4,56,78,3,3,3,3,4)
t.count(3)
print(t.count(3))   # 3 kitni baar aya



# print(t.index(56))

#tuple membershipt=
t=(1,2,3,4,5,6)
print(1 in t) # true or false

#length
print(len(t))


#tuple sort
t=(4,5,6,78,43,24,54)
new=sorted((t))
print(new)
print()

#get the largest and minimum element in a tuple
print(max(t))
print(min(t))
#get sum of tuple
print(sum(t))
