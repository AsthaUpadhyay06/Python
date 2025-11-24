text = input("Enter a string: ")
vowels = "aeiouAEIOU"
v_count = 0
c_count=0

for char in text:
    if char.isalpha(): 
      if char in vowels:
        v_count+=1
    else:
        c_count+=1

print("Number of vowels:", v_count)
print("Number of consonants:", c_count)