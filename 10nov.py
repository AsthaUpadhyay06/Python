# a=[2,3,2,4,3,5,5]
# seen=[]
# out=[]
# for x in a:
#     if x not in seen:
#         seen.append(x)
#         out.append(x)
# print(seen)   
# print(out)   


# lst=[1,23,45,32,33]
# target=33
# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] + lst[j] == target:
#             print("Indexes:", i, j)


#running sum

# lst=[1,2,3,4]
# sum=0
# seen=[]
# for i in range(len(lst)):
#     sum+=lst[i]
#     seen.append(sum)
#     print(seen)


lst=[1,2,0,5,4,0,4,3,0,6]
for i in lst:

    if i==0:

        lst.append(0)

        lst.remove(i)

print(lst)       


       
