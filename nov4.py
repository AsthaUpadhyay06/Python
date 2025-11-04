emptylist=[]
# print(emptylist) 
lst3=[[1,2],[3,4]]  # lists of list
lst4=[1,'eadd',34,4.45]  # list of different datatypes 
# print(lst4)
# print(lst3)
# print(len(lst3))
# print(len(lst4))  #len() nested elements ke andar ke count nahi karta — sirf top-level elements count karta hai.
# lst3.append("dffg")
# print(lst3)
# lst4.append(45)  # append kuch rerurn nhi krta islye print(list.append(44)) likhne me none aata hai
# print(lst4)
# lst4.insert(2,"astha")
# print(lst4)
# lst3.remove([3,4]) # starting se dhoodna start kr deta hai
# print(lst3)
# lst3.append(lst4)
# print(lst3)
# lst3.extend(lst4)
# print(lst3)
# del lst3[1]
# print(lst3)
# numbers = [10, 20, 30, 40]
# removed = numbers.pop(1)   # index 1 pe element 20 hai
# print(numbers)
# print("Removed:", removed)
# numbers.remove(20)
# print(numbers)

#keyword 'in' is used  to test 

# lst=['one','two','three']
# if 'one' in lst:
#     print("AI")
# if 'ornrf' not in lst:
#     print("ml")
# lst.reverse()
# print(lst)   
# num=[34,54,22,45,32,34]
# sortee=sorted(num)
# print(sortee)  # print in ascending order
# sorted_lst=sorted(num,reverse=True)  # descending order
# print(sorted_lst)

# astha=[23,45,"addf",56,66]
# sort=sorted(astha)
# print(astha.sort)

lst=[1,2,3,4,5,55,43]
abc=lst
abc.append(6)
sort=sorted(lst)
print(sort)




