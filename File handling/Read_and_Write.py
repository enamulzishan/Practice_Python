with open("me.txt", "r+") as file:
    read = file.read()
    print(read)
    file.write("\nEGO")