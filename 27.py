# name=input("enrter your name ")
# name="astgaaa"
# print("name ",name)


#conditions 

# dayofweek=input("enter day").lower()
# print(dayofweek)
# if dayofweek=="saturday" or dayofweek=="sunday":

#     print("i will learn")
# else:
#     print("i will practice")  
# num1=int(input("enter num1"))
# num2=int(input("enter num2"))    
# choice=input("enter operations")
# if choice =="+":
#     print("addition",num1+num2)
# elif choice =="-":
#     print("subn",num1-num2)
# elif choice =="*":
#     print("multiply",num1*num2)
# elif choice =="%":
#     print("remainder",num1%num2)


# loops
# list is a data structure which can hold multiple values


listofcloud = ["Aws", "azure", "gcp", "ibm", "oracle", "alibaba"]
cloud = "gcp"

# Original list print
print(listofcloud)
# Output: ['Aws', 'azure', 'gcp', 'ibm', 'oracle', 'alibaba']

# Add new clouds
# listofcloud.append("salesforce")
# listofcloud.append("IBM")

# # Updated list print
# print(listofcloud)
# listofcloud.insert(2,"heroku")
# print(listofcloud)
# print(len(listofcloud))
# listofcloud.insert(0,"HelloClod")
# print(listofcloud)
# # iteration of list
# for cloud in listofcloud:
#     print(cloud)
# for i in range(1,11):
#     print("hello")


import os 
print(os.system('df -h'))
print(os.system('uptime'))
print(os.system('df -h'))  #RAM