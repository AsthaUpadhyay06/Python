# text = input("Enter a string: ")
# print("Reversed string:", text[::-1]) 

text="my name is astha"
reversed=""
for ch in text:
    reversed=ch + reversed
    print("reversed is" ,reversed)