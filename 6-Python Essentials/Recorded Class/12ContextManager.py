with open("myFile.txt", "r") as fp: #No need to manual closing file
    # content = fp.read()
    # content = fp.readline()
    content = fp.readlines()
    print(content)

