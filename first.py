
# list=[1,2,3];
# b=a;
# b.append(4);
# print(id(list));



# a=[1,2,3]
# print(id(a))
# b=a
# b.append(4)
# print(b)

# print(id(a))
# print(id(b))

# print(a)

# print("Astha")


# type functions which are used to check the data type of a variable


# a=33
# print(type(a))
# b="adbd fkjdfkdf fefff"
# print(type(b))
# def func():
    # pass => # placeholder which signifies that their is no work to be done

# print(type(func))


# class demo:
#     pass
# print(type(demo))  # in python each and everything is an object       and each and everything is a class

 # doc strings  are used to document a function or a class or 
 # doc strings are written in triple quotes(inverted commas)
 # 
def fact(n):
    """calculate the factorial of a number n (n) 
    n(int : a non negative integer)
    returns the value of n"""
    return 1 if n==0 else n*fact(n-1)

help(fact)   # help is a inbuilt function which is used to see the doc string of a function or a class



