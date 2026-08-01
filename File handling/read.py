file = open("/OSTAD/File Handling/example.txt", "r")
content = file.read()
print(content)
file.close()


file = open("/OSTAD/File Handling/example.txt", "r")
content = file.readline()
print(content)
file.close()

file = open("/OSTAD/File Handling/example.txt", "r")
content = file.readlines()
print(content)
file.close()

file = open("/OSTAD/File Handling/example.txt", "r")

for line in file:
    print(line)
file.close()
