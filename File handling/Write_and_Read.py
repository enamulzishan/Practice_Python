with open("me.txt", "w+") as file:
    file.write("\ngalaktus/red skull")
    file.seek(0)
    read = file.read()
    print(read)