with open("demo.txt", "w+") as file:
    file.write("\nThis is a demo text file.")
    read = file.read()
    print(read)