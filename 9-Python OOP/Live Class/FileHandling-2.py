fileName = "hello.py"

with open(fileName, "r") as x:
    # content = fp.read()
    # content = fp.readline()
    content = x.readlines()
    print(content)