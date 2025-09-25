import random
import string

length = 8
password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
print("Random Password:", password)
