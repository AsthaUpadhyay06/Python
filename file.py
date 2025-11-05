# Write to file
with open("data.txt", "w") as f:
    f.write("Hello, I am learning Python!")

# Read File
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
