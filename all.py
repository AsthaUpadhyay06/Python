lst=[1,2,3,4]
print(all(lst))

// jab bhinlst k anadar sari value true hogi tabhi all true return karega
// or false jab value me se koi ek bhi false hoga to all false return karega
// lst=[1,2,0,4]
// print(all(lst)) // false return karega

lst=[]
print(all(lst)) // true return karega kyuki empty list me koi false value nahi hoti

lst=[false,1,3]
print(all(lst)) // false return karega kyuki list me false value hai

//jab tk sari value true nahi hoti tab tk all false return karta rahega