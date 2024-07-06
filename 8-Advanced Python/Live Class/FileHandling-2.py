fileName = "hello.py"

with open (fileName, "rt") as x:
    # content = x.readline()
    # content = x.readlines()

    # content = x.read()
    # print(content)

    for line in x:
        print(line, end="")