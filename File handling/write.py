file = open("me.txt", "w")
file.write("Hello, this is a test file.")
file.write("This is the second line.")
file.close()

# Appending to a file
file = open("me.txt", "a")
file.write("This is an appended line.")
file.close()


import os

if os.path.exists("me.txt"):
  print("The file exists.")
else:
  print("The file does not exist.")

