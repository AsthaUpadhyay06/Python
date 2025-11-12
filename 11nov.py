# s={1,2,3}  # { set ko iske andar likhte haii}
# print(s)
# print(type(s))    #<class 'set'>


# set not allowed duplicates value
# s={1,22,3,4,22,3,4,6}
# print(s)


#we can make set from list
# s=set([1,22,3,4,5,3,2])
# print(s)

# initislize a set with set() method

# s=set()
# print(type(s))


 # set indexing ko support nhi KRTa
# s={1,3}
# print(s[0]) 


# s={1,3,5,7}
# s.add(6)
# print(s)
# # s.update([5,6,1])
# print(s)

# # add list and set
# s={2,4}
# s.update([34,7],{4,6,46})
# print(s)


# # #remove by using dis card and remove
# # a={1,2,3,4,5}
# # # a.discard(4)
# # # print(a)
# # a.remove(7)  # error exist nhi hai 7


#remove random element
# # s={1,2,3,4,5}
# # s.pop() #remove random element
# # print(s)

# #clear 
# s={1,2,3,4,5}
# s.clear()
# print(s)

# pyhton set operation
# union
# set1={1,2,3,4,5}
# set2={3,4,5,6,7}
# # print(set1|set2)

# # # another way to geeting union
# # print(set1.union(set2))

# #intersection
# print(set1 & set2)o v
# print(set1.intersection(set2))
# # difference set of elements that are only in set one not in set 2
# print(set1-set2)
# print(set1.difference(set2))
 
# # symmetric difference : set of elements in both set1 and set2 
# # except those that are common in both

# print(set1^set2)
# #use symettric difference function
# print(set1.symmetric_difference(set2))

# #find subset
# x={"a","b","c","d"}
# y={"c","d"}
# print("set 'x' is subset of 'y'?",x.issubset(y))

#Frozen set 

s1=frozenset([1,2,3,4])
s2=frozenset([3,4,5,6])
#try to add element gives eror
# s1.add(5)

# print(s1|s2)
# print(s1 & s2)


a={"hello","astha","upadhyay","aayu"}

for i in a:
    if 'h' in a:
        count+=count
        print(a)
   
