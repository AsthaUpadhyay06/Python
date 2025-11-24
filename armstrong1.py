num = int(input("Enter a number: "))
order = len(str(num))
s = sum(int(digit) ** order for digit in str(num))
if num == s:
    print("Armstrong number")
else:
    print("Not an Armstrong number")