
print("select operation")
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
choice=input("enter choice(1/2/3/4):")
a=int(input("enter first numbert:"))
b=int(input("enter second numbert:"))
if choice=='1':
    print(a,"+",b,"=",a+b)
elif choice=='2':
    print(a,"-",b,"=",a-b)    
elif choice=='3':
    print(a,"*",b,"=",a*b)  
elif choice=='4':
    print(a,"/",b,"=",a/b)  
else:
    print("invalid")
